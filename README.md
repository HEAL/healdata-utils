# HEAL Data Dictionaries


## Data Dictionaries

This repository (in the subdirectory `data-dictionaries`) holds HEAL investigator data dictionaries collected by the HEAL ecosystem Data Task Force Team in addition to the outputs after parsing to json format after validation. 

It is organized by appl_id (ie., study). If adding an additionla study, please add to the below key for easier look up.


See the list of studies with associated appl_id and grant_numbers [here](./studies.yaml)


## Code

Currently, the code contains the package healdata-utils. While this repository is for data-dictionaries right now, `healdata-utils` 
will be expanded for all heal specific data packaging functions. However, given the focus is on data dictionaries currently and all functions are for outputting said data-dictionaries, it is housed here for now.

To use, after spinning up a virtual environment,
navigate to this directory (e.g., `cd <path>/heal-data-dictionaries`)  and run `pip install .`
or `pip install -e .` if you are developing the code.

If using conda, can run:

`conda create -f requirements.yaml`

### Converting input to output data dictionaries
From this directory, run:

`python ./code/data_dictionaries.py` to convert input data_dictionaries.