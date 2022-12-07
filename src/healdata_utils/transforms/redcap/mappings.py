renamemap = {
    'form':'module',
    'data_type': 'type', 
    'question': 'description',
    'name': 'name',
    #'constraints.required': lambda v: to_bool(v),
    #'constraints.enum': Get CodeListItem.CodedValue
    #'constraints.maximum':'',
    #'constraints.minimum':'', 
    #'constraints.maxLength':'',
    #'cde_id':'',
    #'ontology_id': '',
    #TODO: "CodeListItem" in dataforge RedCap schema (and format to dict with @CodedValue:Decode.TranslatedText (or redcap:FormattedTranslatedText)
    #'encoding': see TODO above
    #'format': '',
    #'univar_stats.cat_marginals':'',
    #'missingValues':lambda v: split_str_array(v),
    #'trueValues': if data_type==boolean then get text for 1 ,
    #'falseValues': if data_type==boolean then get text for 0,
}   

recodemap = {
    'type':{
        'float':'number',
        'partialDateTime':'date',
        'text':'string',
    }
}