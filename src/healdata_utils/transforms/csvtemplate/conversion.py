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
from healdata_utils.transforms.csvtemplate.mappings import fieldmap,join_prop


def convert_rec_to_json(field):
    ''' 
    converts a flattened dictionary to a nested dictionary
    based on JSON path dot notation indicating nesting
    '''
    field_json = {}
    for prop_path,prop in field.items():
        if prop:
            # initiate the prop to be added with the entire
            # field 
            prop_json = field_json
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

    return field_json

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
    source = etl.fromcsv(csvtemplate_path,encoding='utf-8')
    fields_to_add = [
        (field,'') 
        for field in mappings.keys() 
        if not field in source.fieldnames()
    ]
    template_tbl = (
        source
        .addfields(fields_to_add) # add fields from mappings not in the csv template to allow convert fxns to work
        .convert(fieldmap)
        .cut(source.fieldnames()) #want to include only fields in csv
    )       
    data_dictionary = data_dictionary_props.copy()
    data_dictionary['data_dictionary'] = [convert_rec_to_json(rec) for rec in etl.dicts(template_tbl)]

    return data_dictionary

def flatten_except_if(dictionary, parent_key=False, sep=".",except_keys=['encodings']):
    """
    Turn a nested dictionary into a flattened dictionary. Taken from gen3 
    mds.agg_mds.adapter.flatten
    but added except keys and fixed a bug where parent is always False in MutableMapping

    :param dictionary: The dictionary to flatten
    :param parent_key: The string to prepend to dictionary's keys
    :param sep: The string used to separate flattened keys
    :param except_keys: keys to not flatten. Note, can be nested if using notation specified in sep
    :return: A flattened dictionary
    """

    items = []
    for key, value in dictionary.items():
        new_key = str(parent_key) + sep + key if parent_key else key
        if isinstance(value,MutableMapping) and not new_key in except_keys:
            items.extend(flatten_except_if(value, new_key, sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


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