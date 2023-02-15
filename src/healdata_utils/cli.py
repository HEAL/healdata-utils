''' 

command line interface for generating HEAL data dictionary/vlmd json files

#TODO: make scheam a CLI option?
#TODO: port to_json and to_csv fxns outputside of CLI? to an io.py folder?
''' 


import click 
from healdata_utils.transforms.csvtemplate.conversion import convert_template_csv_to_json
from healdata_utils.transforms.csvtemplate.conversion import convert_json_to_template_csv
from healdata_utils.transforms.readstat.conversion import convert_readstat
from healdata_utils.transforms.redcap.conversion import convert_redcap
from healdata_utils.transforms.redcapcsv.conversion import convert_redcapcsv
import json
from pathlib import Path
import jsonschema
from healdata_utils.schemas import validate_json
import pandas as pd
choice_fxn = {
    'csv': convert_template_csv_to_json,
    'sav': convert_readstat,
    'dta':convert_readstat,
    'por':convert_readstat,
    'sas7bdat':convert_readstat,
    'json':convert_json_to_template_csv,
    'redcap.xml': convert_redcap,
    "redcap.csv":convert_redcapcsv

}
choice_fxn_md = "\n - ".join(list(choice_fxn.keys())[1:])

def generate_outputpath(input_filepath,outputdir,suffix='json'):


    outputdir_is_file = len(outputdir.suffixes)>0
    if outputdir_is_file:
        outputpath = outputdir
    else:
        outputpath = Path(outputdir)/input_filepath.with_suffix(f".{suffix}").name
    return outputpath 

def to_json(filepath,outputdir,data_dictionary_props={},inputtype=None,):
    f""" 
    writes a data dictioanry (ie variable level metadata)
    to a HEAL metadata json file using a registered function.


    Parameters
    -------------
    filepath: path to input file 
    outputdir: path to a directory where output will go. 
        If a directory is specified, will use the input name for output name replaced with json suffix.
    data_dictionary_props: The other data-dictionary level properties. By default, will 
        give the data_dictionary `title` property as the file name stem. 
    inputtype: The input type. If none specified, will default to using the file extension.
        Currently the registered inputs types are: 
        {choice_fxn_md} 
    """
    filepath = Path(filepath)
    outputdir = Path(outputdir)
    #infer input type
    if not inputtype:
        inputtype = ''.join(filepath.suffixes)[1:].lower()

    ## add dd title
    if not data_dictionary_props.get('title'):
        data_dictionary_props['title'] = filepath.stem

    # get data dictionary based on the input type
    data_dictionary = choice_fxn[inputtype](filepath,data_dictionary_props)


    # VALIDATE
    print('Validating output json file.....')
    validate_json(data_dictionary)

    # write to file
    if Path(outputdir).is_dir():
        Path(outputdir).mkdir(exist_ok=True)
        outputpath = outputdir/filepath.name.replace(".csv",".json")
    
    else:
        outputpath = outputdir

    with open(outputpath,'w') as f:
        json.dump(data_dictionary,f,indent=4)

def to_csv_from_json(filepath,outputdir):
    ''' 
    converts a json file to a csv

    Parameters
    ---------------
    filepath: path to input file 
    outputdir: path to a directory where output will go. 
        If a directory is specified, will use the input name for output name replaced with json suffix.

    Returns
    --------------
    None


    ''' 
    assert filepath.suffix==".json","filepath needs to be a json file"

    resource = choice_fxn['json'](filepath)
    
   # write to file
    if Path(outputdir).is_dir():
        Path(outputdir).mkdir(exist_ok=True)
        outputpath = outputdir/filepath.name.replace(".json",".csv")
    
    else:
        outputpath = outputdir

    # write data dictionary fields
    pd.DataFrame(resource.data).to_csv(outputpath,index=False)

@click.command()
@click.option('--filepath',required=True,help='Path to the file you want to convert to a HEAL data dictionary')
@click.option('--title',default=None,help='The title of your data dictionary. If not specified, then the file name will be used')
@click.option('--description',default=None,help='Description of data dictionary')
@click.option('--inputtype',default=None,type=click.Choice(list(choice_fxn.keys())),help='The type of your input file.')
@click.option('--outputdir',help='The folder where you want to output your HEAL data dictionary')
def main(filepath,title,description,inputtype,outputdir):
    ''' 
    write a data dictioanry (ie variable level metadata)
    to a HEAL metadata json file
    '''
    
    if not outputdir:
        
        outputdir = Path(filepath).parent.parent/'output'

    if inputtype=='json':
        to_csv_from_json(filepath, outputdir)
    else:
        to_json(filepath,outputdir,{'title':title,'description':description},inputtype,)
  
if __name__=='__main__':
    main()