''' 
takes the filled out variable level metadata template
and converts to json, validates, and saves json template to file
based on an explicit set of mapping functions
''' 
import jsonschema 
import petl as etl
from pathlib import Path
from functools import reduce
import json
from frictionless import Schema

import healdata_utils.schemas as schemas
from healdata_utils.transforms.csvtemplate.mappings import fieldmap

def convert_rec_to_json(record):
    ''' 
    converts a flattened dictionary to a nested dictionary
    based on JSON path dot notation indicating nesting
    '''
    record_json = {}
    for prop_path,prop in record.items():
        if prop:
            # initiate the prop to be added with the entire
            # record 
            prop_json = record_json
            # get the inner most dictionary item of the jsonpath
            nested_names = prop_path.split('.')
            for i,prop_name in enumerate(nested_names):
                is_last_nested = i+1==len(nested_names)
                if prop_json.get(prop_name) and not is_last_nested:
                    prop_json = prop_json[prop_name]
                # if no object currently 
                elif not is_last_nested:
                    prop_json[prop_name] = {}
                    prop_json = prop_json[prop_name]
                #assign property to inner most item
                else:
                    prop_json[prop_name] = prop

    return record_json

def convert_template_csv_to_json(
    csvtemplate_path:str,
    jsontemplate_path:str,
    schema:dict=schemas.heal['data_dictionary'],
    mappings:dict=fieldmap
    ) -> dict:
    """
    Parses a csv template into a json file and validates according to the specification provided.
    """

    # loop through empty json output and assign mapping type
    # read in csv
    template_tbl = (
        etl.fromcsv(csvtemplate_path)
        .convertnumbers()
        .convert(fieldmap)
    )       
    data_dictionary = [convert_rec_to_json(rec) for rec in etl.dicts(template_tbl)]
    template_json = data_dictionary
    # TODO: use jsonschema resolver and data_dictionary.json
    # TODO: output informative error messages
    jsonschema.validate(template_json,schema={'type':'array','items':schema})

    # write to file
    template_str_json = json.dumps(template_json,indent=4)
    jsontemplate_path = Path(jsontemplate_path)
    jsontemplate_path.parent.mkdir(exist_ok=True)
    jsontemplate_path.write_text(template_str_json)

    return template_json
