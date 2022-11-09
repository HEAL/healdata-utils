''' 

command line interface for generating HEAL data dictionary/vlmd json files

TODO: refactor top level data dictionary values and validation 
''' 


import click 
from healdata_utils.transforms.csvtemplate.conversion import convert_template_csv_to_json
from healdata_utils.transforms.readstat.conversion import convert_readstat
import json
from pathlib import Path
import jsonschema
import healdata_utils.schemas as schemas

choice_fxn = {
    'csvtemplate': convert_template_csv_to_json,
    'spss': convert_readstat
}

#TODO: make scheam a CLI option?
schema = schemas.heal['data_dictionary']


def main(filepath,title,description,inputtype,outputdir):
    ''' 
    write a data dictioanry (ie variable level metadata)
    to a HEAL metadata json file
    '''
    outputdir = Path(outputdir)
    filepath = Path(filepath)

    # get data dictionary based on the input type
    # NOTE: the spss function is temporary -- will only output a python dict in future but put this 
    # in for demo purpo9se
    dd_fields = choice_fxn[inputtype](filepath)

    #TODO: pull down to validate entrie data dict
    schemas.validate(dd_fields)

    ## add top level data dictionary information
    data_dictionary = {}

    ##(TODO: need to add required title directly to schema and validation 
    ## add data dictionary level fields
    if description:
        data_dictionary['description'] = description

    ## add dd title
    if title:
        data_dictionary['title'] = title
    else:
        data_dictionary['title'] = filepath.stem

    data_dictionary['data_dictionary'] = dd_fields

    #Output jsonfile
    outputdir_is_file = len(outputdir.suffixes)>0
    if outputdir_is_file:
        outputpath = outputdir
    else:
        outputpath = outputdir/filepath.with_suffix('json').name

    with open(outputpath,'w') as f:
        json.dump(data_dictionary,f,indent=4)

        
@click.command()
@click.option('--filepath',required=True,help='Path to the file you want to convert to a HEAL data dictionary')
@click.option('--title',default=None,help='The title of your data dictionary. If not specified, then the file name will be used')
@click.option('--description',default=None,help='Description of data dictionary')
@click.option('--inputtype',default='csvtemplate',type=click.Choice(list(choice_fxn.keys())),help='The type of your input file.')
@click.option('--outputdir',help='The folder where you want to output your HEAL data dictionary')
def main(filepath,title,description,inputtype,outputdir):
    ''' 
    write a data dictioanry (ie variable level metadata)
    to a HEAL metadata json file
    '''
    outputdir = Path(outputdir)
    filepath = Path(filepath)

    # get data dictionary based on the input type
    # NOTE: the spss function is temporary -- will only output a python dict in future but put this 
    # in for demo purpo9se
    dd_fields = schemas.validate(choice_fxn[inputtype](filepath))

    #TODO: pull down to validate entrie data dict

    ## add top level data dictionary information
    data_dictionary = {}

    ##(TODO: need to add required title directly to schema and validation 
    ## add data dictionary level fields
    if description:
        data_dictionary['description'] = description

    ## add dd title
    if title:
        data_dictionary['title'] = title
    else:
        data_dictionary['title'] = filepath.stem

    data_dictionary['data_dictionary'] = dd_fields

    #Output jsonfile
    outputdir_is_file = len(outputdir.suffixes)>0
    if outputdir_is_file:
        outputpath = outputdir
    else:
        outputpath = outputdir/filepath.with_suffix('json').name

    with open(outputpath,'w') as f:
        json.dump(data_dictionary,f,indent=4)


if __name__=='__main__':
    main()