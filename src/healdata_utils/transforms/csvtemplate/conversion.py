''' 
takes the filled out variable level metadata template
and converts to json, validates, and saves json template to file
based on an explicit set of mapping functions

goes the other way (from json to csv as well)

see convert_templatecsv_to_json and convert_json_to_templatecsv
''' 
import jsonschema 
import petl as etl
from pathlib import Path
from functools import reduce
import json
from frictionless import Schema,Resource
from collections.abc import Iterable,MutableMapping
import healdata_utils.schemas as schemas
from healdata_utils.utils import flatten_except_if,convert_rec_to_json
from healdata_utils.transforms.csvtemplate.mappings import fieldmap,join_prop




def convert_template_csv_to_json(
    csvtemplate_path:str,
    data_dictionary_props:dict,
    mappings:dict=fieldmap,
    
    ) -> dict:
    """
    Parses a csv template into a json file and validates according to the specification provided.
    """

    # loop through empty json output and assign mapping type
    # read in csv
    source = Resource(csvtemplate_path).to_petl()
    fields_to_add = [
        (field,'') 
        for field in mappings.keys() 
        if not field in source.fieldnames()
    ]
    template_tbl = (
        source
        .addfields(fields_to_add) # add fields from mappings not in the csv template to allow convert fxns to work
        .convert(fieldmap)
        .convertnumbers()
        .cut(source.fieldnames()) #want to include only fields in csv
    )       
    data_dictionary = data_dictionary_props.copy()
    data_dictionary['data_dictionary'] = [convert_rec_to_json(rec) for rec in etl.dicts(template_tbl)]

    return data_dictionary




def convert_json_to_template_csv(
    jsontemplate_path:str,
    fields_name:str='data_dictionary',
    sep_iter = '|',
    sep_dict = '=',
    **kwargs
    ) -> list:

    with open(jsontemplate_path,'r',encoding='utf-8') as f:
        data_dictionary = json.load(f)

    fields = list(data_dictionary[fields_name])
    fields_csv = []
    #colnames = set()
    for f in fields:
        field_flattened = flatten_except_if(f)
        field_csv = {
            propname:join_prop(propname,prop)
            for propname,prop in field_flattened.items()
        }
        fields_csv.append(field_csv)
        #colnames.update(list(fields))

    return Resource(data=fields_csv)