''' General utilities/helper functions'''
def to_int_if_base10(val):
    """ 
    converts value to a string and if 
    float (or a string rep of a float) of base10 
    to an integer string representation.

    NOTE: 
    """ 
    string = str(val)

    if string.isnumeric():
        digits = string.split('.')
        if len(digits)==2:
            if digits[1]=='0':
                return digits[0]
    else:
        return string


def parse_dictionary_str(string,item_sep,keyval_sep):
    """ 
    parses a stringified dictionary into a dictionary
    based on item separator 

    """
    stritems = string.strip().split(item_sep)
    items = {}
    for stritem in stritems:
        item = stritem.split(keyval_sep,1)
        items[item[0]] = items[item[1]]
    
    return items 


def parse_list_str(string,list_sep):
    return string.strip().split(list_sep)

