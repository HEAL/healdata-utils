# `csv` (Minimal) Data Dictionary


Convert a minimal data dictionary in a csv (or tsv file). For example, may have `name`, `type`, and description and then this adds the rest of the fields. Additionally:

- Converts a few common data types (such as char, character,text to 'string' and 'float' to 'number'.)

- Converts common property names onto the HEAL specification property names (e.g., `Field name`, `variable name`, or `Names` map onto `name`; `Data type`, `data-types`, `FIELD TYPE`, `Variable types` map onto `type` )

## Run the `vlmd` command

=== "CLI"

```bash
vlmd extract --inputtype csv-data-dict data/minimal-csv-dd.csv
```