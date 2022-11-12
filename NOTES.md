# Notes during healdata_utils development

## General 
- **mappings**: need to think about type and format mappings. created a few mappings (see `healdata_utils.mappings` module but will need to further flesh out and account for conditional mappings -- ie if type==X and format==Y then format==U and type==Z)
    - bacpac: what is the data source where data types/formats came from?
    - hemo: SAS type/format mappings

## Study specific
```yaml
bacpac:
  notes: >
    BACPAC data dictionaries were manually converted to template from here 
    https://docs.google.com/spreadsheets/d/1x4WNLEjT98tgUq6c1GGj1syeNvj_eUyE
  todo: 
    - should dds be derived from the define.xml file?
    - what was the data collection instrument used?
    - These data dictionaries replace the previous data dictionaries derived from the (data) tsv files currently on the platform. These files presumably are from there gen3 system. Shouldnt we use these? (Regardless, these provide a good test case especially for the long format questionnaire dataset)
hemo:
  notes: >
    Pulled from https://repository.niddk.nih.gov/media/studies/hemo/Data%20Dictionary.pdf (annual.sas7bdat)
    and manually converted to template. This data dictionary was from a set of SAS data files.
  todo: 
    - map SAS formats to standard

stigma:
  notes: >
    copied output over from a repository specific to stigma surveys. Will incorporate an SPSS conversion tool (currently leveraging this code to incorporate into the healdata-utils)




```

    