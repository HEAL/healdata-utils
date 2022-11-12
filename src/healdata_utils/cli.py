''' 

command line interface for generating HEAL data dictionary/vlmd json files

#TODO: make scheam a CLI option?
#TODO: port to_json and to_csv fxns outputside of CLI?
''' 


import click 
from healdata_utils.transforms.csvtemplate.conversion import convert_template_csv_to_json
from healdata_utils.transforms.csvtemplate.conversion import convert_json_to_template_csv
from healdata_utils.transforms.readstat.conversion import convert_readstat
import json
from pathlib import Path
import jsonschema
from healdata_utils.schemas import validate_json

choice_fxn = {
    'csv': convert_template_csv_to_json,
    'sav': convert_readstat,
    'json':convert_json_to_template_csv
}

def generate_outputpath(input_filepath,outputdir,suffix='json'):


    outputdir_is_file = len(outputdir.suffixes)>0
    if outputdir_is_file:
        outputpath = outputdir
    else:
        outputpath = Path(outputdir)/input_filepath.with_suffix(f".{suffix}").name
    return outputpath 

def to_json(filepath,outputdir,title=None,description=None,inputtype=None,):
    ''' 
    write a data dictioanry (ie variable level metadata)
    to a HEAL metadata json file
    '''
    outputdir = Path(outputdir)
    filepath = Path(filepath)
    if not inputtype:
        inputtype = Path(filepath).suffix.replace('.','')

    outputdir.parent.mkdir(exist_ok=True)

    # get data dictionary based on the input type
    dd_fields = choice_fxn[inputtype](filepath)

    ## add top level data dictionary information
    data_dictionary = {'data_dictionary':dd_fields}



    if description:
        data_dictionary['description'] = description

    ## add dd title
    if title:
        data_dictionary['title'] = title
    elif data_dictionary.get('title'):
        pass 
    else:
        data_dictionary['title'] = filepath.stem

    # VALIDATE
    print('Validating output json file.....')
    validate_json(data_dictionary)

    #Output jsonfile
    outputpath = generate_outputpath(filepath, outputdir,'json')

    with open(outputpath,'w') as f:
        json.dump(data_dictionary,f,indent=4)

def to_csv_from_json(filepath,outputdir,title=None,description=None,):
    ''' 
    converts a json file to a csv
    ''' 
    if not title:
        title = filepath.stem

    Path(outputdir).parent.mkdir(exist_ok=True)
    resource = choice_fxn['json'](filepath,{"title":title,"description":description})
    
    #print('Checking input json file.....')

    outputpath = generate_outputpath(filepath, outputdir,'csv')

    # TODO: write data dictionary params and path to CSV templates
    # del resource['data']
    # resource.path = Path(outputpath).name
    # resource.to_yaml(Path(outputpath).with_suffix('.yaml'))

    # write data dictionary fields
    resource.to_petl().tocsv(outputpath)

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
        print(outputdir)

    if inputtype=='json':
        to_csv_from_json(filepath, outputdir)
    else:
        to_json(filepath,outputdir,title,description,inputtype,)
  
if __name__=='__main__':
    main()