import pyreadstat
import pandas as pd 
from healdata_utils.transforms.readstat.mappings import fieldmap,get_std_type
from pathlib import Path
#TODO: add original type and translated type
# commented out are file metadata
#TODO: incorporate missing values and ranges into missingVals
#TODO: make into a class 
#TODO: change framework to not rely on pandas and only convert to dict (and then use csv to json fxn)

def read_pyreadstat(file_path,**kwargs):
    ''' 
    reads in a "metadata rich file"
    (dta, sav,b7bdat)

    '''
    file_path = Path(file_path)
    ext = file_path.suffix 
    if ext=='.sav':
        read = pyreadstat.read_sav
    #TODO: other extensions
    # elif ext=='.sas7bdat':
    #     read = pyreadstat.read_sas7bdat

    return read(file_path,**kwargs)

def convert_meta_item_to_frame(meta_object,trg_name,meta_name):

    meta_item = getattr(meta_object,meta_name)
    if meta_name=='column_names':
        df = (pd.DataFrame([],index=pd.Index(meta_item,name='name'))

            )
    else:
        df = (
            pd.Series(meta_item)
            .rename(trg_name)
            .to_frame()
            .rename_axis(index='name')
        )
    return df 

def gather_metadata(meta_object,mappings):

    meta_list = []
    assert mappings.get('name')!=None,'Need to specify column_name in mappings'

    for trg_name,meta_name in mappings.items():
        meta_item_df = convert_meta_item_to_frame(meta_object,trg_name,meta_name)
        meta_list.append(meta_item_df) 

    meta_df = pd.concat(meta_list,axis=1)

    # across field logic
    meta_df.update(meta_df.apply(get_std_type,axis=1))
    meta_df['ordered'] = meta_df['format'].apply(lambda x: True if x=='nominal' else None)

    return meta_df

def convert_to_csvtemplate(meta_df):
    return (
        meta_df
        .applymap(lambda x: ('|'.join([f"{str(key)}={str(val)}" 
            for key,val in x.items()])) if type(x)==dict else x)
    )

def convert_to_jsontemplate(meta_df):
    return [
        x.dropna().to_dict() for n,x in meta_df.reset_index().iterrows()
    ]
def convert_readstat(file_path,to_json=True,to_csv=False):
    ''' 
    reads in a pyreadstat 
    and outputs both a json and
    csv template
    ''' 
    file_path = Path(file_path)

    df,meta = read_pyreadstat(file_path)
    #field name mappings
    mapping = fieldmap['pyreadstat'][file_path.suffix.replace('.','')]
    meta_df = gather_metadata(meta, mapping)

    if to_json:
        json = convert_to_jsontemplate(meta_df)
    else:
        json = None

    if to_csv:
        csv = convert_to_csvtemplate(meta_df)



    if to_json and not to_csv:
        return json 

    elif not to_json and to_csv:
        return csv
    else:  
        return json,csv



