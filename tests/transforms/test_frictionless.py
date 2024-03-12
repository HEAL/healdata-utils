from healdata_utils.transforms.frictionless import convert_frictionless_to_jsonschema
from pathlib import Path
import yaml
import json


# %%
def test_convert_frictionless_to_jsonschema():
    frictionless_input_schema = {
        "fields": [
            {"name": "test", "type": "integer", "constraints": {"enum": [1, 2]}}
        ],
        "missingValues": ["Missing"],
    }
    jsonschema_props = convert_frictionless_to_jsonschema(frictionless_input_schema)
    test_passed = jsonschema_props == {
        "type": "array",
        "items": {
            "type": "object",
            "required": ["test"],
            "properties": {
                "test": {
                    "anyOf": [
                        {"type": "integer", "enum": [1, 2]},
                        {"enum": ["Missing"]},
                    ]
                }
            },
        },
    }

    assert (
        test_passed
    ), "Assertion statement for conversion from frictonless to jsonschema failed"
