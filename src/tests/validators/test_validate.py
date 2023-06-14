from healdata_utils.validators.validate import validate_vlmd_csv, validate_vlmd_json


# validate_vlmd_csv
def test_validate_vlmd_csv_with_data():
    data = [
        {
            "name": "field1",
            "description": "This is a test field",
            "encodings": "1=var1|2=var2",
        },
        {"name": "field1", "type": "hello", "encodings": "1"},
    ]
    package = validate_vlmd_csv(data)
    assert package == {
        "data": [
            {
                "module": "",
                "name": "field1",
                "title": "",
                "description": "This is a test field",
                "type": "",
                "format": "",
                "constraints.maxLength": "",
                "constraints.enum": "",
                "constraints.pattern": "",
                "constraints.maximum": "",
                "encodings": "1=var1|2=var2",
                "ordered": "",
                "missingValues": "",
                "trueValues": "",
                "falseValues": "",
                "repo_link": "",
                "cde_id": "",
                "ontology_id": "",
                "univar_stats.median": "",
                "univar_stats.mean": "",
                "univar_stats.std": "",
                "univar_stats.min": "",
                "univar_stats.max": "",
                "univar_stats.mode": "",
                "univar_stats.count": "",
                "univar_stats.twenty_five_percentile": "",
                "univar_stats.seventy_five_percentile": "",
                "univar_stats.cat_marginals": "",
            },
            {
                "module": "",
                "name": "field1",
                "title": "",
                "description": "",
                "type": "hello",
                "format": "",
                "constraints.maxLength": "",
                "constraints.enum": "",
                "constraints.pattern": "",
                "constraints.maximum": "",
                "encodings": "1",
                "ordered": "",
                "missingValues": "",
                "trueValues": "",
                "falseValues": "",
                "repo_link": "",
                "cde_id": "",
                "ontology_id": "",
                "univar_stats.median": "",
                "univar_stats.mean": "",
                "univar_stats.std": "",
                "univar_stats.min": "",
                "univar_stats.max": "",
                "univar_stats.mode": "",
                "univar_stats.count": "",
                "univar_stats.twenty_five_percentile": "",
                "univar_stats.seventy_five_percentile": "",
                "univar_stats.cat_marginals": "",
            },
        ],
        "schema": {
            "type": "array",
            "items": {
                "type": "object",
                "required": [
                    "module",
                    "name",
                    "title",
                    "description",
                    "type",
                    "format",
                    "constraints.maxLength",
                    "constraints.enum",
                    "constraints.pattern",
                    "constraints.maximum",
                    "encodings",
                    "ordered",
                    "missingValues",
                    "trueValues",
                    "falseValues",
                    "repo_link",
                    "cde_id",
                    "ontology_id",
                    "univar_stats.median",
                    "univar_stats.mean",
                    "univar_stats.std",
                    "univar_stats.min",
                    "univar_stats.max",
                    "univar_stats.mode",
                    "univar_stats.count",
                    "univar_stats.twenty_five_percentile",
                    "univar_stats.seventy_five_percentile",
                    "univar_stats.cat_marginals",
                ],
                "properties": {
                    "module": {
                        "anyOf": [
                            {
                                "description": "Module (a place to put the section, form, or other broad category used \nto group variables.\n",
                                "title": "Module (i.e., section,form,category)",
                                "type": "string",
                            },
                            {"enum": [""]},
                        ]
                    },
                    "name": {
                        "description": "The name of a variable (i.e., field) as it appears in the data.\n",
                        "title": "Variable Name",
                        "type": "string",
                    },
                    "title": {
                        "anyOf": [
                            {
                                "description": "The human-readable title of the variable.",
                                "title": "Variable Label (ie Title)",
                                "type": "string",
                            },
                            {"enum": [""]},
                        ]
                    },
                    "description": {
                        "description": "An extended description of the variable.",
                        "title": "Variable Description",
                        "type": "string",
                    },
                    "type": {
                        "anyOf": [
                            {
                                "description": "A classification allowing the user (analyst, researcher or computer) to\nknow how to use the variable\n",
                                "title": "Variable Type",
                                "type": "string",
                                "enum": [
                                    "duration",
                                    "string",
                                    "geopoint",
                                    "boolean",
                                    "number",
                                    "yearmonth",
                                    "year",
                                    "datetime",
                                    "date",
                                    "time",
                                    "integer",
                                    "any",
                                ],
                            },
                            {"enum": [""]},
                        ]
                    },
                    "format": {
                        "anyOf": [
                            {
                                "description": "Indicates the format of the type specified in the `type` property. This\nmay describe the type of unit (such as for time fields like year or month)\nor the format of a date field (such as %y%m%d).\n",
                                "title": "Variable Format",
                                "type": "string",
                                "enum": [
                                    "binary",
                                    "uuid",
                                    "uri",
                                    "object",
                                    "email",
                                    "topojson",
                                    "array",
                                    "any",
                                ],
                            },
                            {"enum": [""]},
                        ]
                    },
                    "constraints.maxLength": {
                        "anyOf": [
                            {
                                "description": "Indicates the maximum length of an iterable (e.g., array, string, or\nobject). For example, if 'Hello World' is the longest value of a\ncategorical variable, this would be a maxLength of 11.\n",
                                "title": "Maximum Length",
                                "type": "integer",
                            },
                            {"enum": [""]},
                        ]
                    },
                    "constraints.enum": {
                        "anyOf": [
                            {
                                "description": "Constrains possible values to a set of values.",
                                "title": "Variable Possible Values",
                                "type": "string",
                                "pattern": "^(?:[^|]+\\||[^|]*)(?:[^|]*\\|)*[^|]*$",
                            },
                            {"enum": [""]},
                        ]
                    },
                    "constraints.pattern": {
                        "anyOf": [
                            {
                                "description": "A regular expression pattern the data MUST conform to.",
                                "title": "Regular Expression Pattern",
                                "type": "string",
                            },
                            {"enum": [""]},
                        ]
                    },
                    "constraints.maximum": {
                        "anyOf": [
                            {
                                "description": "Specifies the maximum value of a field (e.g., maximum -- or most\nrecent -- date, maximum integer etc). Note, this is different then\nmaxLength property.\n",
                                "title": "Maximum Value",
                                "type": "integer",
                            },
                            {"enum": [""]},
                        ]
                    },
                    "encodings": {
                        "anyOf": [
                            {
                                "description": 'Encodings (and mappings) allow categorical values to be stored as\nnumerical values. IMPORTANT: the ==key should be the value represented IN\nthe data== and the ==value should be the to-be-mapped label==. Many\nanalytic software programs use numerical encodings and some algorithms\nonly support numerical values. Additionally, this field provides a way to\nstore categoricals that are stored as  "short" labels (such as\nabbreviations)\n',
                                "title": "Variable Value Encodings (i.e., mappings; value labels)",
                                "type": "string",
                                "pattern": "^(?:.*?=.*?(?:\\||$))+$",
                            },
                            {"enum": [""]},
                        ]
                    },
                    "ordered": {
                        "anyOf": [
                            {
                                "description": "Indicates whether a categorical variable is ordered. This variable  is\nrelevant for variables that have an ordered relationship but not\nnecessarily  a numerical relationship (e.g., Strongly disagree < Disagree\n< Neutral < Agree).\n",
                                "title": "An ordered variable",
                                "type": "boolean",
                            },
                            {"enum": [""]},
                        ]
                    },
                    "missingValues": {
                        "anyOf": [
                            {
                                "description": "A list of missing values specific to a variable.",
                                "title": "Missing Values",
                                "type": "string",
                                "pattern": "^(?:[^|]+\\||[^|]*)(?:[^|]*\\|)*[^|]*$",
                            },
                            {"enum": [""]},
                        ]
                    },
                    "trueValues": {
                        "anyOf": [
                            {
                                "description": "For boolean (true) variable (as defined in type field), this field allows\na physical string representation to be cast as true (increasing\nreadability of the field). It can include one or more values.\n",
                                "title": "Boolean True Value Labels",
                                "type": "string",
                                "pattern": "^(?:[^|]+\\||[^|]*)(?:[^|]*\\|)*[^|]*$",
                            },
                            {"enum": [""]},
                        ]
                    },
                    "falseValues": {
                        "anyOf": [
                            {
                                "description": "For boolean (false) variable (as defined in type field), this field allows\na physical string representation to be cast as false (increasing\nreadability of the field) that is not a standard false value. It can include one or more values.\n",
                                "title": "Boolean False Value Labels",
                                "type": "string",
                                "pattern": "^(?:[^|]+\\||[^|]*)(?:[^|]*\\|)*[^|]*$",
                            },
                            {"enum": [""]},
                        ]
                    },
                    "repo_link": {
                        "anyOf": [
                            {
                                "description": "A link to the variable as it exists on the home repository, if applicable\n",
                                "title": "Variable Repository Link",
                                "type": "string",
                            },
                            {"enum": [""]},
                        ]
                    },
                    "cde_id": {
                        "anyOf": [
                            {
                                "description": "The source and id for the NIH Common Data Elements program.",
                                "title": "Common Data Element Id",
                                "type": "string",
                                "pattern": "^(?:.*?=.*?(?:\\||$))+$",
                            },
                            {"enum": [""]},
                        ]
                    },
                    "ontology_id": {
                        "anyOf": [
                            {
                                "description": "Ontological information for the given variable as indicated  by the\nsource, id, and relation to the specified classification. One or more\nontology classifications can be specified. \n",
                                "title": "Ontology ID",
                                "type": "string",
                                "pattern": "^(?:[^|=]*=){3}(?:[^|]*\\|[^|=]*=){2}[^|]*=(?:[^|]*\\|)?$",
                            },
                            {"enum": [""]},
                        ]
                    },
                    "univar_stats.median": {
                        "anyOf": [{"type": "number"}, {"enum": [""]}]
                    },
                    "univar_stats.mean": {
                        "anyOf": [{"type": "number"}, {"enum": [""]}]
                    },
                    "univar_stats.std": {"anyOf": [{"type": "number"}, {"enum": [""]}]},
                    "univar_stats.min": {"anyOf": [{"type": "number"}, {"enum": [""]}]},
                    "univar_stats.max": {"anyOf": [{"type": "number"}, {"enum": [""]}]},
                    "univar_stats.mode": {
                        "anyOf": [{"type": "number"}, {"enum": [""]}]
                    },
                    "univar_stats.count": {
                        "anyOf": [{"type": "integer"}, {"enum": [""]}]
                    },
                    "univar_stats.twenty_five_percentile": {
                        "anyOf": [{"type": "number"}, {"enum": [""]}]
                    },
                    "univar_stats.seventy_five_percentile": {
                        "anyOf": [{"type": "number"}, {"enum": [""]}]
                    },
                    "univar_stats.cat_marginals": {
                        "anyOf": [{"type": "array"}, {"enum": [""]}]
                    },
                },
                "description": "Variable level metadata individual fields integrated into the variable level\nmetadata object within the HEAL platform metadata service.\n",
                "title": "HEAL Variable Level Metadata Fields",
            },
        },
        "report": {
            "valid": False,
            "errors": [
                {
                    "row": 1,
                    "column": "type",
                    "message": "'hello' is not valid under any of the given schemas",
                },
                {
                    "row": 1,
                    "column": "encodings",
                    "message": "'1' is not valid under any of the given schemas",
                },
            ],
        },
    }


