from pathlib import Path
import yaml 
import healdata_utils


params = Path("configs/convert_to_vlmd.yaml").read_text()
params = yaml.safe_load(params)

for p in params:
    healdata_utils.convert_to_vlmd(**p)



