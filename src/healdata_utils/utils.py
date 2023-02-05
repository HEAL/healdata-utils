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


def parse_encodings():
    # NOTE: need to consider multiple delimiters 
    # (eg if comma delimtier and in value label, only select first one)
    pass 
