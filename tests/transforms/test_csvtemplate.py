from healdata_utils.transforms.csvtemplate import conversion
from conftest import compare_vlmd_tmp_to_output
from conftest import valid_input_params,valid_output_json,valid_output_csv,fields_propname
from pathlib import Path
import shutil

def test_update_templatecsv_version():
    params = dict(valid_input_params["csv-version-update"])
    input_filepath = params["input_filepath"]
    outputdir = "tmp"
    # make an empty temporary output directory
    try:
        Path(outputdir).mkdir()
    except FileExistsError:
        shutil.rmtree(outputdir)
        Path(outputdir).mkdir()

    data_dictionaries = conversion.update_templatecsv_version(input_filepath,**params)

    # clean up
    shutil.rmtree(outputdir)