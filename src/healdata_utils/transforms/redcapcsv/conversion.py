""" 
convert a redcap data dictionary exported
in csv format to a heal-complieant json data dictionary

""" 

from frictionless import Resource
from . import headers,schema
from .mappings import typemappings 
#STEPS
#1 fill section headers
#2 sort rows to allow proper row indexing
#3 make conditionals for each map function

def read(file_path):
    """ 
    Reads in a path to a redcap csv file
    and outputs and dictionary with cleaned up header (field) names
    """ 
    sourcedf = (Resource(file_path)
        .to_petl()
        .todf()
        .rename(columns=headers.mapping)
        .replace({"":None})
    )
    return sourcedf.to_dict(orient="records")

def gather(redcapcsv_dictionary):
    """ 
    maps and translates fields based on redcap field type
    to heal json
    """ 
    sourcefields = sourcedf.to_dict(orient="records")
    targetfields = [{"name":field["name"]} for field in sourcefields]
    for i,sourcefield in enumerate(sourcefields):
        targetfield = targetfields[i]
        sourcefieldtype = sourcefield["type"]
        targetfield.update(typemappings[sourcefieldtype](sourcefield))

        fielddescription = ""
        if sourcefield.get("section"):
            fielddescription+=sourcefield['section']+": "
            fielddescription+=sourcefield.get("label","")
            targetfield["description"] = fielddescription+targetfield.get("description","")
        
        if sourcefield.get("label"):
            targetfield["title"] = sourcefield["label"]
    
    return targetfields

def convert_redcapcsv(file_path,
    data_dictionary_props={}):
    sourcefields = read(file_path)
    targetfields = gather(redcapcsv_dict)

    data_dictionary = data_dictionary_props.copy()
    data_dictionary['data_dictionary'] = targetfields

    return data_dictionary 

    
    
    