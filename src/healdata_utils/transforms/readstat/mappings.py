''' 
contains the mappings 
for a variety of input formats
'''
from pathlib import Path

# TODO: make type mappings 
def get_std_type(row):

    if row['format']=='scale' and row['type']=='double':
        type_std = 'number'
    elif row['format']=='nominal' and row['type']=='double':
        type_std = 'integer'
    else:
        type_std = 'string'
    
    row['type'] = type_std
    return row

fieldmap = {
    'pyreadstat':{
        'sav':{
            'name':'column_names',
            'type':'readstat_variable_types',
            'format':'variable_measure', #TODO: capture original_variable_type
            'description':'column_names_to_labels',
            'encodings':'variable_value_labels'
        }
    }
}