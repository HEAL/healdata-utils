from healdata_utils.schemas.frictionless import healcsvschema
from healdata_utils.transforms.frictionless import convert_frictionless_to_jsonschema
from pathlib import Path
import yaml
import json

transformed_path = ("tests/criteria_data/transforms/"
    "frictionless/convert_frictionless_to_jsonschema_check1.json")


frictionless_input_schema = healcsvschema
jsonschema_props = convert_frictionless_to_jsonschema(frictionless_input_schema)
Path(transformed_path).write_text(json.dumps(jsonschema_props,indent=3))