# validate_vlmd_json
def test_validate_vlmd_json_with_data():
    data = [
        {
            "name": "field1",
            "description": "This is a test field",
            "encodings": {1: "var1", 2: "var2"},
            "type": "float",
        },
        {"name": "field2", "encodings": "1"},
    ]
    package = validate_vlmd_json(data)
    assert package == {
        "data": [
            {
                "name": "field1",
                "description": "This is a test field",
                "encodings": {1: "var1", 2: "var2"},
                "type": "float",
            },
            {"name": "field2", "encodings": "1"},
        ],
        "schema": {
            "type": "object",
            "required": ["title", "data_dictionary"],
            "properties": {
                "title": {"type": "string"},
                "description": {"type": "string"},
                "data_dictionary": {
                    "type": "array",
                    "items": {
                        "$schema": "http://json-schema.org/draft-04/schema#",
                        "$id": "vlmd-fields",
                        "title": "HEAL Variable Level Metadata Fields",
                        "description": "Variable level metadata individual fields integrated into the variable level\nmetadata object within the HEAL platform metadata service.\n",
                        "type": "object",
                        "required": ["name", "description"],
                        "properties": {
                            "module": {
                                "type": "string",
                                "title": "Module (i.e., section,form,category)",
                                "description": "Module (a place to put the section, form, or other broad category used \nto group variables.\n",
                                "examples": [
                                    "Demographics",
                                    "PROMIS",
                                    "Substance use",
                                    "Medical History",
                                    "Sleep questions",
                                    "Physical activity",
                                ],
                            },
                            "name": {
                                "type": "string",
                                "title": "Variable Name",
                                "description": "The name of a variable (i.e., field) as it appears in the data.\n",
                            },
                            "title": {
                                "type": "string",
                                "title": "Variable Label (ie Title)",
                                "description": "The human-readable title of the variable.",
                            },
                            "description": {
                                "type": "string",
                                "title": "Variable Description",
                                "description": "An extended description of the variable.",
                                "examples": [
                                    "Definition",
                                    "Question text (if a survey)",
                                ],
                            },
                            "type": {
                                "title": "Variable Type",
                                "description": "A classification allowing the user (analyst, researcher or computer) to\nknow how to use the variable\n",
                                "type": "string",
                                "enum": [
                                    "number",
                                    "integer",
                                    "string",
                                    "any",
                                    "boolean",
                                    "date",
                                    "datetime",
                                    "time",
                                    "year",
                                    "yearmonth",
                                    "duration",
                                    "geopoint",
                                ],
                            },
                            "format": {
                                "title": "Variable Format",
                                "description": "Indicates the format of the type specified in the `type` property. This\nmay describe the type of unit (such as for time fields like year or month)\nor the format of a date field (such as %y%m%d).\n",
                                "type": "string",
                                "enum": [
                                    "uri",
                                    "email",
                                    "binary",
                                    "uuid",
                                    "any",
                                    "array",
                                    "object",
                                    "topojson",
                                ],
                            },
                            "constraints": {
                                "type": "object",
                                "properties": {
                                    "maxLength": {
                                        "type": "integer",
                                        "title": "Maximum Length",
                                        "description": "Indicates the maximum length of an iterable (e.g., array, string, or\nobject). For example, if 'Hello World' is the longest value of a\ncategorical variable, this would be a maxLength of 11.\n",
                                    },
                                    "enum": {
                                        "type": "array",
                                        "title": "Variable Possible Values",
                                        "description": "Constrains possible values to a set of values.",
                                    },
                                    "pattern": {
                                        "type": "string",
                                        "title": "Regular Expression Pattern",
                                        "description": "A regular expression pattern the data MUST conform to.",
                                    },
                                    "maximum": {
                                        "type": "integer",
                                        "title": "Maximum Value",
                                        "description": "Specifies the maximum value of a field (e.g., maximum -- or most\nrecent -- date, maximum integer etc). Note, this is different then\nmaxLength property.\n",
                                    },
                                },
                            },
                            "encodings": {
                                "title": "Variable Value Encodings (i.e., mappings; value labels)",
                                "description": 'Encodings (and mappings) allow categorical values to be stored as\nnumerical values. IMPORTANT: the ==key should be the value represented IN\nthe data== and the ==value should be the to-be-mapped label==. Many\nanalytic software programs use numerical encodings and some algorithms\nonly support numerical values. Additionally, this field provides a way to\nstore categoricals that are stored as  "short" labels (such as\nabbreviations)\n',
                                "type": "object",
                                "examples": [
                                    '{0:"No",1:"Yes"}',
                                    '{"HW":"Hello world","GBW":"Good bye world","HM":"Hi, Mike"}',
                                ],
                            },
                            "ordered": {
                                "title": "An ordered variable",
                                "description": "Indicates whether a categorical variable is ordered. This variable  is\nrelevant for variables that have an ordered relationship but not\nnecessarily  a numerical relationship (e.g., Strongly disagree < Disagree\n< Neutral < Agree).\n",
                                "type": "boolean",
                            },
                            "missingValues": {
                                "title": "Missing Values",
                                "description": "A list of missing values specific to a variable.",
                                "type": "array",
                            },
                            "trueValues": {
                                "title": "Boolean True Value Labels",
                                "description": "For boolean (true) variable (as defined in type field), this field allows\na physical string representation to be cast as true (increasing\nreadability of the field). It can include one or more values.\n",
                                "type": "array",
                                "items": {"type": "string"},
                                "examples": [
                                    "Required",
                                    "REQUIRED",
                                    "required",
                                    "Yes",
                                    'Checked"',
                                ],
                            },
                            "falseValues": {
                                "title": "Boolean False Value Labels",
                                "description": "For boolean (false) variable (as defined in type field), this field allows\na physical string representation to be cast as false (increasing\nreadability of the field) that is not a standard false value. It can include one or more values.\n",
                                "type": "array",
                            },
                            "repo_link": {
                                "type": "string",
                                "title": "Variable Repository Link",
                                "description": "A link to the variable as it exists on the home repository, if applicable\n",
                            },
                            "cde_id": {
                                "title": "Common Data Element Id",
                                "description": "The source and id for the NIH Common Data Elements program.",
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "source": {"type": "string"},
                                        "id": {"type": "string"},
                                    },
                                },
                            },
                            "ontology_id": {
                                "title": "Ontology ID",
                                "description": "Ontological information for the given variable as indicated  by the\nsource, id, and relation to the specified classification. One or more\nontology classifications can be specified. \n",
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "relation": {"type": "string"},
                                        "source": {"type": "string"},
                                        "id": {"type": "string"},
                                    },
                                },
                            },
                            "univar_stats": {
                                "type": "object",
                                "properties": {
                                    "median": {"type": "number"},
                                    "mean": {"type": "number"},
                                    "std": {"type": "number"},
                                    "min": {"type": "number"},
                                    "max": {"type": "number"},
                                    "mode": {"type": "number"},
                                    "count": {"type": "integer", "minimum": 0},
                                    "twenty_five_percentile": {"type": "number"},
                                    "seventy_five_percentile": {"type": "number"},
                                    "cat_marginals": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "name": {"type": "string"},
                                                "count": {"type": "integer"},
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        "report": {
            "valid": False,
            "errors": [
                {
                    "json_path": "$",
                    "message": "[{'name': 'field1', 'description': 'This is a test field', 'encodings': {1: 'var1', 2: 'var2'}, 'type': 'float'}, {'name': 'field2', 'encodings': '1'}] is not of type 'object'",
                }
            ],
        },
    }


# test_validate_vlmd_csv_with_data()
# test_validate_vlmd_json_with_data()
# print("SUCCESS")
