""" 
holds the mappings for previous schema version
field names (headers, properties) and the current name
in addition to these field name values or value mappings.

""" 
from healdata_utils.schema import healjsonschema

def _flatten(map):
    return {
        sourcename:item["target"] 
        for item in map
        for sourcename in item["source"]
    }

VERSION = ["0","2"]

root_mappings = [
    {
        "target":"fields",
        "source":["data_dictionary"]
    },
    {
        "target":"schemaVersion",
        "source":None,
        "value":healjsonschema["version"]
    }
]


field_mappings = [
    {
        "target":"schemaVersion",
        "source":None,
        # should be same as csv schema version 
        "value":healcsvschema["version"] 
    },
    {
        "target":"section",
        "source":["module"]
    },
    {
        "target":"enumLabels",
        "source":["encoding","encodings"]
    },
    {
        "target":"enumOrdered",
        "source":["ordered"]
    },
    {
        "target":"standardsMappings[0].instrument.target",
        "source":["standardsMappings.type","standardsMappings[0].target"]
    },
    {
        "target":"standardsMappings[0].instrument.title",
        "source":["standardsMappings.label","standardsMappings[0].title"]
    },
    {
        "target":"standardsMappings[0].item.target",
        "source":["standardsMappings.target","standardsMappings[0].target"]
    },
    {
        "target":"standardsMappings[0].item.id",
        "source":["standardsMappings.id","standardsMappings[0].id"]
    },
    {
        "target":"standardsMappings[0].item.url",
        "source":["standardsMappings.url","standardsMappings[0].url"]
    },
    {
        "target":None,
        "source":["repo_link"]
    }
]


root_renamemap = {
    sourcenames:item["target"] 
    for item in root_mappings 
    for sourcenames in item["source"] if item["target"]
}
root_addmap = {"schemaVersion":healjsonschema["version"]}
fields_renamemap = {
    sourcenames:item["target"] 
    for item in field_renamemap 
    for sourcenames in item["source"] if item["target"]
}
fields_droplist = [
    sourcename
    for item in field_mappings
    for sourcename in field_mappings["source"]
    if not item["target"]
]
fields_addmap = {"schemaVersion":healjsonschema["version"]}