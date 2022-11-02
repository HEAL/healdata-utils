from pathlib import Path
import requests


heal = {
    'data_dictionary': requests.get(
        "https://raw.githubusercontent.com/HEAL/heal-metadata-schemas/"
        "variable-level-metadata/variable-level-metadata-schema/schemas/fields.json"
    ).json()
}