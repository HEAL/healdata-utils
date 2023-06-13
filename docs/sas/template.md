# SAS template code

This script can be run separately or inserted directly at the end of a SAS user's workflow.

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