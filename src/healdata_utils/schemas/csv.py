healcsvschema = {
    "version": "0.3.2",
    "title": "HEAL Variable Level Metadata Fields",
    "description": "\n"
    "\n"
    '!!! note "Highly encouraged"\n'
    "\n"
    "  - Only `name` and `description` properties are required. \n"
    "  - For categorical variables, `constraints.enum` and "
    "`enumLabels` (where applicable) properties are highly "
    "encouraged. \n"
    "  - For studies using HEAL or other common data elements "
    "(CDEs), `standardsMappings` information is highly "
    "encouraged.\n"
    "  - `type` and `format` properties may be particularly "
    "useful for some variable types (e.g. date-like variables)\n",
    "type": "object",
    "required": ["name", "description"],
    "additionalProperties": False,
    "properties": {
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
        "section": {
            "type": "string",
            "title": "Section",
            "description": "The section, form, survey "
            "instrument, set of measures  or "
            "other broad category used \n"
            "to group variables. Previously "
            'called "module."\n',
            "examples": ["Demographics", "PROMIS", "Medical History"],
        },
        "name": {
            "type": "string",
            "title": "Variable Name",
            "description": "The name of a variable (i.e., "
            "field) as it appears in the "
            "data. \n",
            "examples": ["gender_id"],
        },
        "title": {
            "type": "string",
            "title": "Variable Label (ie Title)",
            "description": "The human-readable title or label " "of the variable.\n",
            "examples": ["Gender identity"],
        },
        "description": {
            "type": "string",
            "title": "Variable Description",
            "description": "An extended description of "
            "the variable. This could be "
            "the definition of a "
            "variable or the \n"
            "question text (e.g., if a "
            "survey). \n",
            "examples": [
                "The participant's age at the " "time of study enrollment",
                "What is the highest grade or "
                "level of school you have "
                "completed or the highest "
                "degree you have received?",
            ],
        },
        "type": {
            "title": "Variable Type",
            "type": "string",
            "description": "A classification or category of a "
            "particular data element or "
            "property expected or allowed in "
            "the dataset.\n",
            "additionalDescription": "enum definitions:\n"
            "\n"
            "-  `number` (A numeric "
            "value with optional "
            "decimal places. (e.g., "
            "3.14))\n"
            "-  `integer` (A whole "
            "number without decimal "
            "places. (e.g., 42))\n"
            "-  `string` (A sequence "
            "of characters. (e.g., "
            '\\"test\\"))\n'
            "-  `any` (Any type of "
            "data is allowed. (e.g., "
            "true))\n"
            "-  `boolean` (A binary "
            "value representing true "
            "or false. (e.g., true))\n"
            "-  `date` (A specific "
            "calendar date. (e.g., "
            '\\"2023-05-25\\"))\n'
            "-  `datetime` (A "
            "specific date and time, "
            "including timezone "
            "information. (e.g., "
            '\\"2023-05-25T10:30:00Z\\"))\n'
            "-  `time` (A specific "
            "time of day. (e.g., "
            '\\"10:30:00\\"))\n'
            "-  `year` (A specific "
            "year. (e.g., 2023)\n"
            "-  `yearmonth` (A "
            "specific year and month. "
            '(e.g., \\"2023-05\\"))\n'
            "-  `duration` (A length "
            "of time. (e.g., "
            '\\"PT1H\\")\n'
            "-  `geopoint` (A pair of "
            "latitude and longitude "
            "coordinates. (e.g., "
            "[51.5074, -0.1278]))\n",
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
            "type": "string",
            "description": "Indicates the format of the type "
            "specified in the `type` "
            "property. \n"
            "Each format is dependent on the "
            "`type` specified. \n"
            "See "
            "[here](https://specs.frictionlessdata.io/table-schema/#types-and-formats) \n"
            "for more information about "
            "appropriate `format` values by "
            "variable `type`.\n",
            "additionalDescription": "examples/definitions "
            "of patterns and "
            "possible values:\n"
            "\n"
            "Examples of date time "
            "pattern formats\n"
            "\n"
            "- `%Y-%m-%d` (for "
            "date, e.g., "
            "2023-05-25)\n"
            "- `%Y%-%d` (for date, "
            "e.g., 20230525) for "
            "date without dashes\n"
            "- `%Y-%m-%dT%H:%M:%S` "
            "(for datetime, e.g., "
            "2023-05-25T10:30:45)\n"
            "- `%Y-%m-%dT%H:%M:%SZ` "
            "(for datetime with UTC "
            "timezone, e.g., "
            "2023-05-25T10:30:45Z)\n"
            "- "
            "`%Y-%m-%dT%H:%M:%S%z` "
            "(for datetime with "
            "timezone offset, e.g., "
            "2023-05-25T10:30:45+0300)\n"
            "- `%Y-%m-%dT%H:%M` "
            "(for datetime without "
            "seconds, e.g., "
            "2023-05-25T10:30)\n"
            "- `%Y-%m-%dT%H` (for "
            "datetime without "
            "minutes and seconds, "
            "e.g., 2023-05-25T10)\n"
            "- `%H:%M:%S` (for "
            "time, e.g., 10:30:45)\n"
            "- `%H:%M:%SZ` (for "
            "time with UTC "
            "timezone, e.g., "
            "10:30:45Z)\n"
            "- `%H:%M:%S%z` (for "
            "time with timezone "
            "offset, e.g., "
            "10:30:45+0300)\n"
            "\n"
            "Examples of string "
            "formats\n"
            "\n"
            "- `email` if valid "
            "emails (e.g., "
            "test@gmail.com)\n"
            "- `uri` if valid uri "
            "addresses (e.g., "
            "https://example.com/resource123)\n"
            "- `binary` if a base64 "
            "binary encoded string "
            "(e.g., authentication "
            "token like "
            "aGVsbG8gd29ybGQ=)\n"
            "- `uuid` if a "
            "universal unique "
            "identifier also known "
            "as a guid (eg., "
            "f47ac10b-58cc-4372-a567-0e02b2c3d479)\n"
            "\n"
            "\n"
            "Examples of geopoint "
            "formats\n"
            "\n"
            "The two types of "
            "formats for `geopoint` "
            "(describing a "
            "geographic point).\n"
            "\n"
            "- `array` (if "
            "'lat,long' (e.g., "
            "36.63,-90.20))\n"
            "- `object` (if "
            "{'lat':36.63,'lon':-90.20})\n",
        },
        "constraints.required": {
            "type": "boolean",
            "title": "Required variable",
            "description": "If this variable "
            "is marked as true, "
            "then this "
            "variable's value "
            "must be present\n"
            "(ie not missing; "
            "see "
            "missingValues). If "
            "marked as false or "
            "not present, then "
            "the \n"
            "variable CAN be "
            "missing.\n",
        },
        "constraints.maxLength": {
            "type": "integer",
            "title": "Maximum Length",
            "description": "Indicates the "
            "maximum length of "
            "an iterable "
            "(e.g., array, "
            "string, or\n"
            "object). For "
            "example, if "
            "'Hello World' is "
            "the longest value "
            "of a\n"
            "categorical "
            "variable, this "
            "would be a "
            "maxLength of "
            "11.\n",
        },
        "constraints.enum": {
            "type": "string",
            "title": "Variable Possible Values",
            "description": "Constrains possible " "values to a set of " "values.\n",
            "examples": ["1|2|3|4|5", "Poor|Fair|Good|Very " "good|Excellent"],
            "pattern": "^(?:[^|]+\\||[^|]*)(?:[^|]*\\|)*[^|]*$",
        },
        "constraints.pattern": {
            "type": "string",
            "title": "Regular Expression " "Pattern",
            "description": "A regular "
            "expression pattern "
            "the data MUST "
            "conform to.\n",
        },
        "constraints.maximum": {
            "type": "string",
            "title": "Maximum Value",
            "description": "Specifies the "
            "maximum value of a "
            "field (e.g., "
            "maximum -- or most\n"
            "recent -- date, "
            "maximum integer "
            "etc). Note, this is "
            "different then\n"
            "maxLength "
            "property.\n",
        },
        "constraints.minimum": {
            "type": "string",
            "title": "Minimum Value",
            "description": "Specifies the " "minimum value of a " "field.\n",
        },
        "enumLabels": {
            "title": "Variable Value Encodings (i.e., " "mappings; value labels)",
            "description": "Variable value encodings "
            "provide a way to further "
            "annotate any value within a "
            "any variable type,\n"
            "making values easier to "
            "understand. \n"
            "\n"
            "\n"
            "Many analytic software "
            "programs (e.g., SPSS,Stata, "
            "and SAS) use numerical "
            "encodings and some "
            "algorithms\n"
            "only support numerical "
            "values. Encodings (and "
            "mappings) allow categorical "
            "values to be stored as\n"
            "numerical values.\n"
            "\n"
            "Additionally, as another use "
            "case, this field provides a "
            "way to\n"
            "store categoricals that are "
            'stored as  "short" labels '
            "(such as\n"
            "abbreviations).\n"
            "\n"
            "This field is intended to "
            "follow [this "
            "pattern](https://specs.frictionlessdata.io/patterns/#table-schema-enum-labels-and-ordering)\n",
            "type": "string",
            "examples": [
                "1=Poor|2=Fair|3=Good|4=Very " "good|5=Excellent",
                "HW=Hello world|GBW=Good bye " "world|HM=Hi, Mike",
            ],
            "pattern": "^(?:.*?=.*?(?:\\||$))+$",
        },
        "enumOrdered": {
            "title": "An ordered variable",
            "description": "Indicates whether a "
            "categorical variable is "
            "ordered. This variable  is\n"
            "relevant for variables that "
            "have an ordered "
            "relationship but not\n"
            "necessarily  a numerical "
            "relationship (e.g., "
            "Strongly disagree < "
            "Disagree\n"
            "< Neutral < Agree).\n"
            "\n"
            "This field is intended to "
            "follow the ordering aspect "
            "of this [this pattern][this "
            "pattern](https://specs.frictionlessdata.io/patterns/#table-schema-enum-labels-and-ordering)\n",
            "type": "boolean",
        },
        "missingValues": {
            "title": "Missing Values",
            "description": "A list of missing values " "specific to a variable.\n",
            "examples": ["Missing|Skipped|No " "preference", "Missing"],
            "type": "string",
            "pattern": "^(?:[^|]+\\||[^|]*)(?:[^|]*\\|)*[^|]*$",
        },
        "trueValues": {
            "title": "Boolean True Value Labels",
            "description": "For boolean (true) variable "
            "(as defined in type field), "
            "this field allows\n"
            "a physical string "
            "representation to be cast as "
            "true (increasing\n"
            "readability of the field). "
            "It can include one or more "
            "values.\n",
            "type": "string",
            "examples": ["required|Yes|Checked", "required"],
            "pattern": "^(?:[^|]+\\||[^|]*)(?:[^|]*\\|)*[^|]*$",
        },
        "falseValues": {
            "title": "Boolean False Value Labels",
            "description": "For boolean (false) "
            "variable (as defined in "
            "type field), this field "
            "allows\n"
            "a physical string "
            "representation to be cast "
            "as false (increasing\n"
            "readability of the field) "
            "that is not a standard "
            "false value. It can include "
            "one or more values.\n",
            "type": "string",
            "examples": ["Not required|NOT REQUIRED", "No"],
            "pattern": "^(?:[^|]+\\||[^|]*)(?:[^|]*\\|)*[^|]*$",
        },
        "custom": {
            "type": "string",
            "description": "Additional properties not " "included a core property. \n",
            "pattern": "^(?:.*?=.*?(?:\\||$))+$",
        },
    },
    "patternProperties": {
        "^standardsMappings\\[\\d+\\].instrument.url$": {
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
        "^standardsMappings\\[\\d+\\].instrument.source$": {
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
        "^standardsMappings\\[\\d+\\].instrument.title$": {
            "type": "string",
            "title": "Title",
            "examples": ["Adult " "demographics", "adult-demographics"],
            "description": "",
        },
        "^standardsMappings\\[\\d+\\].instrument.id$": {
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
        "^standardsMappings\\[\\d+\\].item.url$": {
            "title": "Standards " "mappings " "- " "Url",
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
        "^standardsMappings\\[\\d+\\].item.source$": {
            "title": "Standards " "mappings " "- " "Source",
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
        "^standardsMappings\\[\\d+\\].item.id$": {
            "title": "Standards " "Mappings " "- " "Id",
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
            "source. \n"
            "Note, "
            "the "
            "`standardsMappings[0].source` "
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
        "^relatedConcepts\\[\\d+\\].url$": {
            "title": "Related " "Concepts " "- Url",
            "description": "The "
            "url "
            "that "
            "links "
            "out "
            "to "
            "the "
            "published, "
            "related "
            "concept. \n"
            "The "
            "listed "
            "examples "
            "could "
            "both "
            "be "
            "attached "
            "to "
            "any "
            "variable "
            "related "
            "to, "
            "for "
            "example, "
            "heroin "
            "use.\n",
            "type": "string",
            "format": "uri",
            "examples": [
                "https://www.ebi.ac.uk/chebi/chebiOntology.do?chebiId=CHEBI:27808",
                "http://purl.bioontology.org/ontology/RXNORM/3304",
            ],
        },
        "^relatedConcepts\\[\\d+\\].title$": {
            "title": "Related " "concepts " "- " "Type",
            "description": "A "
            "human-readable "
            "title "
            "(ie "
            "label) "
            "to "
            "a "
            "concept "
            "related "
            "to "
            "the "
            "given "
            "field.\n"
            "The "
            "listed "
            "examples "
            "could "
            "both "
            "be "
            "attached "
            "to "
            "any "
            "variable "
            "related "
            "to, "
            "for "
            "example, "
            "heroin "
            "use.\n",
            "type": "string",
            "examples": ["Heroin " "Molecular " "Structure", "Heroin " "Ontology"],
        },
        "^relatedConcepts\\[\\d+\\].source$": {
            "title": "Related " "Concepts " "- " "Source",
            "description": "The "
            "source "
            "(e.g., "
            "a "
            "dictionary "
            "or "
            "vocabulary "
            "set) "
            "to "
            "a "
            "concept "
            "related "
            "to "
            "the "
            "given "
            "field.\n"
            "The "
            "listed "
            "examples "
            "could "
            "both "
            "be "
            "attached "
            "to "
            "any "
            "variable "
            "related "
            "to, "
            "for "
            "example, "
            "heroin "
            "use.\n",
            "type": "string",
            "examples": ["CHEBI", "RXNORM"],
        },
        "^relatedConcepts\\[\\d+\\].id$": {
            "title": "Related " "Concepts " "- Id",
            "type": "string",
            "description": "The "
            "id "
            "locating "
            "the "
            "individual "
            "concept "
            "within "
            "the "
            "source "
            "of "
            "the "
            "given "
            "field.\n"
            "The "
            "listed "
            "examples "
            "could "
            "both "
            "be "
            "attached "
            "to "
            "any "
            "variable "
            "related "
            "to, "
            "for "
            "example, "
            "heroin "
            "use.\n",
            "examples": ["27808", "3304"],
        },
    },
}
