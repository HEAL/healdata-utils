
******************************************************************************************************;
/*DETAILED STEPS AND CODE TO PRODUCE AND OUTPUT THE NECESSARY SAS FILES FOR CREATION OF A DATA DICTIONARY FILE*/
/*1. Set up an out directory for the data and catalog file*/
libname out "P:/3652/Common/public_data/samhda-repo/national-mental-health-services-survey/2017";

/*2. Read in input data */
proc import datafile="P:/3652/Common/public_data/samhda-repo/national-mental-health-services-survey/2017/raw_data/NMHSS_2017_PUF_CSV_SAMPLE.csv"
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
data raw_form;
	set raw;
	
	format YOUNGADULTS TREATPSYCHOTHRPY TREATTRAUMATHRPY YESNO. FOCUS FOCUS. PUBLIC PUBLIC.;
	label YOUNGADULTS="Accepts young adults (aged 18-25 years old) for Tx"
			TREATPSYCHOTHRPY="Facility offers individual psychotherapy"
			TREATTRAUMATHRPY="Facility offers trauma therapy"
			FOCUS="Primary treatment focus of facility"
			PUBLIC="Public agency or department that operates facility";
run;

/*4. Output the data file (as sas7bdat) with variable labels and format mappings applied */
data out.final_data;
	set raw_form;

	run;

/*5. Output format catalog to sas7bcat file*/
/*5A. Confirm that formats are saved in work */
PROC CATALOG CAT=WORK.FORMATS; CONTENTS; QUIT;
PROC FORMAT LIB=WORK FMTLIB; RUN;

/*5B. Output sas7bcat to out directory
	Note: The formats applied above are already saved in work.formats. This steps just copies them to 
	the out library */
proc catalog cat=work.FORMATS;
	copy out=out.FORMATS;
	run;