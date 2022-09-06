# Variable level metadata

This metadata directory contains the specifications for variable level metadata submissions to the 
HEAL platform in addition to variable level metadata templates in TSV format and the associated code
converting this template to its validated json format.

## Directories

- `code`: contains the CSV template to json conversion/validation and generation of the template description. 
- `docs`: (a little unconventional) documents and other materials to understand VLMD materials in this repo.
- `schemas`: the JSONschemas specifying variable level metadata. As a data dictionary most likely contains multiple variables, a data dictionary is specified as an array (list) of properties (`data_dictionary.json`) that describe a set of variables (`fields.json` and referenced in the data_dictionary.json). 
- `templates`: the (filled out) templates in TSV spreadsheet format and JSON format. 