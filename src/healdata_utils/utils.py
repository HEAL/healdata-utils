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
    stritems = string.strip().split(item_sep)
    items = {}
    for stritem in stritems:
        item = stritem.split(keyval_sep, 1)
        items[item[0]] = item[1].strip()

    return items


def parse_list_str(string, list_sep):
    return string.strip().split(list_sep)


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

def convert_rec_to_json(field):
    """
    converts a flattened dictionary with key names conforming to 
    JSONpath notation to the nested dictionary format
    """
    field_json = {}
    for prop_path, prop in field.items():
        prop_json = field_json
        if prop:
            # get the necessary info from the json path 
            # (property name, any list indices,a property depth level index) 
            nested_names = [re.sub("\[\d+\]$","",prop_name) 
                for prop_name in prop_path.split(".")]
            nested_indices = [
                re.findall("\[(\d+)\]$",prop_name)[-1] if re.search("\[(\d+)\]$",prop_name)
                else None
                for prop_name in prop_path.split(".")
            ]
            parent_indices = [None] + nested_indices[:-1] # No parent index for first level


            # create the nested json structure
            for parent_index,prop_name,current_index in zip(parent_indices,nested_names,nested_indices):
                is_last_nested = prop_name == nested_names[-1]
                parent_is_array = not parent_index is None
                parent_is_dict = not parent_is_array

                current_is_array = not current_index is None
                current_is_dict = not current_is_array


                if current_is_array:
                    if not prop_name in prop_json:
                        prop_json[prop_name] = [None]*(int(current_index) +1)
                    else:
                        if int(current_index) +1 > len(prop_json[prop_name]):
                            len_extend = len(prop_json[prop_name]) - int(current_index) + 1
                            prop_json[prop_name].extend([None]*len_extend)
                    if is_last_nested:
                        prop_json[prop_name][current_index] = prop
                    else:
                        prop_json = prop_json[prop_name]
                else:
                    if not prop_name in prop_json:
                        prop_json[prop_name] = {}
                    
                    if parent_is_array:
                        if is_last_nested:
                            prop_json[prop_name][parent_index] = prop
                        else:
                            prop_json = prop_json[parent_index][prop_name]
                    else:
                        if is_last_nested:
                            prop_json[prop_name] = prop
                        else:
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



