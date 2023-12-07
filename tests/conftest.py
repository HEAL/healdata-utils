import pytest 
from pathlib import Path
from healdata_utils.conversion import choice_fxn
import json

config = yaml.safe_load(Path("configs/convert_to_vlmd.yaml").read_text())

@pytest.fixture(scope="module")
def fields_propname():
    return "data_dictionary"

@pytest.fixture(scope="module")
def valid_input_params():
    outputdir = Path("tmp")
    input_params = {}
    for p in config:
        p["output_filepath"] = outputdir.joinpath("heal-dd")
        input_params[p["inputtype"]] = p

    return input_params

@pytest.fixture(scope="module")
def valid_output_json(valid_input_params): 
    output_paths = {p["inputtype"]:Path(p["output_filepath"]).with_suffix(".json") 
        for p in config}  
         
    return output_paths

@pytest.fixture(scope="module")
def valid_output_csv(valid_input_params): 
    output_paths = {p["inputtype"]:Path(p["output_filepath"]).with_suffix(".csv") 
        for p in config} 

    return output_paths


def compare_vlmd_tmp_to_output(tmpdir,csvoutput,jsonoutput,fields_propname,stemsuffix=""):
    """ compares a given csv and json output to a tmp directory
    for both csv and json (vlmd - variable level metadata)
    """
    
    ddjson = json.loads(list(tmpdir.glob(f"*{stemsuffix}.json"))[0].read_text())
    #NOTE: csv are just fields so no ddcsv

    # check for incorrect fields       
    csv_fields = list(tmpdir.glob(f"*{stemsuffix}.csv"))[0].read_text().split("\n")
    json_fields = ddjson.pop(fields_propname) #NOTE: testing individual fields

    valid_output_json_fields = jsonoutput.pop(fields_propname)
    valid_output_csv_fields = csvoutput

    invalid_json_fields = []
    invalid_csv_fields = []
    indices = range(len(json_fields))
    for i in indices:
        if json_fields[i]!=valid_output_json_fields[i]:
            invalid_json_fields.append(i)
        if csv_fields[i]!=valid_output_csv_fields[i]:
            invalid_csv_fields.append(i)
    
    json_field_names = [f["name"] for f in json_fields]
    csv_field_names = [f["name"] for f in json_fields]
    try:
        assert sorted(json_field_names)==sorted(csv_field_names),f"json fields must have the same field names as csv fields"
    except:
        assert json_field_names == csv_field_names, "json field names must be same as csv field names"
    
    assert len(invalid_json_fields)==0,f"The following **json** dd fields are not valid: {str(invalid_json_fields)}"
    assert len(invalid_csv_fields)==0,f"The following **csv** dd fields are not valid: {str(invalid_csv_fields)}"
    
    
    # check if root level properties other than the fields are valid
    for propname in ddjson:
        assert ddjson[propname] == jsonoutput[propname],f"json dd property '{propname}' assertion failed"
