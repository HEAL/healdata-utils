# SAS 

Sas7bdat files contain the actual data values (observations/records). The file also includes variable metadata (variable `names` and variable labels/ `descriptions`).

Sas7bcat files contain variable value labels, or `encodings`, that can be mapped onto datasets.


## Create a `sas7bdat` and a `sas7bcat` file

Many SAS users create formats and labels in their current workflows (see [an example here](example.md)). In this section, we provide syntax that can be easily copy-pasted into these existing workflows to create `sas7bdat` and `sas7bcat` files to input easily into the `vlmd` tool.


After creating the necessary `sas7bdat` and `sas7bcat` files, you can then run the `vlmd` command. Note, the `sas7bcat` files are optional. However, if you don't include, the `encodings` (ie value labels) will not be added.

## Run the `vlmd` command

TODO: ADD VLMD COMMAND HERE