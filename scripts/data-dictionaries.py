""" 
converting various formats to HEAL data dictionaries

"""
from healdata_utils.cli import to_json,to_csv_from_json
from healdata_utils.config import studies,ROOT_DIR
import json

for study,info in studies.items():
    data_dictionaries = info.get('data_dictionaries')
    if data_dictionaries:
        for dd in data_dictionaries:
            input_file = ROOT_DIR/'data-dictionaries'/study/'input'/dd['file_name']
            outputdir = input_file.parents[1]/'output'/input_file.with_suffix('.json').name
            to_json(input_file,outputdir,title=dd['title'])
            to_csv_from_json(outputdir,outputdir.with_suffix(".csv"))
