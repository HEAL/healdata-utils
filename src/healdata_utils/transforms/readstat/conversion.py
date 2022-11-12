import pyreadstat
import pandas as pd 
from healdata_utils.transforms.readstat.mappings import fieldmap,typemap
from pathlib import Path
#TODO: add original type and translated type
# commented out are file metadata
#TODO: incorporate missing values and ranges into missingVals
#TODO: make into a class 
#TODO: change framework to not rely on pandas and only convert to dict (and then use csv to json fxn)

def read_pyreadstat(file_path,**kwargs):
    ''' 
    reads in a "metadata rich file"
    (dta, sav,b7bdat)

    '''
    file_path = Path(file_path)
    ext = file_path.suffix 
    if ext=='.sav':
        read = pyreadstat.read_sav
    #TODO: other extensions
    # elif ext=='.sas7bdat':
    #     read = pyreadstat.read_sas7bdat

    return read(file_path,**kwargs)

def get_type(meta,colname,typemap):

    for std_name,conds in typemap.items():
        is_type = sum([meta[key][colname]==val for key,val in conds])==len(list(conds))
        if is_type:
            return std_name

def is_ordered(meta,colname):
    return meta['variable_measure'][colname]=='nominal'

def to_int_if_base10(string):
    digits = string.split('.')
    if len(digits)==2:
        if digits[1]=='0' and digits[0].is_numeric():
            return digits[0]
    
    return string

def convert_readstat(file_path,fieldmap=fieldmap):
    _,meta = read_pyreadstat(file_path,metadataonly=True)
    meta = meta.__dict__ #change meta container object to dictionary so easier to map
    meta_mapped = []
    ext = Path(file_path).suffix.replace('.','')
    for colname in meta['column_names']:
        meta_field = {'name':colname}
        for new_name,map_fxn in fieldmap['pyreadstat'][ext].items():
            if new_name=='type':
                meta_param = map_fxn(meta,colname,typemap['pyreadstat'][ext])
            else:
                meta_param = map_fxn(meta,colname)
            
            if meta_param:
                meta_field[new_name] = meta_param

        if not meta_field.get('description'):
            meta_field['description'] = 'No description'
        meta_mapped.append(meta_field)
    
    return meta_mapped
