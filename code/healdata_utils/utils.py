
# split array columns
def split_str_array(string,sep='|'):
    if string:
        return [s.strip() for s in string.split(sep)]
    else:
        return None

# if object within array, assign to properties
def map_keys_vals(keys,vals):
    ''' zips two lists of the same size as 
    a dictionary
    ''' 
    return dict(zip(keys,vals))

def split_and_map(string,prop):
    ''' 
    splits nested stringified delimited lists 
    (delimiters being | for outer and = for inner)
    and zips/maps each of the inner lists to a set
    of values (right now keys of a dictionary)
    TODO: rename function split_and_map_to_keys
    TODO: generalize to more than keys


    '''
    if string:
        keys = prop['items']['properties'].keys()
        return [
            map_keys_vals(keys,split_str_array(x,sep='=')) 
            for x in split_str_array(string,sep='|')
        ]
    else:
        return None

def loads_dict(string,item_sep='|',key_val_sep='='):
    if string:
        return dict([split_str_array(s,key_val_sep) 
            for s in split_str_array(string,item_sep)])