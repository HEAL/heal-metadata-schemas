# Variable level metadata

This metadata directory contains the specifications for variable level metadata submissions to the 
HEAL platform in addition to variable level metadata templates in CSV format and the associated code
converting this template to its validated json format.


## Workflow

The `schemas/dictionary` directory contains a comprehensive json schema with fields for 

## Directories

- `docs`: 
See the rendered human readable schemas
in a markdown format and an interactive html format.
- `schemas/jsonschema`: the JSONschemas specifying variable level metadata. As a data dictionary most likely contains multiple variables, a data dictionary is specified as an array (list) of properties(`data_dictionary.json`) that describe a set of variables (`fields.json` and referenced in the data_dictionary.json). 
- `schemas/frictionless/csvtemplate`: contains schemas following the frictionless schema specifications. `fields.json` contains the frictionless Table Schema descriptor that validates a tabular heal templated csv data dictionary. See [here](https://specs.frictionlessdata.io/table-schema/) for the specification
- `schemas/dictionary`: the yaml files used to generate json schemas with build.py. Fields with `jsonSpec` and `csvSpec` keys to indicate which property to extract in the `build.py` script. 
- `templates`: the ~~(filled out)~~ templates in csv spreadsheet format and JSON format. 
- `build.py`: This script compiles the yaml files and generates associated jsonschemas and frictionless schemas.

## Contributing

To contribute to the variable level metadata, please modify the `dictionary/*.yaml` files directly. For example, if you want to add/modify an example, description, etc for either the JSON or CSV spec, then do so here. 


## Considerations

Please use github issues for any additional considerations. See additional comments above.