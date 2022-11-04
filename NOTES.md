# Notes during healdata_utils development

## General 
- need to think about type and format mappings. created a few mappings (see `healdata_utils.mappings` module but will need to further flesh out and account for conditional mappings -- ie if type==X and format==Y then format==U and type==Z)

## Study specific
## bacpac
- BACPAC data dictionaries were manually converted from here https://docs.google.com/spreadsheets/d/1x4WNLEjT98tgUq6c1GGj1syeNvj_eUyE/edit#gid=2024186250
- TODO: should dds be derived from the define.xml file?