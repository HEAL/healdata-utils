''' 
takes the filled out variable level metadata template
and converts to json, validates, and saves json template to file
based on an explicit set of mapping functions

goes the other way (from json to csv as well)

see convert_templatecsv_to_json and convert_json_to_templatecsv
''' 
import petl as etl
from pathlib import Path
# from frictionless import Resource,Package
from healdata_utils.io import read_delim
from healdata_utils import mappings,schemas,utils
from os import PathLike

def convert_templatecsv(
    csvtemplate: str,
    data_dictionary_props: dict,
    renamemap:dict=None,
    recodemap:dict=None,
    droplist:dict=None,
    item_sep:str="|", 
    keyval_sep:str="=",
    **kwargs
) -> dict:
    """
    [shortdesc]
    Converts a CSV conforming to HEAL specifications (but see 2 additional notes below) 
    into a HEAL-specified data dictionary in both csv format and json format.

    Converts an in-memory data dictionary or a path to a data dictionary file into a HEAL-specified tabular template by:
        1. Adding missing fields, and
        2. Converting fields from a specified mapping.
            NOTE: currently this mapping is only float/num to number or text/char to string (case insensitive)
                In future versions, there will be a specified module for csv input mappings.
    [shortdesc]
    
    Parameters
    ----------
    csvtemplate : str or path-like or an object that can be inferred as data by frictionless's Resource class.
        Data or path to data with the data being a tabular HEAL-specified data dictionary.
        This input can be any data object or path-like string excepted by a frictionless Resource object.
    data_dictionary_props : dict
        The HEAL-specified data dictionary properties.
    renamemap: A mapping of source (current) column headers to target (desired -- conforming to CVS HEAL spec)
        column headers 
    recodemap: A mapping of values for each column in HEAL spec -- {..."colname":{"oldvalue":"newvalue"...}...}
    droplist: a list of variables to drop from headers before processing
    item_sep:str (default:"|") Used to split stringified items (in objects and arrays)
    keyval_sep:str (default:"=") Used to split stringified each key-value pair

    Returns
    -------
    dict
        A dictionary with two keys:
            - 'templatejson': the HEAL-specified JSON object.
            - 'templatecsv': the HEAL-specified tabular template.

    """

    if isinstance(csvtemplate,(str,PathLike)):
        template_tbl = read_delim(str(Path(csvtemplate)))
    else:
        template_tbl = pd.DataFrame(csvtemplate)

    if not renamemap:
        renamemap = {}

    if not recodemap:
        recodemap = {}

    if not droplist:
        droplist = []

    # get transforms
    # cast numbers explicitly based on schema
    # this is needed in case there is only one record in a string column that is a number (ie don't want to convert)
    fields = utils.flatten_properties(schemas.healjsonschema["properties"]["fields"]["items"]["properties"])
    castnumbers = {}
    parse_dicts_and_lists = {}
    for fieldname,field in fields.items(): 
        if field["type"] == "integer":
            castnumbers[fieldname] = lambda v:int(v[fieldname]) 
        elif field["type"] == "number":
            castnumbers[fieldname] = lambda v:float(v[fieldname])
        elif field["type"] == "object":
            fxn = lambda v: utils.parse_dictionary_str(v[fieldname],item_sep,keyval_sep)
            parse_dicts_and_lists[fieldname] = fxn
        elif field["type"] == "array":
            parse_dicts_and_lists[fieldname] = lambda v: utils.parse_list_str(v[fieldname],item_sep)

    tbl_csv = (
        template_tbl
        .rename(columns=renamemap)
        .replace(recodemap)
        .drop(columns=droplist,errors="ignore")
        .assign(**castnumbers)
        .assign(**parse_dicts_and_lists)
    )

    fields_json = []
    for record in tbl_csv.to_dict(orient="records"):
        jsonrecord = utils.unflatten_jsonpath(record,schemas.healjsonschema)        
        fields_json.append(jsonrecord)

    template_json = dict(**data_dictionary_props,fields=fields_json)
    template_csv = dict(**data_dictionary_props,fields=fields_csv)

    return {"templatejson":template_json,"templatecsv":template_csv}