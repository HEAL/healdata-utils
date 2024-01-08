''' 
contains mappings (both lambda functions or column mappings)
''' 

from healdata_utils import schemas
from healdata_utils import mappings
# split array columns
def split_str_array(string,sep='|'):
    if string:
        return [s.strip() for s in string.split(sep)]
    else:
        return string

def loads_dict(string,item_sep='|',key_val_sep='='):
    if string:
        return dict([split_str_array(s,key_val_sep) 
            for s in split_str_array(string,item_sep)])
    else:
        return string


# cast numbers explicitly based on schema
# this is needed in case there is only one record in a string column that is a number (ie don't want to convert)
castnumbers = {
    field["name"]:int if field["type"]=="integer" else float
    for field in schemas.healcsvschema["fields"]
    if field.get("type","") in ["integer","number"]
}