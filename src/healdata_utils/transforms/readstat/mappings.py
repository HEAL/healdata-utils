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

#https://www.reed.edu/psychology/stata/gs/tutorials/types.html#:~:text=Stata%20Data%20Formats%20%26%20Changing%20Them%201%20Numbers,the%20way%20the%20date%20and%20time%20displayed.%20
typemap = {
    'pyreadstat':{
        'sav':{
            'number':{'readstat_variable_types':'double','variable_measure':'scale'},
            'integer':{'readstat_variable_types':'double','variable_measure':'nominal'},
            'string':{'readstat_variable_types':'string'}
        },
        'sas7bdat':{},

        # Taken from following resources:
        #http://wlm.userweb.mwn.de/Stata/wstatvar.htm
        #https://gitlab.com/phs-rcg/pystata-extensions/-/blob/main/src/pystata_extensions/__init__.py
        # may need to further specify other constraints based on these types or from the actual data 
        # ie for boolean values need to look at data and see what min/max is? or just use 
        # what the specs are for byte (-127 to 100)
        'dta':{
            'number':{'readstat_variable_types':'double'},
            'float':{'readstat_variable_types':'float'},
            'integer':{'readstat_variable_types':'byte'},
            'integer':{'readstat_variable_types':'long'},
            'integer':{'readstat_variable_types':'int'},
            'string':{'readstat_variable_types':'str|str#\d+'} 
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
        },
        'sas7bdat':{},
        'dta':{}
    }
}




