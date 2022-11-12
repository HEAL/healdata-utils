from pathlib import Path
import json 
from gen3.auth import Gen3Auth
from gen3.metadata import Gen3Metadata
from healdata_utils.config import studies,ROOT_DIR

GEN3_ENV = ROOT_DIR/'.gen3'/'qa-heal.json'
#GEN3_ENV = ROOT_DIR/'.gen3'/'preprod-heal.json'
auth = Gen3Auth(refresh_file=GEN3_ENV.as_posix())
metadata = Gen3Metadata(auth)

for study,info in studies.items():
    data_dictionaries = info.get('data_dictionaries')
    if data_dictionaries:
        for dd in data_dictionaries:
            output_file = ROOT_DIR/'data-dictionaries'/study/'output'/(Path(dd['file_name']).stem+'.json')
            mds_dd = {
                "_guid_type": "data_dictionary",
                "data_dictionary":json.loads(output_file.read_text())
            }
            metadata.create(metadata=mds_dd,guid=dd['guid'],overwrite=True)