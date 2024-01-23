import requests
from pathlib import Path
import pprint
import subprocess
import argparse
import yaml 

import healdata_utils

def copy_schemas(fork,branch):
    pp = pprint.PrettyPrinter(indent=2,compact=True, sort_dicts=False)
    jsonschema_url = (
      f"https://raw.githubusercontent.com/{fork}/heal-metadata-schemas/{branch}/"
      "variable-level-metadata-schema/schemas/jsonschema/data-dictionary.json"
    )
    csvschema_url = (
        f"https://raw.githubusercontent.com/{fork}/heal-metadata-schemas/{branch}/"
        "variable-level-metadata-schema/schemas/frictionless/csvtemplate/fields.json"
    )
    healjsonschema = requests.get(jsonschema_url).json()
    healcsvtemplate = requests.get(csvschema_url).json()

    healjsonschema_str = pp.pformat(healjsonschema)
    healcsvtemplate_str = pp.pformat(healcsvtemplate)

    py_schema_dir = Path(__file__).parents[1].joinpath("src/healdata_utils/schemas") 
    py_schema_dir.joinpath("__init__.py").write_text("from .jsonschema import healjsonschema\nfrom .frictionless import healcsvschema")
    py_schema_dir.joinpath("jsonschema.py").write_text(f"healjsonschema = {healjsonschema_str}")
    py_schema_dir.joinpath("frictionless.py").write_text(f"healcsvschema = {healcsvtemplate_str}")
    
    for f in ["jsonschema.py","frictionless.py"]:
        subprocess.run(["black",str(py_schema_dir.joinpath(f))])
    
    # docs
    jsonmd_url = (
      f"https://raw.githubusercontent.com/{fork}/heal-metadata-schemas/{branch}/"
      "variable-level-metadata-schema/"
      "docs/md-rendered-schemas/jsonschema-jsontemplate-data-dictionary.md"
    )
    csvmd_url = (
        f"https://raw.githubusercontent.com/{fork}/heal-metadata-schemas/{branch}/"
        "variable-level-metadata-schema/"
        "docs/md-rendered-schemas/jsonschema-csvtemplate-fields.md"
    )
    jsonmd = requests.get(jsonmd_url).text
    csvmd = requests.get(csvmd_url).text

    Path("docs/vlmd/schemas/json-data-dictionary.md").write_text(str(jsonmd))
    Path("docs/vlmd/schemas/csv-fields.md").write_text(str(csvmd))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=('Copies and formats the HEAL'
        ' vlmd fricitonless and jsonschema schemas ')
    )
    # Add arguments
    parser.add_argument('-b', '--branch', type=str,
        default="main", 
        help=('The branch name or commit hash from heal-metadata-schemas'))
    parser.add_argument('-f','--fork',
        type=str,help="Name of the fork (default is HEAL)",
        default="HEAL")
    args = parser.parse_args()
    copy_schemas(args.fork,args.branch)

    # sync data
    params = Path("configs/convert_to_vlmd.yaml").read_text()
    params = yaml.safe_load(params)

    for p in params:
        healdata_utils.convert_to_vlmd(**p)

    # sync templates
    template_params = Path("configs/write_vlmd_template.yaml").read_text()
    template_params = yaml.safe_load(template_params)

    for p in template_params:
        healdata_utils.write_vlmd_template(**p)

    # sync converted schema
    transformed_path = ("tests/criteria_data/transforms/"
        "frictionless/convert_frictionless_to_jsonschema_check1.json")


    frictionless_input_schema = healcsvschema
    jsonschema_props = healdata_utils.transforms.frictionlessconvert_frictionless_to_jsonschema(
        healdata_utils.schemas.frictionlessfrictionless_input_schema)
    Path(transformed_path).write_text(json.dumps(jsonschema_props,indent=3))

