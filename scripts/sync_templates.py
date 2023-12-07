import healdata_utils
from pathlib import Path
import yaml

template_params = Path("configs/write_vlmd_template.yaml").read_text()
template_params = yaml.safe_load(template_params)

for p in template_params:
    healdata_utils.write_vlmd_template(**p)
