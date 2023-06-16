from healdata_utils.validators.validate import validate_vlmd_csv, validate_vlmd_json
import json
import os

print(os.getcwd())
# validate_vlmd_csv
def test_validate_vlmd_csv_with_data():
    data = [
        {
            "name": "field1",
            "description": "This is a test field",
            "encodings": "1=var1|2=var2",
        },
        {"name": "field1", "type": "hello", "encodings": "1"},
    ]
    package = validate_vlmd_csv(data)
    with open("tests\\criteria_data\\test_validate_check1.json", 'r') as fp:
        package_check = json.load(fp)
    assert package == package_check


# validate_vlmd_json
def test_validate_vlmd_json_with_data():
    data = [
        {
            "name": "field1",
            "description": "This is a test field",
            "encodings": {1: "var1", 2: "var2"},
            "type": "float",
        },
        {"name": "field2", "encodings": "1"},
    ]
    package = validate_vlmd_json(data)
    with open("tests\\criteria_data\\test_validate_check2.json", 'r') as fp:
        package_check = json.load(fp)
    assert package == package_check

