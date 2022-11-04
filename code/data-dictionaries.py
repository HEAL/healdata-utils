from healdata_utils.csvtemplate import convert_template_csv_to_json
from healdata_utils.config import studies,ROOT_DIR
from frictionless import Resource
# current template with examples from HEAL repo

template_output = convert_template_csv_to_json(
    csvtemplate_path=("https://raw.githubusercontent.com/HEAL/" 
    "heal-metadata-schemas/variable-level-metadata/variable-level-metadata-schema/templates/"
    "template_submission.csv"), 
    jsontemplate_path=ROOT_DIR/"data-dictionaries"/"template"/"output.json"
    
)

input_files = (ROOT_DIR/'data-dictionaries'/'bacpac'/'input').glob("*")
for input_file in input_files:
    print(input_file)
    convert_template_csv_to_json(
        csvtemplate_path=input_file,
        jsontemplate_path=input_file.parents[1]/'output'/f"{input_file.stem}.json"
    )

# for study,info in studies.items():
#     input_files = (ROOT_DIR/'data-dictionaries'/study/'input').glob('*')
#     for input_file in input_files:
#         convert_template_csv_to_json(
#             csvtemplate_path=input_file,
#             jsontemplate_path=input_file.parents[1]/'output'/input_file.stem+'.json'
#         )
