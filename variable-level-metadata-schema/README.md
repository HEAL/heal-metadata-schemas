# Variable level metadata

This metadata directory contains the specifications for variable level metadata documents. 


## Workflow

The `schemas/dictionary` directory contains a comprehensive json schema with fields for 

## Directories

- `docs`: 
See the rendered human readable schemas
in a markdown format and an interactive html format.
- `schemas/jsonschema`: `data_dictionary.json` contains the final and full specification.
- `schemas/frictionless/csvtemplate`: contains schemas following the frictionless schema specifications. `fields.json` contains the frictionless Table Schema descriptor that validates a tabular heal templated csv data dictionary. See [here](https://specs.frictionlessdata.io/table-schema/) for the specification. **NOTE: the `csvtemplate` is an intermediate format meant to be converted into the final `jsontemplate` format.
- `schemas/dictionary`: the yaml files used to generate json schemas with build.py. Fields with `jsonSpec` and `csvSpec` keys to indicate which property to extract in the `build.py` script. 
- `templates`: empty templates in csv spreadsheet format and JSON format. 
- `examples`: the ~~(filled out)~~ templates in csv spreadsheet format and JSON format.
 TO BE ADDED: for now, see https://github.com/norc-heal/healdata-utils/tree/main/tests/data/valid/output
- `build.py`: This script compiles the yaml files and generates associated jsonschemas and frictionless schemas in addition to the human rendered schemas

## Contributing

To contribute to the variable level metadata, please modify the `dictionary/*.yaml` files directly. For example, if you want to add/modify an example, description, etc for either the JSON or CSV spec, then do so here. 


## Considerations

Please use github issues for any additional considerations. See additional comments above.

:::warning

    This is a warning admonition.

:::