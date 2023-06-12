# Example of generating sas7bdat and sas7bcat files

The below SAS syntax is an example of how to use the template within your SAS workflow.

Here we create all of our variable and value labels. This could be within one or multiple sas scripts
but for demonstration purposes, we only use one script. In your existing workflows, these may also include analyses and other PROC calls for data exploration.

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
	-1	="Missing"
	-2	="Logical skip"
	-3	="Don't know"
	-5	="Refused"
	-6	="Not applicable"
	-7	="Multiple responses"
	-9	="Not used in this version";
	
	VALUE PUBLIC
	1='State mental health authority (SMHA)'
	2='Other state government agency or department'
	3='Regional/district authority or county, local, or municipal government'
	4='Tribal government'
	5='Indian Health Service'
	6='Department of Veterans Affairs'
	7='Other'
		-1	="Missing"
		-2	="Logical skip"
		-3	="Don't know"
		-5	="Refused"
		-6	="Not applicable"
		-7	="Multiple responses"
		-9	="Not used in this version";
	
	VALUE FOCUS
	1='Mental health treatment'
	2='Substance abuse treatment'
	3='Mix of mental health and substance abuse treatment (neither is primary)'
	4='General health care'
	5='Other service focus'
		-1	="Missing"
		-2	="Logical skip"
		-3	="Don't know"
		-5	="Refused"
		-6	="Not applicable"
		-7	="Multiple responses"
		-9	="Not used in this version";

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