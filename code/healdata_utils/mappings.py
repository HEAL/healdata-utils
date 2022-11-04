from healdata_utils import schemas 
from healdata_utils.utils import split_and_map,split_str_array

def mapval(v,mapping):
    v = str(v)
    if v in mapping:
        return mapping[v]
    else:
        return v

typemap = {
    'text':'string',
    'float':'number',
}

formatmap = {
    'ISO8601':'' # NOTE: this is the default date format for frictionless so not necessary to specify
}

props = schemas.heal['data_dictionary']['properties']
    #mappings for array of dicts, arrays, and dicts
fieldmap = {
    'constraints.enum': lambda v: split_str_array(v),
    'cde_id': lambda v: split_and_map(v, props['cde_id']),
    'ontology_id': lambda v: split_and_map(v, props['ontology_id']),
    'encoding':lambda v: loads_dict(v),
    'format': lambda v: mapval(v,formatmap),
    'type':lambda v: mapval(v,typemap),
    #'univar_stats.cat_marginals':lambda v: split_and_map(v, prop['univar_stats']['cat_marginals']),
    'missingValues':lambda v: split_str_array(v),
    'trueValues': lambda v: split_str_array(v),
    'falseValues':lambda v: split_str_array(v),
    # TODO: add stats
}
