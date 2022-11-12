''' 
conversion from input format (e.g., csv template, etc)
to json format for data dictionaries

''' 

from healdata_utils.cli import to_json
from healdata_utils.config import studies,ROOT_DIR
import json
# current template with examples from HEAL repo

csvtemplate_path=("https://raw.githubusercontent.com/HEAL/" 
    "heal-metadata-schemas/variable-level-metadata/variable-level-metadata-schema/templates/"
    "template_submission.csv")
csvtemplate_props={
        'title':f"template",
        'description': 'This is a HEAL metadata template with representative examples' ,
    }
outputdir = ROOT_DIR/"data-dictionaries"/"template"/"output.json"   
to_json(csvtemplate_path,outputdir,csvtemplate_props)
# Did above 
del studies['template']

for study,info in studies.items():
    data_dictionaries = info.get('data_dictionaries')
    if data_dictionaries:
        for dd in data_dictionaries:
            if dd.get('conversiontype')=='csvtemplate':
                input_file = ROOT_DIR/'data-dictionaries'/study/'input'/dd['file_name']
                dd_json = to_json(
                    filepath=input_file,
                    outputdir=input_file.parents[1]/'output'/f"{input_file.stem}.json",
                    data_dictionary_props={'title':f"{study}-{dd['title']}"}
                )