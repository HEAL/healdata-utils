# Supported Input Formats

In this section, supported formats for generating heal-compliant data dictionaries are listed. We also provide additional instructions on how to get the necessary input files format/software.

### Redcap: Data Dictionary CSV Export

For users collecting data in a [Redcap](https://www.project-redcap.org) data management system, HEAL-compliant data dictionaries can be generated directly from Redcap exports. 

The redcap data dictionary export serves the purpose of providing variable level metadata in a standardized,tabular format and is generally easy to export. The HEAL data utilities leverages this user experience and standardized format to enable HEAL researchers to generate a Heal-compliant data dictionary. 


#### Export your Redcap data dictionary 

To download a Redcap CSV export do the following*: 


1. After logging in to your Redcap project page, locate the `Data dictionary` page. A link to this page may be available on the project side bar (see image below) or in the `Project Setup tab` at the top of your page.

![redcap_dd_link](../assets/redcap_data_dictionary_page.png "Redcap DD Export button")

2. After arriving at the `Data dictionary` page, click on `Download the current data dictionary` to export the dictionary (see below).

![redcap_export_link](../assets/redcap_csv_dd_export_link.png "Redcap DD Export button")

*there may be slight differences depending on your specific Redcap instance and version

#### Run the `vlmd` command

```bash
vlmd --filepath input/example_redcap_demo.redcap.csv --inputtype redcap.csv --outputdir output/heal-vlmd-from-redcap.csv
```

### SAS `sas7bdat` (and `sas7bcat`) files

To accomodate SAS users, HEAL data utilities supports the binary `Sas7bdat` file format, which contains the actual data values (observations/records). This file also includes variable metadata (variable `names` and variable labels/ `descriptions`).

HEAL data utilities also provides the option to accompany the `sas7bdat` file with a file of another format -- the `Sas7bcat` file.  This type of file contains variable value labels, or `encodings` that can be mapped onto datasets. 

#### Creating a `sas7bdat` and a `sas7bcat` file

Many SAS users create formats and labels in their current workflows. In this section, we provide syntax that can be easily copy-pasted into these existing workflows to create `sas7bdat` and `sas7bcat` files to input easily into the `vlmd` tool. 

This script template can be run separately or inserted directly at the end of a SAS user's workflow.

???+ Template
    ```sas title="template.sas"
    /*1. Read in data file without value labels and run full code. 
            Note: The most important pieces to run here are the PROC FORMAT statement(s) and any data steps 
            that assign formats and variable labels which are needed for the data dictionary*/

    %INCLUDE "<INSERT SAS SCRIPT HERE FILE PATH HERE>"; /* THIS WILL RUN A SEPARATE SAS SCRIPT*/
    %INCLUDE "<INSERT SAS SCRIPT HERE FILE PATH HERE>"; /* THIS WILL RUN A SECOND SEPARATE SAS SCRIPT*/

    /*2. Output the format catalog (sas7bcat) */
    /*2a. If you do not have an out directory, assign one to output the SAS catalog and data file - maybe this 
            should be at the very top?*/

    libname out "<INSERT THE DESIRED LOCATION (FILE PATH) TO YOUR SAS7BCAT AND SAS7BDAT FILES HERE>";

    /*2b. Output the format catalog.
            The format catalog is automatically stored in work.formats. This step copies the format file to the 
            out directory as a sas7bcat file.*/
    proc catalog cat=work.FORMATS;
        copy out=out.FORMATS;
        run;
        
    /*3. Output the data file (sas7bdat) */
    data out.yourdata;
        set <INSERT THE NAME OF YOUR FINAL SAS DATASET HERE>;
        run;

    ```


The below SAS syntax is an example of how to use the template within your SAS workflow.

Here we create all of our variable and value labels. This could be within one or multiple sas scripts
but for demonstration purposes, we only use one script. In your existing workflows, these may also include analyses and other PROC calls for data exploration

???+ Example Template Usage

    ```sas title="my_existing_sas_workflow.sas"

    /*2. Read in input data */
    proc import datafile="myprojectfolder/input/mydata.csv"
        out=raw
        dbms=csv replace;
        getnames=yes;
    run;

    /*3. Set up proc format and apply formats and variable labels in data step */
    proc format;
        VALUE YESNO
        0		="No"
        1		="Yes"
        
        VALUE PUBLIC
        1='State mental health authority (SMHA)'
        2='Other state government agency or department'
        3='Regional/district authority or county, local, or municipal government'
        4='Tribal government'
        5='Indian Health Service'
        6='Department of Veterans Affairs'
        7='Other'
        
        VALUE FOCUS
        1='Mental health treatment'
        2='Substance abuse treatment'
        3='Mix of mental health and substance abuse treatment (neither is primary)'
        4='General health care'
        5='Other service focus';

    **Apply formats;
    data processed;
        set raw;
        
        format YOUNGADULTS TREATPSYCHOTHRPY TREATTRAUMATHRPY YESNO. FOCUS FOCUS. PUBLIC PUBLIC.;
        label YOUNGADULTS="Accepts young adults (aged 18-25 years old) for Tx"
                TREATPSYCHOTHRPY="Facility offers individual psychotherapy"
                TREATTRAUMATHRPY="Facility offers trauma therapy"
                FOCUS="Primary treatment focus of facility"
                PUBLIC="Public agency or department that operates facility";
    run;
    ```

    This second script called `my_output.sas` is the filled out template ([see here](template.md)). Note the `%INCLUDE` function that calls `my_existing_sas_workflow.sas`

    ```sas title="my_output.sas"
    /*1. Read in data file without value labels and run full code. 
            Note: The most important pieces to run here are the PROC FORMAT statement(s) and any data steps 
            that assign formats and variable labels which are needed for the data dictionary*/

    %INCLUDE "myprojectfolder/myworkflow.sas"; /* THIS WILL RUN A SEPARATE SAS SCRIPT*/

    /*2. Output the format catalog (sas7bcat) */

    libname out "myprojectfolder/output";

    /*2b. Output the format catalog.
            The format catalog is automatically stored in work.formats. This step copies the format file to the 
            out directory as a sas7bcat file.*/
    proc catalog cat=work.FORMATS;
        copy out=out.FORMATS;
        run;
        
    /*3. Output the data file (sas7bdat) to your output folder*/
    data out.yourdata;
        set processed;
        run;

    ```

#### Run the `vlmd` command

After creating the necessary `sas7bdat` and `sas7bcat` files, you can then run the `vlmd` command. Note, the `sas7bcat` files are optional. However, if you don't include, the `encodings` (ie value labels) will not be added.

```bash
vlmd --filepath input/data.sas7bdat --sas7bcat-filepath input/formats.sas7bcat --inputtype sas7bdat
```


### SPSS `.sav` files

For SPSS users, HEAL data utilities generates heal-compliant data dictioanries from SPSS's default file format for storing datasets: A `SAV` file. It not only stores the data itself but also stores metadata such as variable names, variable labels, types, and value labels. The HEAL data utilities extracts the data and metadata to create heal-compliant data dictionaries.


<!-- ### Creating a well-annotated `sav` file

TO ADD -->

#### Run the `vlmd` command
```bash
vlmd --filepath data/example_pyreadstat_output.sav --inputtype sav
```
### Stata `.dta` files

For Stata users, HEAL data utilities generates heal-compliant data dictionaries through Stata's default file format: the `DTA` files. `DTA` files not only store the data itself but also stores metadata such as variable names, variable labels, types, and value labels.

<!-- ### Creating a well-annotated `dta` file

TO ADD -->
#### Run the `vlmd` command
```bash
vlmd --filepath data/example_pyreadstat_output.dta --inputtype dta
```
### `csv` Datasets

[TODO]

### `csv` HEAL data dictionary (e.g., from template)

[TODO]
### `json` HEAL data dictionary (e.g., from template)
[TODO]