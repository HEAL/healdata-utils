""" 
validation of json records against a jsonschema specification 
and conversion of one schema spec to jsonschema specification 
eg frictionless --> jsonschema

""" 

import jsonschema

def validate_against_jsonschema(json_object,schema):
    
    Validator = jsonschema.validators.validator_for(schema)
    validator = Validator(schema)
    report = []
    is_valid = True
    for error in validator.iter_errors(json_object):
        is_valid = False
        error_report = {
            "json_path":error.get("json_path", ""),
            "message":error.get("message", ""),
            "absolute_path":list(error.get("path", [])),
            "relative_path":list(error.get("relative_path", [])),
            "validator":error.get("validator", ""),
            "validator_value":error.get("validator_value", "")
        }
        report.append(error_report)

    return {"valid":is_valid,"errors":report}