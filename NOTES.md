# Notes during healdata_utils development

## General 
- **mappings**: need to think about type and format mappings. created a few mappings (see `healdata_utils.mappings` module but will need to further flesh out and account for conditional mappings -- ie if type==X and format==Y then format==U and type==Z)
    - bacpac: what is the data source where data types/formats came from?
    - hemo: SAS type/format mappings