from dataforge.sources.redcap.project import REDCapProject
from pathlib import Path
import re
import xmltodict
import pandas as pd
from healdata_utils.transforms.redcap.mappings import renamemap,recodemap

def __parse_redcap_filename(path):
    path = Path(path)
    return {
        'project_name':re.search("^[^_]+",path.name).group(0),
        'path':path.parent.as_posix()
    }

def _make_redcap_project(path):
    redcap_params = __parse_redcap_filename(path)
    project = REDCapProject(**redcap_params,input_type='metadata')
    return project

def make_tabular_form_metadata(path):
    def tabulate_form(form_name,form_object):
        return (
            pd.DataFrame([item.__dict__ for item in form_object.items])
            .assign(form=form_name)
            .set_index(['form','oid'])
        )

    project = _make_redcap_project(path)
    tabular_form_list = [
        tabulate_form(form_name,form_object) 
        for form_name,form_object in project.forms.items()
    ]
    return pd.concat(tabular_form_list)

def get_code_list(path):
    ''' 
    #NOTE: TEMPORORY SOLUTION: used until CodeList put into dataforge schemas
    creates a tabular data frame of 
    encodings, choices (if checkbox) and enums
    ''' 
    
    code_list = xmltodict.parse(Path(path).read_text())\
        ['ODM']['Study']['MetaDataVersion'].get('CodeList',None)

    if code_list:
        df = pd.DataFrame(code_list).fillna(value="")
        df['choice_num'] = df['@Name'].str.replace("^.*__","",regex=True)
        df['choices_dict'] = df['@redcap:CheckboxChoices'].apply(lambda choices:dict([[val.strip() 
            for val in item.split(",")] for item in choices.split("|")]) if choices else None)
        df['choice'] = df.apply(lambda row: row['choices_dict'][row['choice_num']]\
             if row['choices_dict'] else None,axis=1)
        df['encodings'] = df.apply(
            lambda row: {
                val['@CodedValue']:val['Decode']['TranslatedText']
                for val in row['CodeListItem']
            } if row['CodeListItem'] else None,
            axis=1
        )
        df['constraints.enum'] = df['encodings'].apply(lambda row:list(row.keys()) if row else None)
        df['name'] = df['@Name']
        return df[['name','choice','encodings','constraints.enum']]

def convert_redcap(path,data_dictionary_props={}):
    df = (
        make_tabular_form_metadata(path)
        .reset_index()
        .rename(columns=renamemap)
        .replace(recodemap)
        [renamemap.values()]
        .merge(get_code_list(path),on='name',how='left',validate="1:1")
    )
    df['description'].where(
            df['choice'].isna(),
            df['description']+"["+df['choice']+"]",
            inplace=True
        )
    df.description.fillna('No description',inplace=True)
    del df['choice']
    
    json = [s.dropna().to_dict() for i,s in df.iterrows()]
    data_dictionary = data_dictionary_props.copy()
    data_dictionary['data_dictionary'] = json
    return data_dictionary