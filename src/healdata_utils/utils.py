""" General utilities/helper functions"""
import re
from collections.abc import MutableMapping


# individual cell utilities
def strip_html(html_string):
    if html_string:
        return re.sub(r"<[^>]+>", "", html_string)
    else:
        return html_string


def to_int_if_base10(val):
    """
    converts value to a string and if
    float (or a string rep of a float) of base10
    to an integer string representation.

    NOTE:
    """
    string = str(val)

    if "." in string:
        parts = string.split(".")
        if len(parts) == 2 and parts[1] == "0":
            return parts[0]

    return string


def parse_dictionary_str(string, item_sep, keyval_sep):
    """
    parses a stringified dictionary into a dictionary
    based on item separator

    """
    if string != "" and string != None:
        stritems = string.strip().split(item_sep)
        items = {}

        for stritem in stritems:
            if stritem:
                item = stritem.split(keyval_sep, 1)
                items[item[0].strip()] = item[1].strip()
        
        return items
    else:
        return string


def parse_list_str(string, item_sep):
    if string != "" and string != None:
        return string.strip().split(item_sep)
    else:
        return string


# dictionary utilities
def flatten_to_jsonpath(dictionary,schema,parent_key=False, sep="."):
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
    # flatten if type array -> type object with properties
    # flatten if type object with properties
    items = []
    for key, value in dictionary.items():
        new_key = str(parent_key) + sep + key if parent_key else key
        prop = schema["properties"][key]
        childprops = prop.get("properties")
        childitem_props = prop.get("items",{}).get("properties")

        if childprops:
            item = flatten_to_jsonpath(
                dictionary=_value, 
                schema=prop,
                parent_key=new_key, 
                sep=sep)
            items.extend(item.items())
        elif childitem_props:
            for i,_value in enumerate(value):
                item = flatten_to_jsonpath(
                    dictionary=_value, 
                    schema=prop,
                    parent_key=new_key, 
                    sep=f"[{str(i)}]{sep}")
                items.extend(item.items())

        else:
            items.append((new_key, value))

    return dict(items)

def stringify_keys(dictionary):
    orig_keys = list(dictionary.keys())
    for key in orig_keys:
        dictionary[str(key)] = dictionary.pop(key)

def unflatten_jsonpath(field):
    """
    Converts a flattened dictionary with key names conforming to 
    JSONpath notation to the nested dictionary format.
    """
    field_json = {}

    for prop_path, prop in field.items():
        prop_json = field_json

        # if isinstance(prop,list):
        #     prop = [v for val in prop if if val != None or val != ""]
        # elif isinstance(prop,dict):
        #     # filter falsey  values of "" and None
        #     prop = {key:val for key,val in prop.items() if val != None or val != ""}


        if prop:
            # Get the necessary info from the JSON path 
            nested_names = [re.sub("\[\d+\]$", "", prop_name) for prop_name in prop_path.split(".")]
            nested_indices = [re.findall("\[(\d+)\]$", prop_name)[-1] if re.search("\[(\d+)\]$", prop_name) else None for prop_name in prop_path.split(".")]

            for prop_name, array_index in zip(nested_names, nested_indices):
                is_last_nested = prop_name == nested_names[-1]

                if array_index is not None:
                    # Handle array properties
                    if prop_name not in prop_json:
                        prop_json[prop_name] = [None] * (int(array_index) + 1)

                    if is_last_nested:
                        if prop_json[prop_name][int(array_index)] is None:
                            prop_json[prop_name][int(array_index)] = {}
                        
                        if isinstance(prop_json[prop_name][int(array_index)], dict):
                            prop_json[prop_name][int(array_index)].update({prop_name: prop})
                        else:
                            prop_json[prop_name][int(array_index)] = {prop_name: prop}
                    else:
                        if prop_json[prop_name][int(array_index)] is None:
                            prop_json[prop_name][int(array_index)] = {}
                        
                        prop_json = prop_json[prop_name][int(array_index)]
                else:
                    # Handle non-array properties
                    if is_last_nested:
                        if prop_name not in prop_json:
                            prop_json[prop_name] = prop
                        else:
                            if isinstance(prop_json[prop_name], dict):
                                prop_json[prop_name].update({prop_name: prop})
                            else:
                                prop_json[prop_name] = {prop_name: prop}
                    else:
                        if prop_name not in prop_json:
                            prop_json[prop_name] = {}
                        
                        prop_json = prop_json[prop_name]

    return field_json

# json to csv utils
def join_iter(iterable,sep_list="|"):
    return sep_list.join([str(p) for p in iterable])

def join_dictvals(dictionary:dict,sep:str):
    return sep.join(dictionary.values())

def join_dictitems(dictionary:dict,sep_keyval='=',sep_items='|'):
    """ joins a mappable collection (ie dictionary) into a string
    representation with specified separators for the key and value
    in addition to items. 

    All items are coerced to the string representation (eg if key or value
    is None, this will be coerced to "None")


    """
    dict_list = []
    for key,val in dictionary.items():
        keystr = str(key)
        valstr = str(val)
        dict_list.append(keystr+sep_keyval+valstr)
    return sep_items.join(dict_list)


# documentation building utilities
def find_docstring_desc(fxn):
    """
    return the description part of a docstring
    (ie text before Parameters)
    """
    exp = "^(.*)Parameters\\n"

    if fxn.__doc__:
        docstring = fxn.__doc__.strip()
    else:
        docstring = "No documentation"
    try:
        return re.search(exp, docstring, re.DOTALL).group(1)
    except AttributeError:
        return docstring


# add missing values and order according to the order of a list


def sync_fields(data, field_list,missing_value=None):
    """
    Sorts fields and adds missing fields (with None value).
    If extra fields exist in a record that are not in field_list, then tacks on at 
    end of record.


    Parameters
    --------------
    data [list]: json array of values
    fields [list]: the list of all fields (e.g., from a schema)

    Returns
    -------------
    list: json array with fields added if missing
    """
    data_with_missing = []

    for record in data:
        extra_fields = list(set(list(record)).difference(field_list))
        new_record = {field:record.get(field, missing_value) 
            for field in field_list+extra_fields}
        data_with_missing.append(new_record)

    
    return data_with_missing


# %% 
# Working with schemas
def flatten_properties(properties, parentkey="", sep=".",itemsep="[0]"):
    """
    flatten schema properties
    """
    properties_flattened = {}
    for key, item in properties.items():
        # flattened keys
        if parentkey:
            flattenedkey = parentkey + "." + key
        else:
            flattenedkey = key

        if isinstance(item, MutableMapping):
            props = item.get("properties")
            items = item.get("items",{}).get("properties")
            if props:
                newprops = flatten_properties(props, parentkey=flattenedkey)
                properties_flattened.update(newprops)

            elif items:
                newprops = flatten_properties(items,parentkey=flattenedkey+itemsep)
                properties_flattened.update(newprops)
            else:
                properties_flattened[flattenedkey] = item
        
        else:
            properties_flattened[flattenedkey] = item
    
    return properties_flattened

def flatten_schema(schema):
    schema_flattened = dict(schema)
    properties = schema.get("properties")
    if properties:
        schema_flattened["properties"] = flatten_properties(properties)
    return schema_flattened