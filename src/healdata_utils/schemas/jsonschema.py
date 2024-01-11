healjsonschema = {
    "version": "0.2.0",
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "vlmd",
    "title": "Variable Level Metadata (Data Dictionaries)",
    "description": "This schema defines the variable level metadata for one data "
    "dictionary for a given study.Note a given study can have "
    "multiple data dictionaries",
    "type": "object",
    "required": ["title", "fields"],
    "properties": {
        "title": {"type": "string"},
        "description": {"type": "string"},
        "schemaVersion": {
            "type": "string",
            "description": "The version of the schema "
            "used in agreed upon "
            "convention of "
            "major.minor.path (e.g., "
            "1.0.2) \n"
            "\n"
            "NOTE: This is NOT for "
            "versioning of each "
            "indiviual data dictionary "
            "instance. \n"
            "Rather, it is the\n"
            "version of THIS schema "
            "document. See `version` "
            "property (below) if "
            "specifying the individual "
            "data dictionary instance\n"
            "version.\n"
            "\n"
            "If generating a vlmd "
            "document as a csv file, "
            "include this version in \n"
            "every row/record to "
            "indicate this is a schema "
            "level property \n"
            "(not applicable for the "
            "json version as this "
            "property is already at "
            "the schema/root level)\n",
            "pattern": "\\d+\\.\\d+\\.\\d+",
            "examples": ["1.0.0", "0.2.0"],
        },
        "version": {
            "type": "string",
            "description": "The specified individual data "
            "dictionary instance version.",
        },
        "standardsMappings": {
            "type": "array",
            "description": "A set of standardized "
            "instruments linked to "
            "all variables within "
            "the `fields` property "
            "(but see note).\n"
            "\n"
            '!!! note "NOTE"\n'
            "\n"
            "  If "
            "`standardsMappings` "
            "is present at both "
            "the root (this "
            "property) and within "
            "`fields`, \n"
            "  then the `fields` "
            "`standardsMappings` "
            "property takes "
            "precedence.\n"
            "\n"
            "  Note, only "
            "instrument can be "
            "mapped to this "
            "property as opposed "
            "to the `fields` "
            "`standardsMappings`\n"
            "  This property has "
            "the same "
            "specification as the "
            "`fields` "
            "`standardsMappings` "
            "to make the cascading "
            "logic\n"
            "  easier to "
            "understand in the "
            "same way other "
            "standards implement "
            "cascading \n"
            "  (e.g., "
            "`missingValues` in "
            "the [frictionless "
            "specification](https://specs.frictionlessdata.io/patterns/#missing-values-per-field))\n",
            "items": {
                "properties": {
                    "type": "object",
                    "instrument": {
                        "type": "object",
                        "title": "Standard " "mapping " "- " "instrument",
                        "description": "A "
                        "standardized "
                        "set "
                        "of "
                        "items "
                        "which "
                        "encompass \n"
                        "a "
                        "variable "
                        "in "
                        "this "
                        "variable "
                        "level "
                        "metadata "
                        "document "
                        "(if "
                        "at "
                        "the "
                        "root "
                        "level "
                        "or "
                        "the "
                        "document "
                        "level) \n"
                        "or "
                        "the "
                        "individual "
                        "variable "
                        "(if "
                        "at "
                        "the "
                        "field "
                        "level). \n"
                        "\n"
                        "\n"
                        "!!! "
                        "note "
                        '"NOTE"\n'
                        "\n"
                        "  "
                        "If "
                        "information "
                        "is "
                        "present "
                        "at "
                        "both "
                        "the "
                        "root "
                        "and "
                        "the "
                        "field "
                        "level, \n"
                        "  "
                        "then "
                        "the "
                        "information "
                        "at "
                        "the "
                        "field "
                        "level "
                        "would "
                        "take "
                        "precedence "
                        "(i.e., "
                        "it "
                        "would "
                        "cascade).\n",
                        "properties": {
                            "url": {
                                "title": "Url",
                                "description": "A "
                                "url "
                                "(e.g., "
                                "link, "
                                "address) "
                                "to "
                                "a "
                                "file "
                                "or "
                                "other "
                                "resource "
                                "containing "
                                "the "
                                "instrument, "
                                "or\n"
                                "a "
                                "set "
                                "of "
                                "items "
                                "which "
                                "encompass "
                                "a "
                                "variable "
                                "in "
                                "this "
                                "variable "
                                "level "
                                "metadata "
                                "document "
                                "(if "
                                "at "
                                "the "
                                "root "
                                "level "
                                "or "
                                "the "
                                "document "
                                "level) \n"
                                "or "
                                "the "
                                "individual "
                                "variable "
                                "(if "
                                "at "
                                "the "
                                "field "
                                "level). \n",
                                "type": "string",
                                "format": "uri",
                                "examples": [
                                    "https://www.heal.nih.gov/files/CDEs/2023-05/adult-demographics-cdes.xlsx"
                                ],
                            },
                            "source": {
                                "type": "string",
                                "title": "Source",
                                "description": "An "
                                "abbreviated "
                                "name/acronym "
                                "from "
                                "a "
                                "controlled "
                                "vocabulary "
                                "referencing "
                                "the "
                                "resource "
                                "(e.g., "
                                "program "
                                "or "
                                "repository)\n"
                                "containing "
                                "the "
                                "instrument, "
                                "or "
                                "a "
                                "set "
                                "of "
                                "items "
                                "which "
                                "encompass "
                                "a "
                                "variable "
                                "in "
                                "this "
                                "variable "
                                "level "
                                "metadata "
                                "document "
                                "(if "
                                "at "
                                "the "
                                "root "
                                "level "
                                "or "
                                "the "
                                "document "
                                "level) \n"
                                "or "
                                "the "
                                "individual "
                                "variable "
                                "(if "
                                "at "
                                "the "
                                "field "
                                "level). \n",
                                "enum": ["heal-cde"],
                            },
                            "title": {
                                "type": "string",
                                "title": "Title",
                                "examples": [
                                    "Adult " "demographics",
                                    "adult-demographics",
                                ],
                            },
                            "id": {
                                "type": "string",
                                "title": "Identifier",
                                "description": "A "
                                "code "
                                "or "
                                "other "
                                "string "
                                "that "
                                "identifies "
                                "the "
                                "instrument "
                                "within "
                                "the "
                                "source.\n"
                                "This "
                                "should "
                                "always "
                                "be "
                                "from "
                                "the "
                                "source's "
                                "formal, "
                                "standardized "
                                "identification "
                                "system \n",
                                "examples": ["5141"],
                            },
                        },
                    },
                }
            },
        },
        "fields": {
            "type": "array",
            "items": {
                "title": "HEAL Variable Level " "Metadata Fields",
                "description": "Variable level "
                "metadata individual "
                "fields integrated "
                "into the variable "
                "level\n"
                "metadata object "
                "within the HEAL "
                "platform metadata "
                "service.\n"
                "\n"
                '!!! note "Highly '
                'encouraged"\n'
                "\n"
                "  Only `name` and "
                "`description` "
                "properties are "
                "required. \n"
                "  For categorical "
                "variables, "
                "`constraints.enum` "
                "and `enumLabels` "
                "(where applicable) "
                "properties are highly "
                "encouraged. \n"
                "  For studies using "
                "HEAL or other common "
                "data elements (CDEs), "
                "`standardsMappings` "
                "information is highly "
                "encouraged.\n"
                "  `type` and `format` "
                "properties may be "
                "particularly useful "
                "for some variable "
                "types (e.g. date-like "
                "variables)\n",
                "type": "object",
                "required": ["name", "description"],
                "properties": {
                    "schemaVersion": {
                        "type": "string",
                        "description": "The "
                        "version "
                        "of "
                        "the "
                        "schema "
                        "used "
                        "in "
                        "agreed "
                        "upon "
                        "convention "
                        "of "
                        "major.minor.path "
                        "(e.g., "
                        "1.0.2) \n"
                        "\n"
                        "NOTE: "
                        "This "
                        "is "
                        "NOT "
                        "for "
                        "versioning "
                        "of "
                        "each "
                        "indiviual "
                        "data "
                        "dictionary "
                        "instance. \n"
                        "Rather, "
                        "it "
                        "is "
                        "the\n"
                        "version "
                        "of "
                        "THIS "
                        "schema "
                        "document. "
                        "See "
                        "`version` "
                        "property "
                        "(below) "
                        "if "
                        "specifying "
                        "the "
                        "individual "
                        "data "
                        "dictionary "
                        "instance\n"
                        "version.\n"
                        "\n"
                        "If "
                        "generating "
                        "a "
                        "vlmd "
                        "document "
                        "as "
                        "a "
                        "csv "
                        "file, "
                        "include "
                        "this "
                        "version "
                        "in \n"
                        "every "
                        "row/record "
                        "to "
                        "indicate "
                        "this "
                        "is "
                        "a "
                        "schema "
                        "level "
                        "property \n"
                        "(not "
                        "applicable "
                        "for "
                        "the "
                        "json "
                        "version "
                        "as "
                        "this "
                        "property "
                        "is "
                        "already "
                        "at "
                        "the "
                        "schema/root "
                        "level)\n",
                        "pattern": "\\d+\\.\\d+\\.\\d+",
                        "examples": ["1.0.0", "0.2.0"],
                    },
                    "section": {
                        "type": "string",
                        "title": "Section",
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
                        "variables. "
                        "Previously "
                        "called "
                        '"module."\n',
                        "examples": ["Demographics", "PROMIS", "Medical " "History"],
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
                        "examples": ["gender_id"],
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
                        "variable.\n",
                        "examples": ["Gender " "identity"],
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
                        "dataset.\n",
                        "additionalDescription": "enum "
                        "definitions:\n"
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
                        "See "
                        "[here](https://specs.frictionlessdata.io/table-schema/#types-and-formats) \n"
                        "for "
                        "more "
                        "information "
                        "about "
                        "appropriate "
                        "`format` "
                        "values "
                        "by "
                        "variable "
                        "`type`.\n",
                        "additionalDescription": "examples/definitions "
                        "of "
                        "patterns "
                        "and "
                        "possible "
                        "values:\n"
                        "\n"
                        "Examples "
                        "of "
                        "date "
                        "time "
                        "pattern "
                        "formats\n"
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
                        "Examples "
                        "of "
                        "string "
                        "formats\n"
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
                        "Examples "
                        "of "
                        "geopoint "
                        "formats\n"
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
                            "required": {
                                "type": "boolean",
                                "title": "Required " "variable",
                                "description": "If "
                                "this "
                                "variable "
                                "is "
                                "marked "
                                "as "
                                "true, "
                                "then "
                                "this "
                                "variable's "
                                "value "
                                "must "
                                "be "
                                "present\n"
                                "(ie "
                                "not "
                                "missing; "
                                "see "
                                "missingValues). "
                                "If "
                                "marked "
                                "as "
                                "false "
                                "or "
                                "not "
                                "present, "
                                "then "
                                "the \n"
                                "variable "
                                "CAN "
                                "be "
                                "missing.\n",
                            },
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
                                "type": "array",
                                "title": "Variable " "Possible " "Values",
                                "description": "Constrains "
                                "possible "
                                "values "
                                "to "
                                "a "
                                "set "
                                "of "
                                "values.\n",
                                "examples": [
                                    [1, 2, 3, 4, 5],
                                    [
                                        "Poor",
                                        "Fair",
                                        "Good",
                                        "Very " "good",
                                        "Excellent",
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
                    "enumLabels": {
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
                        "abbreviations).\n"
                        "\n"
                        "This "
                        "field "
                        "is "
                        "intended "
                        "to "
                        "follow "
                        "[this "
                        "pattern](https://specs.frictionlessdata.io/patterns/#table-schema-enum-labels-and-ordering)\n",
                        "type": "object",
                        "examples": [
                            {
                                "1": "Poor",
                                "2": "Fair",
                                "3": "Good",
                                "4": "Very " "good",
                                "5": "Excellent",
                            },
                            {
                                "HW": "Hello " "world",
                                "GBW": "Good " "bye " "world",
                                "HM": "Hi, " "Mike",
                            },
                        ],
                    },
                    "enumOrdered": {
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
                        "Agree).\n"
                        "\n"
                        "This "
                        "field "
                        "is "
                        "intended "
                        "to "
                        "follow "
                        "the "
                        "ordering "
                        "aspect "
                        "of "
                        "this "
                        "[this "
                        "pattern][this "
                        "pattern](https://specs.frictionlessdata.io/patterns/#table-schema-enum-labels-and-ordering)\n",
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
                        "examples": [["Not " "required", "NOT " "REQUIRED"], ["No"]],
                    },
                    "standardsMappings": {
                        "type": "array",
                        "description": "\n"
                        "A "
                        "set "
                        "of "
                        "instrument "
                        "and "
                        "item "
                        "references "
                        "to "
                        "standardized "
                        "data "
                        "elements "
                        "designed "
                        "to "
                        "document\n"
                        "the "
                        "[HEAL "
                        "common "
                        "data "
                        "elements "
                        "program](https://heal.nih.gov/data/common-data-elements)\n"
                        "and "
                        "other "
                        "standardized/common "
                        "element "
                        "sources "
                        "to "
                        "facilitate "
                        "cross-study "
                        "comparison "
                        "and "
                        "interoperability\n"
                        "of "
                        "data. "
                        "One "
                        "can "
                        "either "
                        "map "
                        "an "
                        "individual "
                        "data "
                        "element "
                        "or "
                        "an "
                        "instrument "
                        "in "
                        "which "
                        "the "
                        "field "
                        "is \n"
                        "a "
                        "part "
                        "of.\n"
                        "\n"
                        "__**All "
                        "Fields "
                        "Mapped "
                        "(Both "
                        "Instrument "
                        "and "
                        "Item)**__\n"
                        "\n"
                        "```json\n"
                        '"standardsMappings": '
                        "[\n"
                        "    "
                        "{\n"
                        "        "
                        '"instrument": '
                        "{\n"
                        "            "
                        '"url": '
                        '"https://www.heal.nih.gov/files/CDEs/2023-05/adult-demographics-cdes.xlsx",\n'
                        "            "
                        '"source": '
                        '"heal-cde",\n'
                        "            "
                        '"title": '
                        '"adult-demographics",\n'
                        "            "
                        '"id": '
                        '"5141"\n'
                        "        "
                        "},\n"
                        "        "
                        '"item": '
                        "{\n"
                        "            "
                        '"url": '
                        '"https://evs.nci.nih.gov/ftp1/CDISC/SDTM/SDTM%20Terminology.html#CL.C74457.RACE",\n'
                        "            "
                        '"source": '
                        '"CDISC",\n'
                        "            "
                        '"id": '
                        '"C74457"\n'
                        "        "
                        "}\n"
                        "    "
                        "}\n"
                        "]\n"
                        "```\n"
                        "\n"
                        "__**Only "
                        "Instrument "
                        "Title "
                        "of "
                        "Form "
                        "CDE "
                        "File "
                        "Mapped**__\n"
                        "\n"
                        "In "
                        "this "
                        "scenario, "
                        "especially "
                        "as "
                        "CDE "
                        "variables "
                        "do "
                        "not "
                        "have "
                        "associated "
                        "CDISC "
                        "ids "
                        "listed, "
                        "only "
                        "instrument "
                        "information "
                        "is "
                        "given.\n"
                        "\n"
                        "```json\n"
                        '"standardsMappings": '
                        "[\n"
                        "    "
                        "{\n"
                        "        "
                        '"instrument": '
                        "{\n"
                        "            "
                        '"source": '
                        '"heal-cde",\n'
                        "            "
                        '"title": '
                        '"Adult '
                        'demographics"\n'
                        "        "
                        "}\n"
                        "    "
                        "}\n"
                        "]\n"
                        "```\n"
                        "\n"
                        "__**Only "
                        "Instrument "
                        "ID "
                        "of "
                        "HEAL "
                        "CDE "
                        "Mapped**__\n"
                        "\n"
                        "```json\n"
                        '"standardsMappings": '
                        "[\n"
                        "    "
                        "{\n"
                        "        "
                        '"instrument": '
                        "{\n"
                        "            "
                        '"source": '
                        '"heal-cde",\n'
                        "            "
                        '"id": '
                        '"5141"\n'
                        "        "
                        "}\n"
                        "    "
                        "}\n"
                        "]\n"
                        "```\n"
                        "\n"
                        "__**Other "
                        "Non-HEAL "
                        "CDE "
                        "Use "
                        "Cases**__\n"
                        "\n"
                        "Only "
                        "item "
                        "matched "
                        "(for "
                        "example "
                        "if "
                        "found "
                        "in "
                        "the "
                        "NIH "
                        "(not "
                        "HEAL) "
                        "CDE "
                        "repository). "
                        "Folks "
                        "would "
                        "enter "
                        "the "
                        "information "
                        "in "
                        "the "
                        '"Identifier" '
                        "section. "
                        "Similar "
                        "to "
                        "the "
                        "above, "
                        "they "
                        "could "
                        "also "
                        "just "
                        "enter "
                        "the "
                        '"url".\n'
                        "\n"
                        "```json\n"
                        '"standardsMappings": '
                        "[\n"
                        "    "
                        "{\n"
                        "        "
                        '"item": '
                        "{\n"
                        "            "
                        '"source": '
                        '"NLM",\n'
                        "            "
                        '"id": '
                        '"Fakc6Jy2x"\n'
                        "        "
                        "}\n"
                        "    "
                        "}\n"
                        "]\n"
                        "```\n"
                        "\n"
                        "__**Multiple "
                        "CDE "
                        "Mappings**__\n"
                        "\n"
                        "Two "
                        "separate "
                        "records. "
                        "If "
                        "desired, "
                        "multiple "
                        "standard "
                        "mappings "
                        "can "
                        "be "
                        "entered, "
                        "say "
                        "from "
                        "the "
                        "NIH "
                        "HEAL "
                        "CDE "
                        "repo "
                        "and "
                        "the "
                        "NIH "
                        "CDE "
                        "lookup "
                        "(NLM) "
                        "by "
                        "way "
                        "of "
                        "two "
                        "separate "
                        "records "
                        "in "
                        "the "
                        "list.\n"
                        "\n"
                        "```json\n"
                        '"standardsMappings": '
                        "[\n"
                        "    "
                        "{\n"
                        "        "
                        '"instrument": '
                        "{\n"
                        "            "
                        '"source": '
                        '"heal-cde",\n'
                        "            "
                        '"title": '
                        '"Adult '
                        'demographics"\n'
                        "        "
                        "},\n"
                        "        "
                        '"item": '
                        "{\n"
                        "            "
                        '"source": '
                        '"CDISC",\n'
                        "            "
                        '"id": '
                        '"C74457"\n'
                        "        "
                        "},\n"
                        "    "
                        "},\n"
                        "    "
                        "{\n"
                        "        "
                        '"item": '
                        "{\n"
                        "            "
                        '"source": '
                        '"NLM",\n'
                        "            "
                        '"id": '
                        '"Fakc6Jy2x"\n'
                        "        "
                        "}\n"
                        "    "
                        "}\n"
                        "]\n"
                        "```\n",
                        "items": {
                            "type": "object",
                            "properties": {
                                "instrument": {
                                    "type": "object",
                                    "title": "Standard " "mapping " "- " "instrument",
                                    "description": "A "
                                    "standardized "
                                    "set "
                                    "of "
                                    "items "
                                    "which "
                                    "encompass \n"
                                    "a "
                                    "variable "
                                    "in "
                                    "this "
                                    "variable "
                                    "level "
                                    "metadata "
                                    "document "
                                    "(if "
                                    "at "
                                    "the "
                                    "root "
                                    "level "
                                    "or "
                                    "the "
                                    "document "
                                    "level) \n"
                                    "or "
                                    "the "
                                    "individual "
                                    "variable "
                                    "(if "
                                    "at "
                                    "the "
                                    "field "
                                    "level). \n"
                                    "\n"
                                    "\n"
                                    "!!! "
                                    "note "
                                    '"NOTE"\n'
                                    "\n"
                                    "  "
                                    "If "
                                    "information "
                                    "is "
                                    "present "
                                    "at "
                                    "both "
                                    "the "
                                    "root "
                                    "and "
                                    "the "
                                    "field "
                                    "level, \n"
                                    "  "
                                    "then "
                                    "the "
                                    "information "
                                    "at "
                                    "the "
                                    "field "
                                    "level "
                                    "would "
                                    "take "
                                    "precedence "
                                    "(i.e., "
                                    "it "
                                    "would "
                                    "cascade).\n",
                                    "properties": {
                                        "url": {
                                            "title": "Url",
                                            "description": "A "
                                            "url "
                                            "(e.g., "
                                            "link, "
                                            "address) "
                                            "to "
                                            "a "
                                            "file "
                                            "or "
                                            "other "
                                            "resource "
                                            "containing "
                                            "the "
                                            "instrument, "
                                            "or\n"
                                            "a "
                                            "set "
                                            "of "
                                            "items "
                                            "which "
                                            "encompass "
                                            "a "
                                            "variable "
                                            "in "
                                            "this "
                                            "variable "
                                            "level "
                                            "metadata "
                                            "document "
                                            "(if "
                                            "at "
                                            "the "
                                            "root "
                                            "level "
                                            "or "
                                            "the "
                                            "document "
                                            "level) \n"
                                            "or "
                                            "the "
                                            "individual "
                                            "variable "
                                            "(if "
                                            "at "
                                            "the "
                                            "field "
                                            "level). \n",
                                            "type": "string",
                                            "format": "uri",
                                            "examples": [
                                                "https://www.heal.nih.gov/files/CDEs/2023-05/adult-demographics-cdes.xlsx"
                                            ],
                                        },
                                        "source": {
                                            "type": "string",
                                            "title": "Source",
                                            "description": "An "
                                            "abbreviated "
                                            "name/acronym "
                                            "from "
                                            "a "
                                            "controlled "
                                            "vocabulary "
                                            "referencing "
                                            "the "
                                            "resource "
                                            "(e.g., "
                                            "program "
                                            "or "
                                            "repository)\n"
                                            "containing "
                                            "the "
                                            "instrument, "
                                            "or "
                                            "a "
                                            "set "
                                            "of "
                                            "items "
                                            "which "
                                            "encompass "
                                            "a "
                                            "variable "
                                            "in "
                                            "this "
                                            "variable "
                                            "level "
                                            "metadata "
                                            "document "
                                            "(if "
                                            "at "
                                            "the "
                                            "root "
                                            "level "
                                            "or "
                                            "the "
                                            "document "
                                            "level) \n"
                                            "or "
                                            "the "
                                            "individual "
                                            "variable "
                                            "(if "
                                            "at "
                                            "the "
                                            "field "
                                            "level). \n",
                                            "enum": ["heal-cde"],
                                        },
                                        "title": {
                                            "type": "string",
                                            "title": "Title",
                                            "examples": [
                                                "Adult " "demographics",
                                                "adult-demographics",
                                            ],
                                        },
                                        "id": {
                                            "type": "string",
                                            "title": "Identifier",
                                            "description": "A "
                                            "code "
                                            "or "
                                            "other "
                                            "string "
                                            "that "
                                            "identifies "
                                            "the "
                                            "instrument "
                                            "within "
                                            "the "
                                            "source.\n"
                                            "This "
                                            "should "
                                            "always "
                                            "be "
                                            "from "
                                            "the "
                                            "source's "
                                            "formal, "
                                            "standardized "
                                            "identification "
                                            "system \n",
                                            "examples": ["5141"],
                                        },
                                    },
                                },
                                "item": {
                                    "type": "object",
                                    "title": "Standard " "mapping " "- " "item",
                                    "description": "A "
                                    "standardized "
                                    "item "
                                    "(ie "
                                    "field, "
                                    "variable "
                                    "etc) "
                                    "mapped "
                                    "to "
                                    "this "
                                    "individual "
                                    "variable.\n",
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
                                            "mapping "
                                            "of "
                                            "a "
                                            "variable "
                                            "(e.g., "
                                            "common "
                                            "data "
                                            "element)\n",
                                            "type": "string",
                                            "format": "uri",
                                            "examples": [
                                                "https://evs.nci.nih.gov/ftp1/CDISC/SDTM/SDTM%20Terminology.html#CL.C74457.RACE"
                                            ],
                                        },
                                        "source": {
                                            "title": "Standard "
                                            "Mapping "
                                            "- "
                                            "Source",
                                            "description": "The "
                                            "source "
                                            "of "
                                            "the "
                                            "standardized "
                                            "variable. "
                                            "Note, "
                                            "this "
                                            "property "
                                            "is "
                                            "required "
                                            "if \n"
                                            "an "
                                            "id "
                                            "is "
                                            "specified.\n",
                                            "examples": ["CDISC"],
                                            "type": "string",
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
                                            "source. "
                                            "Note, "
                                            "the "
                                            "`standardsMapping[\\d+].source` "
                                            "property "
                                            "is "
                                            "required "
                                            "if \n"
                                            "this "
                                            "property "
                                            "is "
                                            "specified.\n",
                                            "examples": ["C74457"],
                                        },
                                    },
                                },
                            },
                        },
                    },
                    "relatedConcepts": {
                        "title": "Related " "Concepts",
                        "description": "__**[Under "
                        "development]**__ "
                        "Mappings "
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
                                    "source.",
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
