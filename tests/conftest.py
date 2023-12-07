import pytest 
from pathlib import Path
from healdata_utils.conversion import choice_fxn
import json
import yaml

config = yaml.safe_load(Path("configs/convert_to_vlmd.yaml").read_text())

fields_propname = "data_dictionary"

outputdir = Path("tmp")
valid_input_params = {}
valid_output_json = {}
valid_output_csv = {}
for p in config:
    inputtype = p["inputtype"]
    valid_input_params[inputtype] = p.copy()
    valid_input_params[inputtype]["output_filepath"] = outputdir.joinpath("heal-dd")
    if p.get("sheet_name"):
        file_paths = [Path(p["output_filepath"]+"-"+s) for s in p["sheet_name"]]
        valid_output_json[inputtype] = [path.with_suffix(".json") for path in file_paths]
        valid_output_csv[inputtype] = [path.with_suffix(".csv") for path in file_paths]

    else:
        valid_output_json[inputtype] = Path(p["output_filepath"]).with_suffix(".json")
        valid_output_csv[inputtype] = Path(p["output_filepath"]).with_suffix(".csv")


def _compare_vlmd_tmp_to_output(filepath,csvoutput,jsonoutput,fields_propname):
    """ compares a given csv and json output to a tmp directory
    for both csv and json (vlmd - variable level metadata)

    filepath can be any suffix (json or csv or just file stem as code below explicitly replaces)
    """

    filepath = Path(filepath)
    ddjson = json.loads(filepath.with_suffix(".json").read_text())
    #NOTE: csv are just fields so no ddcsv

    # check for incorrect fields       
    csv_fields = filepath.with_suffix(".csv").read_text().split("\n")
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



def compare_vlmd_tmp_to_output(_valid_input_params):
    # currently json and csv are produced automatically
    # so should be both a csv and json file (at least 2 files)
    # more than 2 happens in cases of package-like dds formed such as with excel
    inputtype = _valid_input_params["inputtype"]

    if isinstance(valid_output_json[inputtype],(Path,str)) and isinstance(valid_output_csv[inputtype],(Path,str)):
        file_paths = [(valid_output_json[inputtype],valid_output_csv[inputtype])]
    else:
        file_paths = zip(valid_output_json[inputtype],valid_output_csv[inputtype])
    
    for i,_file_paths in enumerate(file_paths):
        jsonpath,csvpath = _file_paths
        
        _valid_output_json = json.loads(Path(jsonpath).read_text())
        _valid_output_csv = Path(csvpath).read_text().split("\n")
        
        if _valid_input_params.get("sheet_name"):
            filename = Path(_valid_input_params["output_filepath"]).name + "-" + _valid_input_params.get("sheet_name",[])[i] # need to append if excel file
            filedir = Path(_valid_input_params["output_filepath"]).parent

            filepath = filedir/filename
        else:
            filepath = Path(_valid_input_params["output_filepath"])
        _compare_vlmd_tmp_to_output(
            filepath=filepath,
            csvoutput=_valid_output_csv,
            jsonoutput=_valid_output_json,
            fields_propname=fields_propname
        )