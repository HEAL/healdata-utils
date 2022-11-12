''' 
contains the mappings 
for a variety of input formats
'''
from pathlib import Path

def get_type(meta,colname,typemap):

    for std_name,conds in typemap.items():
        is_type = sum([meta[key][colname]==val for key,val in conds.items()])==len(list(conds))
        if is_type:
            return std_name

def is_ordered(meta,colname):
    return meta['variable_measure'].get(colname,'')=='nominal'

def to_int_if_base10(val):

    # if numeric
    if type(val)==int:
        return str(val)
    elif type(val)==float:
        if val.is_integer():
            return str(int(val))
        else:
            return str(val)

    #could be a string representation of number
    else:
        digits = str(val).split('.')
        if len(digits)==2:
            if digits[1]=='0' and digits[0].is_numeric():
                return digits[0]
        
    return str(val)

typemap = {
    'pyreadstat':{
        'sav':{
            'number':{'readstat_variable_types':'double','variable_measure':'scale'},
            'integer':{'readstat_variable_types':'double','variable_measure':'nominal'},
            'string':{'readstat_variable_types':'string'}
        }
    }
}

fieldmap = {
    'pyreadstat':{
        'sav':{
            'type': lambda meta,colname,typemap: get_type(meta,colname,typemap),
            #'format':lambda meta,colname: meta['variable_measure'][colname], #TODO: capture original_variable_type
            'description':lambda meta,colname: meta['column_names_to_labels'][colname],
            'encodings':lambda meta,colname: {
                to_int_if_base10(key):to_int_if_base10(val) 
                for key,val in meta['variable_value_labels'].get(colname,{}).items()
            },
            'ordered': lambda meta,colname: is_ordered(meta,colname)
        }
    }
}




