""" 
spss/sas/stata --> to HEAL data dictionary

"""
from healdata_utils.transforms.readstat.conversion import convert_readstat
from healdata_utils.config import studies,ROOT_DIR
import json

for study,info in studies.items():
    data_dictionaries = info.get('data_dictionaries')
    if data_dictionaries:
        for dd in data_dictionaries:
            if dd.get('conversiontype')=='spss':
                input_file = ROOT_DIR/'data-dictionaries'/study/'input'/dd['file_name']
                outputdir = input_file.parents[1]/'output'
                jsontemplate,csvtemplate = convert_readstat(input_file,to_json=True,to_csv=True)

                csvpath = outputdir/(input_file.stem.lower()+'.csv')
                csvtemplate.to_csv(csvpath)

                jsonpath = outputdir/(input_file.stem+'.json')
                #NOTE: temp workaround: json--> dict --> json file
                jsonpath.write_text(
                    json.dumps({'title':dd['title'],'data_dictionary':jsontemplate},indent=4),
                )

