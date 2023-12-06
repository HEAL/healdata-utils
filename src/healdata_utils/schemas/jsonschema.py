healjsonschema = {
    "version": "0.1.0",
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "vlmd",
    "title": "Variable Level Metadata (Data Dictionaries)",
    "description": "This schema defines the variable level metadata for one data "
    "dictionary for a given study.Note a given study can have "
    "multiple data dictionaries",
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
                "title": "HEAL Variable " "Level Metadata " "Fields",
                "description": "Variable "
                "level "
                "metadata "
                "individual "
                "fields "
                "integrated "
                "into the "
                "variable "
                "level\n"
                "metadata "
                "object "
                "within the "
                "HEAL "
                "platform "
                "metadata "
                "service.\n"
                "\n"
                "!!! note "
                '"NOTE"\n'
                "\n"
                "  Only "
                "`name` and "
                "`description` "
                "properties "
                "are "
                "required. \n"
                "  For "
                "categorical "
                "variables, "
                "`constraints.enum` "
                "and "
                "`encodings` "
                "(where "
                "applicable) "
                "properties "
                "are highly "
                "encouraged. \n"
                "  For "
                "studies "
                "using HEAL "
                "or other "
                "common data "
                "elements "
                "(CDEs), "
                "`standardsMappings` "
                "information "
                "is highly "
                "encouraged.\n"
                "  `type` and "
                "`format` "
                "properties "
                "may be "
                "particularly "
                "useful for "
                "some "
                "variable "
                "types (e.g. "
                "date-like "
                "variables)\n",
                "type": "object",
                "additionalProperties": True,
                "required": ["name", "description"],
                "properties": {
                    "module": {
                        "type": "string",
                        "title": "Module",
                        "description": "The "
                        "section, "
                        "form, "
                        "survey "
                        "instrument, "
                        "set "
                        "of "
                        "measures  "
                        "or "
                        "other "
                        "broad "
                        "category "
                        "used \n"
                        "to "
                        "group "
                        "variables.\n",
                        "examples": [
                            "Demographics",
                            "PROMIS",
                            "Substance " "use",
                            "Medical " "History",
                            "Sleep " "questions",
                            "Physical " "activity",
                        ],
                    },
                    "name": {
                        "type": "string",
                        "title": "Variable " "Name",
                        "description": "The "
                        "name "
                        "of "
                        "a "
                        "variable "
                        "(i.e., "
                        "field) "
                        "as "
                        "it "
                        "appears "
                        "in "
                        "the "
                        "data. \n",
                    },
                    "title": {
                        "type": "string",
                        "title": "Variable " "Label " "(ie " "Title)",
                        "description": "The "
                        "human-readable "
                        "title "
                        "or "
                        "label "
                        "of "
                        "the "
                        "variable. \n",
                        "examples": ["My " "Variable", "Gender " "identity"],
                    },
                    "description": {
                        "type": "string",
                        "title": "Variable " "Description",
                        "description": "An "
                        "extended "
                        "description "
                        "of "
                        "the "
                        "variable. "
                        "This "
                        "could "
                        "be "
                        "the "
                        "definition "
                        "of "
                        "a "
                        "variable "
                        "or "
                        "the \n"
                        "question "
                        "text "
                        "(e.g., "
                        "if "
                        "a "
                        "survey). \n",
                        "examples": [
                            "The "
                            "participant's "
                            "age "
                            "at "
                            "the "
                            "time "
                            "of "
                            "study "
                            "enrollment",
                            "What "
                            "is "
                            "the "
                            "highest "
                            "grade "
                            "or "
                            "level "
                            "of "
                            "school "
                            "you "
                            "have "
                            "completed "
                            "or "
                            "the "
                            "highest "
                            "degree "
                            "you "
                            "have "
                            "received?",
                        ],
                    },
                    "type": {
                        "title": "Variable " "Type",
                        "type": "string",
                        "description": "A "
                        "classification "
                        "or "
                        "category "
                        "of "
                        "a "
                        "particular "
                        "data "
                        "element "
                        "or "
                        "property "
                        "expected "
                        "or "
                        "allowed "
                        "in "
                        "the "
                        "dataset.\n"
                        "\n"
                        "Definitions:\n"
                        "\n"
                        "-  "
                        "`number` "
                        "(A "
                        "numeric "
                        "value "
                        "with "
                        "optional "
                        "decimal "
                        "places. "
                        "(e.g., "
                        "3.14))\n"
                        "-  "
                        "`integer` "
                        "(A "
                        "whole "
                        "number "
                        "without "
                        "decimal "
                        "places. "
                        "(e.g., "
                        "42))\n"
                        "-  "
                        "`string` "
                        "(A "
                        "sequence "
                        "of "
                        "characters. "
                        "(e.g., "
                        '\\"test\\"))\n'
                        "-  "
                        "`any` "
                        "(Any "
                        "type "
                        "of "
                        "data "
                        "is "
                        "allowed. "
                        "(e.g., "
                        "true))\n"
                        "-  "
                        "`boolean` "
                        "(A "
                        "binary "
                        "value "
                        "representing "
                        "true "
                        "or "
                        "false. "
                        "(e.g., "
                        "true))\n"
                        "-  "
                        "`date` "
                        "(A "
                        "specific "
                        "calendar "
                        "date. "
                        "(e.g., "
                        '\\"2023-05-25\\"))\n'
                        "-  "
                        "`datetime` "
                        "(A "
                        "specific "
                        "date "
                        "and "
                        "time, "
                        "including "
                        "timezone "
                        "information. "
                        "(e.g., "
                        '\\"2023-05-25T10:30:00Z\\"))\n'
                        "-  "
                        "`time` "
                        "(A "
                        "specific "
                        "time "
                        "of "
                        "day. "
                        "(e.g., "
                        '\\"10:30:00\\"))\n'
                        "-  "
                        "`year` "
                        "(A "
                        "specific "
                        "year. "
                        "(e.g., "
                        "2023)\n"
                        "-  "
                        "`yearmonth` "
                        "(A "
                        "specific "
                        "year "
                        "and "
                        "month. "
                        "(e.g., "
                        '\\"2023-05\\"))\n'
                        "-  "
                        "`duration` "
                        "(A "
                        "length "
                        "of "
                        "time. "
                        "(e.g., "
                        '\\"PT1H\\")\n'
                        "-  "
                        "`geopoint` "
                        "(A "
                        "pair "
                        "of "
                        "latitude "
                        "and "
                        "longitude "
                        "coordinates. "
                        "(e.g., "
                        "[51.5074, "
                        "-0.1278]))\n",
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
                        "title": "Variable " "Format",
                        "type": "string",
                        "description": "Indicates "
                        "the "
                        "format "
                        "of "
                        "the "
                        "type "
                        "specified "
                        "in "
                        "the "
                        "`type` "
                        "property. \n"
                        "Each "
                        "format "
                        "is "
                        "dependent "
                        "on "
                        "the "
                        "`type` "
                        "specified. \n"
                        "For "
                        "example: "
                        "If "
                        "`type` "
                        "is "
                        '"string", '
                        "then "
                        "see "
                        "the "
                        "[String "
                        "formats](https://specs.frictionlessdata.io/table-schema/#string). \n"
                        "If "
                        "`type` "
                        "is "
                        '"date", '
                        '"datetime", '
                        "or "
                        '"time", '
                        "default "
                        "format "
                        "is "
                        "ISO8601 "
                        "formatting "
                        "for "
                        "those "
                        "respective "
                        "types "
                        "(see "
                        "details "
                        "on "
                        "ISO8601 "
                        "format "
                        "for "
                        "[Date](https://specs.frictionlessdata.io/table-schema/#date),\n"
                        "[Datetime](https://specs.frictionlessdata.io/table-schema/#datetime), \n"
                        "or "
                        "[Time](https://specs.frictionlessdata.io/table-schema/#time)) "
                        "- "
                        "If "
                        "you "
                        "want "
                        "to "
                        "specify "
                        "a "
                        "date-like "
                        "variable "
                        "using "
                        "standard "
                        "Python/C "
                        "strptime "
                        "syntax, "
                        "see "
                        "[here](#format-details-for-date-datetime-time-type-variables) "
                        "for "
                        "details. \n"
                        "See "
                        "[here](https://specs.frictionlessdata.io/table-schema/#types-and-formats) "
                        "for "
                        "more "
                        "information "
                        "about "
                        "appropriate "
                        "`format` "
                        "values "
                        "by "
                        "variable "
                        "`type`. \n"
                        "\n"
                        "[Additional "
                        "information]\n"
                        "\n"
                        "Date "
                        "Formats "
                        "(date, "
                        "datetime, "
                        "time "
                        "`type` "
                        "variable):\n"
                        "\n"
                        "A "
                        "format "
                        "for "
                        "a "
                        "date "
                        "variable "
                        "(`date`,`time`,`datetime`).  \n"
                        "**default**: "
                        "An "
                        "ISO8601 "
                        "format "
                        "string.\n"
                        "**any**: "
                        "Any "
                        "parsable "
                        "representation "
                        "of "
                        "a "
                        "date/time/datetime. "
                        "The "
                        "implementing "
                        "library "
                        "can "
                        "attempt "
                        "to "
                        "parse "
                        "the "
                        "datetime "
                        "via "
                        "a "
                        "range "
                        "of "
                        "strategies.\n"
                        "\n"
                        "**{PATTERN}**: "
                        "The "
                        "value "
                        "can "
                        "be "
                        "parsed "
                        "according "
                        "to "
                        "`{PATTERN}`,\n"
                        "which "
                        "`MUST` "
                        "follow "
                        "the "
                        "date "
                        "formatting "
                        "syntax "
                        "of \n"
                        "C "
                        "/ "
                        "Python "
                        "[strftime](http://strftime.org/) "
                        "such "
                        "as:\n"
                        "\n"
                        "- "
                        '"`%Y-%m-%d` '
                        "(for "
                        "date, "
                        "e.g., "
                        '2023-05-25)"\n'
                        "- "
                        '"`%Y%-%d` '
                        "(for "
                        "date, "
                        "e.g., "
                        "20230525) "
                        "for "
                        "date "
                        "without "
                        'dashes"\n'
                        "- "
                        '"`%Y-%m-%dT%H:%M:%S` '
                        "(for "
                        "datetime, "
                        "e.g., "
                        '2023-05-25T10:30:45)"\n'
                        "- "
                        '"`%Y-%m-%dT%H:%M:%SZ` '
                        "(for "
                        "datetime "
                        "with "
                        "UTC "
                        "timezone, "
                        "e.g., "
                        '2023-05-25T10:30:45Z)"\n'
                        "- "
                        '"`%Y-%m-%dT%H:%M:%S%z` '
                        "(for "
                        "datetime "
                        "with "
                        "timezone "
                        "offset, "
                        "e.g., "
                        '2023-05-25T10:30:45+0300)"\n'
                        "- "
                        '"`%Y-%m-%dT%H:%M` '
                        "(for "
                        "datetime "
                        "without "
                        "seconds, "
                        "e.g., "
                        '2023-05-25T10:30)"\n'
                        "- "
                        '"`%Y-%m-%dT%H` '
                        "(for "
                        "datetime "
                        "without "
                        "minutes "
                        "and "
                        "seconds, "
                        "e.g., "
                        '2023-05-25T10)"\n'
                        "- "
                        '"`%H:%M:%S` '
                        "(for "
                        "time, "
                        "e.g., "
                        '10:30:45)"\n'
                        "- "
                        '"`%H:%M:%SZ` '
                        "(for "
                        "time "
                        "with "
                        "UTC "
                        "timezone, "
                        "e.g., "
                        '10:30:45Z)"\n'
                        "- "
                        '"`%H:%M:%S%z` '
                        "(for "
                        "time "
                        "with "
                        "timezone "
                        "offset, "
                        "e.g., "
                        '10:30:45+0300)"\n'
                        "\n"
                        "String "
                        "formats:\n"
                        "\n"
                        "- "
                        '"`email` '
                        "if "
                        "valid "
                        "emails "
                        "(e.g., "
                        'test@gmail.com)"\n'
                        "- "
                        '"`uri` '
                        "if "
                        "valid "
                        "uri "
                        "addresses "
                        "(e.g., "
                        'https://example.com/resource123)"\n'
                        "- "
                        '"`binary` '
                        "if "
                        "a "
                        "base64 "
                        "binary "
                        "encoded "
                        "string "
                        "(e.g., "
                        "authentication "
                        "token "
                        "like "
                        'aGVsbG8gd29ybGQ=)"\n'
                        "- "
                        '"`uuid` '
                        "if "
                        "a "
                        "universal "
                        "unique "
                        "identifier "
                        "also "
                        "known "
                        "as "
                        "a "
                        "guid "
                        "(eg., "
                        'f47ac10b-58cc-4372-a567-0e02b2c3d479)"\n'
                        "\n"
                        "\n"
                        "Geopoint "
                        "formats:\n"
                        "\n"
                        "The "
                        "two "
                        "types "
                        "of "
                        "formats "
                        "for "
                        "`geopoint` "
                        "(describing "
                        "a "
                        "geographic "
                        "point).\n"
                        "\n"
                        "- "
                        "`array` "
                        "(if "
                        "'lat,long' "
                        "(e.g., "
                        "36.63,-90.20))\n"
                        "- "
                        "`object` "
                        "(if "
                        "{'lat':36.63,'lon':-90.20})\n",
                    },
                    "constraints": {
                        "type": "object",
                        "properties": {
                            "maxLength": {
                                "type": "integer",
                                "title": "Maximum " "Length",
                                "description": "Indicates "
                                "the "
                                "maximum "
                                "length "
                                "of "
                                "an "
                                "iterable "
                                "(e.g., "
                                "array, "
                                "string, "
                                "or\n"
                                "object). "
                                "For "
                                "example, "
                                "if "
                                "'Hello "
                                "World' "
                                "is "
                                "the "
                                "longest "
                                "value "
                                "of "
                                "a\n"
                                "categorical "
                                "variable, "
                                "this "
                                "would "
                                "be "
                                "a "
                                "maxLength "
                                "of "
                                "11.\n",
                            },
                            "enum": {
                                "title": "Variable " "Possible " "Values",
                                "description": "Constrains "
                                "possible "
                                "values "
                                "to "
                                "a "
                                "set "
                                "of "
                                "values.\n",
                                "type": "array",
                                "examples": [
                                    [1, 2, 3, 4],
                                    [
                                        "White",
                                        "Black " "or " "African " "American",
                                        "American " "Indian " "or " "Alaska " "Native",
                                        "Native "
                                        "Hawaiian "
                                        "or "
                                        "Other "
                                        "Pacific "
                                        "Islander",
                                        "Asian",
                                        "Some " "other " "race",
                                        "Multiracial",
                                    ],
                                ],
                            },
                            "pattern": {
                                "type": "string",
                                "title": "Regular " "Expression " "Pattern",
                                "description": "A "
                                "regular "
                                "expression "
                                "pattern "
                                "the "
                                "data "
                                "MUST "
                                "conform "
                                "to.\n",
                            },
                            "maximum": {
                                "type": "integer",
                                "title": "Maximum " "Value",
                                "description": "Specifies "
                                "the "
                                "maximum "
                                "value "
                                "of "
                                "a "
                                "field "
                                "(e.g., "
                                "maximum "
                                "-- "
                                "or "
                                "most\n"
                                "recent "
                                "-- "
                                "date, "
                                "maximum "
                                "integer "
                                "etc). "
                                "Note, "
                                "this "
                                "is "
                                "different "
                                "then\n"
                                "maxLength "
                                "property.\n",
                            },
                            "minimum": {
                                "type": "integer",
                                "title": "Minimum " "Value",
                                "description": "Specifies "
                                "the "
                                "minimum "
                                "value "
                                "of "
                                "a "
                                "field.\n",
                            },
                        },
                    },
                    "encodings": {
                        "title": "Variable "
                        "Value "
                        "Encodings "
                        "(i.e., "
                        "mappings; "
                        "value "
                        "labels)",
                        "description": "Variable "
                        "value "
                        "encodings "
                        "provide "
                        "a "
                        "way "
                        "to "
                        "further "
                        "annotate "
                        "any "
                        "value "
                        "within "
                        "a "
                        "any "
                        "variable "
                        "type,\n"
                        "making "
                        "values "
                        "easier "
                        "to "
                        "understand. \n"
                        "\n"
                        "\n"
                        "Many "
                        "analytic "
                        "software "
                        "programs "
                        "(e.g., "
                        "SPSS,Stata, "
                        "and "
                        "SAS) "
                        "use "
                        "numerical "
                        "encodings "
                        "and "
                        "some "
                        "algorithms\n"
                        "only "
                        "support "
                        "numerical "
                        "values. "
                        "Encodings "
                        "(and "
                        "mappings) "
                        "allow "
                        "categorical "
                        "values "
                        "to "
                        "be "
                        "stored "
                        "as\n"
                        "numerical "
                        "values.\n"
                        "\n"
                        "Additionally, "
                        "as "
                        "another "
                        "use "
                        "case, "
                        "this "
                        "field "
                        "provides "
                        "a "
                        "way "
                        "to\n"
                        "store "
                        "categoricals "
                        "that "
                        "are "
                        "stored "
                        "as  "
                        '"short" '
                        "labels "
                        "(such "
                        "as\n"
                        "abbreviations).\n",
                        "type": "object",
                        "examples": [
                            {"0": "No", "1": "Yes"},
                            {
                                "HW": "Hello " "world",
                                "GBW": "Good " "bye " "world",
                                "HM": "Hi, " "Mike",
                            },
                        ],
                    },
                    "ordered": {
                        "title": "An " "ordered " "variable",
                        "description": "Indicates "
                        "whether "
                        "a "
                        "categorical "
                        "variable "
                        "is "
                        "ordered. "
                        "This "
                        "variable  "
                        "is\n"
                        "relevant "
                        "for "
                        "variables "
                        "that "
                        "have "
                        "an "
                        "ordered "
                        "relationship "
                        "but "
                        "not\n"
                        "necessarily  "
                        "a "
                        "numerical "
                        "relationship "
                        "(e.g., "
                        "Strongly "
                        "disagree "
                        "< "
                        "Disagree\n"
                        "< "
                        "Neutral "
                        "< "
                        "Agree).\n",
                        "type": "boolean",
                    },
                    "missingValues": {
                        "title": "Missing " "Values",
                        "description": "A "
                        "list "
                        "of "
                        "missing "
                        "values "
                        "specific "
                        "to "
                        "a "
                        "variable.\n",
                        "examples": [
                            ["Missing", "Skipped", "No " "preference"],
                            ["Missing"],
                        ],
                        "type": "array",
                    },
                    "trueValues": {
                        "title": "Boolean " "True " "Value " "Labels",
                        "description": "For "
                        "boolean "
                        "(true) "
                        "variable "
                        "(as "
                        "defined "
                        "in "
                        "type "
                        "field), "
                        "this "
                        "field "
                        "allows\n"
                        "a "
                        "physical "
                        "string "
                        "representation "
                        "to "
                        "be "
                        "cast "
                        "as "
                        "true "
                        "(increasing\n"
                        "readability "
                        "of "
                        "the "
                        "field). "
                        "It "
                        "can "
                        "include "
                        "one "
                        "or "
                        "more "
                        "values.\n",
                        "type": "array",
                        "items": {"type": "string"},
                        "examples": [["required", "Yes", "Checked"], ["required"]],
                    },
                    "falseValues": {
                        "title": "Boolean " "False " "Value " "Labels",
                        "description": "For "
                        "boolean "
                        "(false) "
                        "variable "
                        "(as "
                        "defined "
                        "in "
                        "type "
                        "field), "
                        "this "
                        "field "
                        "allows\n"
                        "a "
                        "physical "
                        "string "
                        "representation "
                        "to "
                        "be "
                        "cast "
                        "as "
                        "false "
                        "(increasing\n"
                        "readability "
                        "of "
                        "the "
                        "field) "
                        "that "
                        "is "
                        "not "
                        "a "
                        "standard "
                        "false "
                        "value. "
                        "It "
                        "can "
                        "include "
                        "one "
                        "or "
                        "more "
                        "values.\n",
                        "type": "array",
                    },
                    "repo_link": {
                        "type": "string",
                        "title": "Variable " "Repository " "Link",
                        "description": "A "
                        "link "
                        "to "
                        "the "
                        "variable "
                        "as "
                        "it "
                        "exists "
                        "on "
                        "the "
                        "home "
                        "repository, "
                        "if "
                        "applicable\n",
                    },
                    "standardsMappings": {
                        "title": "Standards " "Mappings",
                        "description": "A "
                        "published "
                        "set "
                        "of "
                        "standard "
                        "variables "
                        "such "
                        "as "
                        "the "
                        "NIH "
                        "Common "
                        "Data "
                        "Elements "
                        "program.",
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "url": {
                                    "title": "Standards " "Mapping " "- " "Url",
                                    "description": "The "
                                    "url "
                                    "that "
                                    "links "
                                    "out "
                                    "to "
                                    "the "
                                    "published, "
                                    "standardized "
                                    "mapping.\n",
                                    "type": "string",
                                    "format": "uri",
                                    "examples": [
                                        "https://cde.nlm.nih.gov/deView?tinyId=XyuSGdTTI"
                                    ],
                                },
                                "type": {
                                    "title": "Standards " "Mapping " "- " "Title",
                                    "description": "The "
                                    "**type** "
                                    "of "
                                    "mapping "
                                    "linked "
                                    "to "
                                    "a "
                                    "published "
                                    "set "
                                    "of "
                                    "standard "
                                    "variables "
                                    "such "
                                    "as "
                                    "the "
                                    "NIH "
                                    "Common "
                                    "Data "
                                    "Elements "
                                    "program\n",
                                    "examples": ["cde", "ontology", "reference_list"],
                                    "type": "string",
                                },
                                "label": {
                                    "title": "Standards " "Mapping " "- " "Label",
                                    "description": "A "
                                    "free "
                                    "text "
                                    "**label** "
                                    "of "
                                    "a "
                                    "mapping "
                                    "indicating "
                                    "a "
                                    "mapping(s) "
                                    "to "
                                    "a "
                                    "published "
                                    "set "
                                    "of "
                                    "standard "
                                    "variables "
                                    "such "
                                    "as "
                                    "the "
                                    "NIH "
                                    "Common "
                                    "Data "
                                    "Elements "
                                    "program.\n",
                                    "type": "string",
                                    "examples": [
                                        "substance " "use",
                                        "chemical " "compound",
                                        "promis",
                                    ],
                                },
                                "source": {
                                    "title": "Standard " "Mapping " "- " "Source",
                                    "description": "The "
                                    "source "
                                    "of "
                                    "the "
                                    "standardized "
                                    "variable.\n",
                                    "type": "string",
                                    "examples": [
                                        "TBD "
                                        "(will "
                                        "have "
                                        "controlled "
                                        "vocabulary)"
                                    ],
                                },
                                "id": {
                                    "title": "Standard " "Mapping " "- " "Id",
                                    "type": "string",
                                    "description": "The "
                                    "id "
                                    "locating "
                                    "the "
                                    "individual "
                                    "mapping "
                                    "within "
                                    "the "
                                    "given "
                                    "source.\n",
                                },
                            },
                        },
                    },
                    "relatedConcepts": {
                        "title": "Related " "Concepts",
                        "description": "Mappings "
                        "to "
                        "a "
                        "published "
                        "set "
                        "of "
                        "concepts "
                        "related "
                        "to "
                        "the "
                        "given "
                        "field "
                        "such "
                        "as "
                        "ontological "
                        "information "
                        "(eg., "
                        "NCI "
                        "thesaurus, "
                        "bioportal "
                        "etc)",
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "url": {
                                    "title": "Related " "Concepts " "- " "Url",
                                    "description": "The "
                                    "url "
                                    "that "
                                    "links "
                                    "out "
                                    "to "
                                    "the "
                                    "published, "
                                    "standardized "
                                    "concept.\n",
                                    "type": "string",
                                    "format": "uri",
                                    "examples": [
                                        "https://cde.nlm.nih.gov/deView?tinyId=XyuSGdTTI"
                                    ],
                                },
                                "type": {
                                    "title": "Related " "concepts " "- " "Type",
                                    "description": "The "
                                    "**type** "
                                    "of "
                                    "mapping "
                                    "to "
                                    "a "
                                    "published "
                                    "set "
                                    "of "
                                    "concepts "
                                    "related "
                                    "to "
                                    "the "
                                    "given "
                                    "field "
                                    "such "
                                    "as \n"
                                    "ontological "
                                    "information "
                                    "(eg., "
                                    "NCI "
                                    "thesaurus, "
                                    "bioportal "
                                    "etc)\n",
                                    "type": "string",
                                },
                                "label": {
                                    "type": "string",
                                    "title": "Related " "Concepts " "- " "Label",
                                    "description": "A "
                                    "free "
                                    "text "
                                    "**label** "
                                    "of "
                                    "mapping "
                                    "to "
                                    "a "
                                    "published "
                                    "set "
                                    "of "
                                    "concepts "
                                    "related "
                                    "to "
                                    "the "
                                    "given "
                                    "field "
                                    "such "
                                    "as \n"
                                    "ontological "
                                    "information "
                                    "(eg., "
                                    "NCI "
                                    "thesaurus, "
                                    "bioportal "
                                    "etc)\n",
                                },
                                "source": {
                                    "title": "Related " "Concepts " "- " "Source",
                                    "description": "The "
                                    "source "
                                    "of "
                                    "the "
                                    "related "
                                    "concept.\n",
                                    "type": "string",
                                    "examples": [
                                        "TBD "
                                        "(will "
                                        "have "
                                        "controlled "
                                        "vocabulary)"
                                    ],
                                },
                                "id": {
                                    "title": "Related " "Concepts " "- " "Id",
                                    "type": "string",
                                    "description": "The "
                                    "id "
                                    "locating "
                                    "the "
                                    "individual "
                                    "mapping "
                                    "within "
                                    "the "
                                    "given "
                                    "source.\n",
                                },
                            },
                        },
                    },
                    "univarStats": {
                        "type": "object",
                        "description": "Univariate "
                        "statistics "
                        "inferred "
                        "from "
                        "the "
                        "data "
                        "about "
                        "the "
                        "given "
                        "variable \n",
                        "properties": {
                            "median": {"type": "number"},
                            "mean": {"type": "number"},
                            "std": {"type": "number"},
                            "min": {"type": "number"},
                            "max": {"type": "number"},
                            "mode": {"type": "number"},
                            "count": {"type": "integer", "minimum": 0},
                            "twentyFifthPercentile": {"type": "number"},
                            "seventyFifthPercentile": {"type": "number"},
                            "categoricalMarginals": {
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
}
