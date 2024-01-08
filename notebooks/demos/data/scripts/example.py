# %%
""" 
writes example files for proof of concept and/or testing

""" 
#TODO: write xport file and make PROC FORMAT .sas script
 # for reading into SAS to get .sas7bdat. (pyreadstat cant write)

# %%
import pyreadstat
import pandas as pd
import copy
import os 
import pathlib
from healdata_utils.transforms.readstat.conversion import convert_readstat
import json
from pathlib import Path
os.chdir(pathlib.Path(__file__).parent)

# %%
headers = "id visit_dt sex_at_birth race hispanic_ethnicity SU4 age"
rows = [
    [1,"06/05/1988",1,2,1,15,59],
    [2,"04/07/1989",2,2,0,4,48],
    [3,"04/07/1990","a","b","a","a",33],
    [3,"04/07/1990","b","a","b","b",33]
]

df = pd.DataFrame(rows,columns=headers.split(" "))
#NOTE: date format is inferred and carried over to output
df = df.apply(pd.to_numeric, errors='ignore')
df['visit_dt'] = pd.to_datetime(df['visit_dt'])

# %%
descriptions = {
    "id":"Unique identifier for participant",
    "visit_dt":"Date of the interview",
    "sex_at_birth":"The self-reported sex of the participant/subject at birth",
    "race":"Self-reported race",
    "hispanic_ethnicity":"Are you of Hispanic, Latino, or Spanish origin?",
    "SU4":"Heroin Days Used in days",
    "age":"Age of participant in year"
}

encodings = {
    "sex_at_birth":{
        1:"Male",
        2:"Female",
        3:"Intersex" ,
        4:"None of these describe me" ,
        "a":"Not reported" ,
        "b":"Prefer not to answer"
    },
    "race":{
        1:"White",
        2:"Black or African American",
        3:"American Indian or Alaska Native",
        4:"Native",
        5:"Hawaiian or Other Pacific Islander",
        6:"Asian",
        7:"Some other race" ,
        8:"Multiracial", 
        "a":"Not reported" ,
        "b":"Prefer not to answer"
     },
    "hispanic_ethnicity":{
        1:"Yes",
        0:"No",
        "a":"Not reported",
        "b":"Prefer not to answer"
    },
    "age":{
        "a":"Not reported",
        "b":"Prefer not to answer"
    },
    "SU4":{
        "a":"Not reported",
        "b":"Prefer not to answer"
    }
}

missing_stata = {
    varname:["a","b"]
    for varname in descriptions.keys()
}


def mapmissing(mapping,encodings):
    """ map constant missing values

    encodings = pyreadstat variable value labels

    Example:
    mapping = {"a":-99}
    encodings = {"var1":{1:"test","a":"test2"},...}
    """
    encodings = copy.deepcopy(encodings)
    for varname in list(encodings):
        encodings[varname] = pd.Series(encodings[varname])\
            .rename(index=mapping)\
            .to_dict()

    return encodings

# %%
df_spss = df.replace({"a":-99,"b":-98}).convert_dtypes()
encodings_spss = mapmissing({"a":-99,"b":-98},encodings)
missing_spss = {
    varname:[-99,-98]
    for varname in descriptions.keys()
}

# %%
pyreadstat.write_dta(df,
    "../example_pyreadstat_output.dta",
    missing_user_values=missing_stata,
    variable_value_labels=encodings,
    column_labels=descriptions
    )

#NOTE about missing values (ie missing_ranges)
# missing_ranges (dict, optional) – user defined missing values. 
# Must be a dictionary with keys as variable names matching variable names in the dataframe. 
# The values must be a list. Each element in that list can either be either a discrete numeric or string value (max 3 per variable)
#  or a dictionary with keys ‘hi’ and ‘lo’ to indicate the upper and lower range for numeric values (max 1 range value + 1 discrete value per variable). 
# hi and lo may also be the same value in which case it will be interpreted as a discrete missing value. For this to be effective, values in the dataframe must be the same as reported here and not NaN.
pyreadstat.write_sav(df_spss,
    "../example_pyreadstat_output.sav",
    missing_ranges=missing_spss,
    variable_value_labels=encodings_spss,
    column_labels=descriptions
    )

#%%
for ext in ["sav","dta"]:
    dds = convert_readstat(f"../example_pyreadstat_output.{ext}")

    #%%
    ddjson = json.dumps(dds['templatejson'],indent=4)
    Path(f"../example_{ext}_pyreadstat_output.json").write_text(ddjson)

    pd.DataFrame(dds['templatecsv']["fields"])\
        .to_csv(f"../example_{ext}_pyreadstat_output.csv",index=False)

