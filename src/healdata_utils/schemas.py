from pathlib import Path
from frictionless import Schema
import jsonschema
heal = {
    'data_dictionary': Schema(
        "https://raw.githubusercontent.com/norc-heal/heal-metadata-schemas/"
        "mbkranz/variable-lvl/variable-level-metadata-schema/schemas/fields.json"
    ).to_dict()
}

schema = heal['data_dictionary']
def validate(dd_fields):
    ''' 
    Validates the data dictionary fields property (need to add outermost (see TODOs below))

    ''' 
    # TODO: use jsonschema resolver and data_dictionary.json 
    # TODO: output informative error messages
    # TODO: add required property of title and optional of description to data_dictionary.json schema

    return jsonschema.validate(dd_fields,schema={'type':'array','items':schema})