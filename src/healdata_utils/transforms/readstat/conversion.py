import pyreadstat
import pandas as pd 
from pathlib import Path
from healdata_utils.utils import to_int_if_base10

def read_pyreadstat(file_path,**kwargs):
    ''' 
    reads in a "metadata rich file"
    (dta, sav,b7bdat). Note, xport format not supported
    as it doesnt supply value labels.

    '''
    file_path = Path(file_path)
    ext = file_path.suffix 
    if ext=='.sav':
        read = pyreadstat.read_sav
    elif ext=='.sas7bdat':
        read = pyreadstat.read_sas7bdat
    elif ext=='.dta':
        read = pyreadstat.read_sav
    elif ext=='.por':
        read = pyreadstat.read_por

    return read(file_path,**kwargs)

def convert_readstat(file_path,
    data_dictionary_props={}):
    
    df,meta = read_pyreadstat(file_path)
    df = df.convert_dtypes()
    meta = meta.__dict__ #change meta container object to dictionary so easier to map
    fields = pd.io.json.build_table_schema(df,index=False)['fields'] #converts to frictionless Table Schema

    for field in fields:
        field.pop('extDtype',None)
        fieldname = field['name']

        value_labels = meta.get('variable_value_labels',{}).get(fieldname)
        if value_labels:
            field['encodings'] = {
                to_int_if_base10(key):to_int_if_base10(val)
                for key,val in value_labels.items()
            }
            
            #NOTE: enums are assumed if labels represent entire set of values
            # this avoids value labels that are, for example, partials such as top/bottom encodings
            enums = set(value_labels.keys())
            values = set(df[fieldname].dropna()) 
            if not values.difference(enums):
                constraints_enums = {'constraints':{'enum':[to_int_if_base10(v) for v in enums]}}
                field.update(constraints_enums)
        
        variable_label = meta.get('value_labels',{}).get(fieldname)
        if variable_label:
            field['description'] = variable_label

    data_dictionary = data_dictionary_props.copy()
    data_dictionary['data_dictionary'] = fields 

    return data_dictionary
