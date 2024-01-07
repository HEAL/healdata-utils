from healdata_utils.schema import healjsonschema

root_namemap = [
    {
        "current":"fields",
        "former":["data_dictionary"]
    },
    {
        "current":"schemaVersion",
        "former":None,
        "values":healjsonschema["version"]
    }
]


field_namemap = [
    {
        "current":"section",
        "former":["module"]
    },
    {
        "current":"enumLabels",
        "former":["encoding","encodings"],

    },
    {
        "current":"enumOrdered",
        "former":["ordered"]
    },
    {
        "current":"standardsMappings[\d+].instrument.source",
        "former":["standardsMappings.type"]
    },
    {+
        "current":"standardsMappings[\d+].instrument.title",
        "former":["standardsMappings.label"]
    },
    {
        "current":"standardsMappings[\d+].item.source",
        "former":["standardsMappings.source"]
    },
    {
        "current":"standardsMappings[\d+].item.id",
        "former":["standardsMappings.id"]
    },
    {
        "current":"standardsMappings[\d+].item.url",
        "former":["standardsMappings.url"]
    }
]
