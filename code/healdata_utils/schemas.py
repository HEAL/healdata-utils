from pathlib import Path
import requests
from frictionless import Schema

heal = {
    'data_dictionary': Schema(
        "https://raw.githubusercontent.com/norc-heal/heal-metadata-schemas/"
        "mbkranz/variable-lvl/variable-level-metadata-schema/schemas/fields.json"
    ).to_dict()
}