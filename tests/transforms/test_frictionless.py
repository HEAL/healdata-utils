from healdata_utils.transforms.frictionless import convert_frictionless_to_jsonschema
from pathlib import Path
import yaml
import json


def test_convert_frictionless_to_jsonschema():
    with Path(__file__).parent.joinpath("../data/test_frictionless_schema.yaml").open(
        mode="r"
    ) as f:
        frictionless_schema = yaml.safe_load(f)
    jsonschema_props = convert_frictionless_to_jsonschema(frictionless_schema)
    with open("tests/criteria_data/test_frictionless_check1.json", "r") as fp:
        jsonschema_props_check = json.load(fp)
    test_passed = jsonschema_props == jsonschema_props_check
    if not test_passed:
        raise Exception("line 15 assertion statement failed")