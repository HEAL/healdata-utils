import pandas as pd
#STEPS
#1 fill section headers
#2 sort rows to allow proper row indexing
#3 make conditionals for each map function
# NOTES	- large text box for lots of text
# DROPDOWN	- dropdown menu with options
# RADIO	- radio buttons with options
# CHECKBOX	- checkboxes to allow selection of more than one option
# FILE	- upload a document
# CALC	- perform real-time calculations
# SQL	- select query statement to populate dropdown choices
# DESCRIPTIVE	- text displayed with no data entry and optional image/file attachment
# SLIDER	- visual analogue scale; coded as 0-100
# YESNO	- radio buttons with yes and no options; coded as 1, Yes | 0, No
# TRUEFALSE	- radio buttons with true and false options; coded as 1, True | 0, False

def maptext(field,text_validation_colindex=6):
    """ 
    TEXT - single-line text box (for text and numbers)

    looks at text validation field
    """
    text_validation = field[text_validation_colindex].lower()



    fieldformat = None 
    fieldpattern = None
    if "datetime" in text_validation:
        fieldtype = "datetime"
        fieldformat = "any"
    elif "date" in text_validation:
        fieldtype = "date"
        fieldformat = "any" 
    elif text_validation=="email":
        fieldtype = "string"
        fieldformat = "email"
    elif text_validation=="integer":
        fieldtype = "integer"
    elif text_validation=="alpha_only":
        fieldtype = "string"
        fieldpattern = "^[a-zA-Z]+$"
    elif "number" in text_validation:
        fieldtype = "number"
        if "comma_decimal" in text_validation:
            fielddecimal_char = ","
    elif text_validation=="phone":
        fieldtype = "string"
        fieldpattern = "^[0-9]{3}-[0-9]{3}-[0-9]{4}$" 
    elif text_validation=="postalcode_australia":
        fieldtype = "string"
        fieldpattern = "^[0-9]{4}$"
    elif text_validation=="postalcode_canada":
        fieldtype = "string"
        fieldpattern = "^[A-Z][0-9][A-Z] [0-9][A-Z][0-9]$"
    elif text_validation=="ssn":
        fieldtype = "string"
        fieldpattern = "^[0-9]{3}-[0-9]{2}-[0-9]{4}$"
    elif "time" in text_validation:
        fieldtype = "time"
        fieldformat = "any"
    elif text_validation=="vmrn":
        fieldtype = "string"
        fieldpattern = "^[0-9]{10}$"
    elif text_validation=="zipcode":
        fieldtype = "string"
        fieldpattern = "^[0-9]{5}$"
    else:
        fieldtype = "string"
    
    return {
        "type":fieldtype,
        "format":fieldformat,
        "constraints.pattern":fieldpattern
    }

def mapnotes(field):
    """ NOTES	
    large text box for lots of text
    """
    return {"type":"string"}

def mapdropdown(field):
    """ 
    DROPDOWN	
    dropdown menu with options

    Determined by "options" (ie Choices, Calculations, OR Slider Labels)
    """
    # parse enum/encodings


    {"type":"integer"}
def mapradio(field):
    """ 
    RADIO	- radio buttons with options

    Determined by "options" (ie Choices, Calculations, OR Slider Labels)

    """
    # parse enum/encodings 


def mapcheckbox(field):
    """ 
    CHECKBOX	- checkboxes to allow selection of more than one option


    ## Are data from checkbox (choose all that apply) field types handled differently from other field types when imported or exported?
    Yes. When your data are exported, each option from a checkbox field becomes a separate variable coded 1 or 0 to reflect whether it is checked or unchecked. By default, each option is pre-coded 0, so even if you have not yet collected any data, you will see 0's for each checkbox option. The variable names will be the name of the field followed by the option number. So, for example, if you have a field coded as follows:

    Race

    1, Caucasian

    2, African American

    3, Asian

    4, Other

    In your exported dataset, you will have four variables representing the field Race that will be set as 0 by default, coded 1 if the option was checked for a record. The variable names will consist of the field name. three underscores, and the choice value:

    race___1
    race___2
    race___3
    race___4

    Notes:

    when you import data into a checkbox field, you must code it based on the same model
    negative values can be used as the raw coded values for checkbox fields. Due to certain limitations, negative values will not work when importing values using the Data Import Tool, API and cause problems when exporting data into a statistical analysis package. The workaround is that negative signs are replaced by an underscore in the export/import-specific version of the variable name (e.g., for a checkbox named "race", its choices "2" and "-2" would export as the fields
    race___2

    race____2

    A checkbox field can be thought of as a series of yes/no questions in one field. Therefore, a yes (check) is coded as 1 and a no (uncheck) is coded a 0. An unchecked response on a checkbox field is still regarded as an answer and is not considered missing.
    """ 


def mapfile(field):
    pass 


def mapcalc(field):
    pass 


def mapsql(field):
    pass 


def mapyesno(field):
    pass 


def maptruefalse(field):
    pass 


def mapslider(field):
    pass 

def mapdescriptive(field):
    pass 

def mapfile(field):
    pass 

# race___2
# race____2




RADIO	
radio buttons with options
"radio"
CHECKBOX	
checkboxes to allow selection of more than one option
"checkbox"
FILE	
upload a document
FILE with Text Validation "Signature" = Signature Field
"file"
CALC	
perform real-time calculations
"calc"
SQL	
select query statement to populate dropdown choices
"sql"
DESCRIPTIVE	
text displayed with no data entry and optional image/file attachment
"descriptive"
SLIDER	
visual analogue scale; coded as 0-100
"slider"
YESNO	
radio buttons with yes and no options; coded as 1, Yes | 0, No
"yesno"
TRUEFALSE	
radio buttons with true and false options; coded as 1, True | 0, False
"truefalse"

# demo csv
demopath = r"C:\Users\kranz-michael\Downloads\REDCapDataDictonaryDemo (1).csv"
demodf = pd.read_csv(demopath)