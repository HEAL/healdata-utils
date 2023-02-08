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

def gather(sourcefields):
    """ 
    maps and translates fields based on redcap field type
    to heal json
    """ 
    def _add_description(sourcefield,targetfield):

        fieldlabel = sourcefield.get("label","")
        if sourcefield.get("section"):
            fieldsection = sourcefield['section']+": "
        else:
            fieldsection = ""
        
        
        return fieldsection+fieldlabel+targetfield.get("description","")

    def _add_title(sourcefield,targetfield):
        if sourcefield.get("label"):
            return sourcefield["label"]
    
    def _add_module(sourcefield,targetfield):
        if sourcefield.get("form"):
            return sourcefield["form"]

    targetfields = [{"name":field["name"]} for field in sourcefields]

    for i,sourcefield in enumerate(sourcefields):
        targetfield = targetfields[i]
        sourcefieldtype = sourcefield["type"]

        if sourcefieldtype in list(typemappings):
            mappedfield = typemappings[sourcefieldtype](sourcefield)
            mappedfieldlist = [mappedfield] if isinstance(mappedfield,dict) else mappedfield
            #NOTE if one sourcefield generates more than 1 target field (ie checkbox) need to iterate through
            for mappedfield in mappedfieldlist:
                mappedfield["description"] = _add_description(sourcefield, mappedfield)
                mappedfield["title"] = _add_title(sourcefield, mappedfield)
                mappedfield["module"] = _add_module(sourcefield, mappedfield)
                targetfield.update(mappedfield)
        else:
            targetfields.pop(i) 

    return targetfields

def convert_redcapcsv(file_path,
    data_dictionary_props={}):
    sourcefields = read(file_path)
    targetfields = gather(sourcefields)

    data_dictionary = data_dictionary_props.copy()
    data_dictionary['data_dictionary'] = targetfields

    return data_dictionary 

    
    
    