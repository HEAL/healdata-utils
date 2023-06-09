# SAS template code

Template code to produce a sas7bdat file and a sas7bcat file.

A sas7bdat file is XXXX

A sas7bcat file is XXXX


```sas


/*1. Read in data file without value labels and run full code. 
		Note: The most important pieces to run here are the PROC FORMAT statement(s) and any data steps 
		that assign formats and variable labels which are needed for the data dictionary*/

%INCLUDE "&base_dir/&year/tmp/&proc"; *Should we include this as where they would put in their file name?;

/*2. Output the format catalog (sas7bcat) */
/*2a. If you do not have an out directory, assign one to output the SAS catalog and data file - maybe this 
		should be at the very top?*/
libname out "P:/3652/Common/public_data/samhda-repo/national-mental-health-services-survey/2019";

/*2b. Output the format catalog.
		The format catalog is automatically stored in work.formats. This step copies the format file to the 
		out directory as a sas7bcat file.*/
proc catalog cat=work.FORMATS;
	copy out=out.FORMATS;
	run;
	
/*3. Output the data file (sas7bdat) */
data out.format_2017_data;
	set processed;
	run;

```