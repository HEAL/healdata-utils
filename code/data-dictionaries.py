from healdata_utils.csvtemplate import convert_template_csv_to_json
from healdata_utils.config import studies,ROOT_DIR

input_files = (ROOT_DIR/'data-dictionaries'/'bacpac'/'input').glob("*")
for input_file in input_files:
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
