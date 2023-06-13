# %%

from pathlib import Path 
from healdata_utils.cli import convert_to_vlmd
import os 
import pandas as pd
import json
import shutil

from healdata_utils.cli import input_descriptions
from IPython.display import Markdown,display
os.chdir(Path(__file__).parent)
def printdir(dirname):
    for d in Path(dirname).iterdir():
        print(d)
        if Path(d).is_dir():
            for _d in Path(d).iterdir():
                print(f"   {_d}")

# %%
# current file paths for proof of concept
demo_filepaths = {
    # first 20 records of NMHSS SAMHDA Public Use File 
    "sas7bdat":"data/example_nmhss_2019_first_20recs.sas7bdat", 
    # SPSS/Stata examples created from pyreadstat via notebooks/demos/scripts/example.py
    "dta":"data/example_pyreadstat_output.dta", 
    "sav":"data/example_pyreadstat_output.sav",
    # The demostration CSV data dictionary exported from UChicago Redcap instance
    "redcap.csv":"data/example_redcap_demo.redcap.csv",
    # Valid csv version of pyreadstat 
    "csv":"data/example_pyreadstat_output.csv"
}
# %%
description = "This is a proof of concept to demonstrate the healdata-utils functionality"
title = "Healdata-utils Demonstration Data Dictionary"
healdir = "output"
input_type = "sas7bdat"
inputpath = demo_filepaths[input_type]
if input_type=="sas7bdat":
    sas7bcat_filepath = "../../tests/data/sas-nmhss-2019/formats.sas7bcat"
else:
    sas7bcat_filepath = None
#%%
# import pyreadstat
# test = pyreadstat.read_sas7bcat(sas7bcat_filepath)

# %%
# make python demo output
Path(healdir).mkdir(exist_ok=True)

# %%
data_dictionaries = convert_to_vlmd(
    filepath=inputpath,
    outputdir=healdir, #if not specified, will not write to file
    inputtype=input_type, #if not specified, looks for suffix
    data_dictionary_props={
        "name":Path(inputpath).stem,
        "title":title,
        "description":description},
    sas7bcat_filepath=sas7bcat_filepath
)
