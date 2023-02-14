from pathlib import Path
from frictionless import Schema
import jsonschema

# TODO: use data_dictionary.json 
# TODO: output informative error messages in validation
# NOTE: would it be good to also have a frictionless CSV template with regexs?...may be easier to spot text errors?

heal = {
    'data_dictionary': Schema(
        "https://raw.githubusercontent.com/norc-heal/heal-metadata-schemas/"
        "mbkranz/variable-lvl/variable-level-metadata-schema/schemas/fields.json"
    ).to_dict()
}

schema = {
    'type':'object',
    'required':[
        'title',
        'data_dictionary'
    ],
    'properties':{
        'title':{'type':'string'},
        'description':{'type':'string'},
        'data_dictionary':{'type':'array','items':heal['data_dictionary']}
    }
}

def validate_json(data_dictionary,schema=schema):
    ''' 
    Validates the data dictionary fields property (need to add outermost (see TODOs below))

    ''' 

    jsonschema.validate(data_dictionary,schema=schema)