''' 
conversion from input format (e.g., csv template, etc)
to json format for data dictionaries
''' 

from healdata_utils.transforms.csvtemplate.conversion import convert_template_csv_to_json
from healdata_utils.config import studies,ROOT_DIR
import json
# current template with examples from HEAL repo

template_fields = convert_template_csv_to_json(
    csvtemplate_path=("https://raw.githubusercontent.com/HEAL/" 
    "heal-metadata-schemas/variable-level-metadata/variable-level-metadata-schema/templates/"
    "template_submission.csv"),
)
with open(ROOT_DIR/"data-dictionaries"/"template"/"output.json",'w') as f:
    json.dump(
        {
            'title':f"template",
            'description': 'This is a HEAL metadata template with representative examples' ,
            'data_dictionary':template_fields
        },
        f,
        indent=4
    )

# Did above 
del studies['template']

for study,info in studies.items():
    data_dictionaries = info.get('data_dictionaries')
    if data_dictionaries:
        for dd in data_dictionaries:
            if dd.get('conversiontype')=='csvtemplate':
                input_file = ROOT_DIR/'data-dictionaries'/study/'input'/dd['file_name']
                fields = convert_template_csv_to_json(input_file)
                with open(input_file.parents[1]/'output'/f"{input_file.stem}.json",'w') as f:
                    json.dump(
                        {'title':f"{study}-{dd['title']}",'data_dictionary':fields},
                        f,
                        indent=4
                        
                    )
