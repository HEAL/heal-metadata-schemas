# Variable level metadata

This metadata directory contains the specifications for variable level metadata submissions to the 
HEAL platform in addition to variable level metadata templates in TSV format and the associated code
converting this template to its validated json format.

## Directories

- `docs`: (a little unconventional) documents and other materials to understand VLMD materials in this repo.
- `schemas/jsonschema`: the JSONschemas specifying variable level metadata. As a data dictionary most likely contains multiple variables, a data dictionary is specified as an array (list) of properties(`data_dictionary.json`) that describe a set of variables (`fields.json` and referenced in the data_dictionary.json). 
- `schemas/frictionless`: contains schemas following the frictionless schema specifications. `fields.json` contains the frictionless Table Schema descriptor that validates a tabular heal templated csv data dictionary. See [here](https://specs.frictionlessdata.io/table-schema/) for the specification
- `schemas/dictionary`: the yaml files used to generate json schemas with build.py. Currently, some steps are non-standard such as using _jsonSpec and _csvSpec keys to indicate which property to extract. In the  future,
it may be worth (1) implementing if/else/then in schemas and (2) modifying csv template such that all fields
are completely flattened (eg instead of having ontology_id entry as is=SOURCE=ID, this would be three separate fields -- this would make it easier to go between json and csv.
- `schemas
- `templates`: the (filled out) templates in TSV spreadsheet format and JSON format. 
- `build.py`: **Work in progress** this script compiles the yaml files and generates associated jsonschemas and frictionless schemas.


## Other sources of materials for variable level metadata

See [this google doc](https://docs.google.com/document/d/1-n7XZayEkj1k7QBwqgqXzAJYCBbEz2fpNqVtuisI2-Y/edit?usp=sharing) to illustrate the resources used to make decisions and 
next steps 


## Considerations

Please use github issues for any additional considerations. See additional comments above.