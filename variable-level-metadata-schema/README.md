# Variable level metadata

This metadata directory contains the specifications for variable level metadata documents in the HEAL data ecosystem. 

## Schemas
There are three categories of schemas important in this directory:

### json data dictionary format specification
1. `schemas/jsonschema/data-dictionary.json`: The "json" json data dictionary schema (ie json template schema)
    - Intended to specify the data dictionary representation of json objects available in the HEAL platform metadata-service.

### csv field format specifications

2. `schemas/frictionless/fields.json` Table schema (previously known as "frictionless") standard specification
    - This json file is intended to represent csv data dictionary documents following the [Table Schema specification](https://specs.frictionlessdata.io/table-schema/).
    - Csv version is intended to make data dictionary creation and discovery available in a more familiar/human readable format,
    - The representation of data dictionary field values in a csv file. It's used to facilitate documentation of data dictionary csv 
    files in addition to input validation. 
3. `schemas/jsontemplate/fields.json`The "csv" json schema (ie csv template schema)
    - :warning: The "csv" json schema is intended to be an intermediate specification used for documentation and in translation workflows to the json schema template. As fully specifying a tabular file (for example missing value specification) is out of scope here (see the table schema representation in (2))

## Workflow

The `schemas/dictionary` directory contains a comprehensive json schema with fields for 



## Directories

- `docs`: 
See the rendered human readable schemas
in a markdown format and an interactive html format.
- `schemas/jsonschema`: contains the final and full specification.
- `schemas/frictionless`: contains schemas following the frictionless schema specifications. `fields.json` contains the frictionless Table Schema descriptor that validates a tabular heal templated csv data dictionary. See [here](https://specs.frictionlessdata.io/table-schema/) for the specification. **NOTE: the `csvtemplate` is an intermediate format meant to be converted into the final `jsontemplate` format.
- `schemas/dictionary`: the yaml files used to generate json schemas and documentation with build.py. 
- `templates`: empty templates in csv spreadsheet format and JSON format. 
- `examples`: exapmles of filled out templates in csv spreadsheet format and JSON format.
 TO BE ADDED: for now, see https://github.com/norc-heal/healdata-utils/tree/main/tests/data/valid/output
- `build.py`: This script compiles the yaml files and generates associated jsonschemas and frictionless schemas in addition to the human rendered schemas

## Contributing

To contribute to the variable level metadata specification (and annotations/examples/documentation), please modify the `dictionary/*.yaml` files directly.

❗ Please read the below conventions and principles before contributing and review the existing `dictionary` directory.


## Conventions, principles, and rules

### Annotation/documentation properties
1. `description`: SHOULD be created as markdown syntax without any headers as headers are applied in the templates.

2. `additionalDescription`: SHOULD be added if there are additional documentation "footer" details. In rendering the documentation, these are appended to the end of rendered markdown document.

### `type` conversion rules 
Given csv field values can only be scalar values with records separated by a new line and each individual field values separated by a comma delimiter, the following rules and restrictions are applied to allow json to csv specification translation.

1. type `object`
    - converted to type `string` with pattern of `^(?:.*?=.*?(?:\||$))+$` to indicate a stringified object with a equal sign (`=`) connecting the key-value pair and a pipe (`|`) delimiter separating unique key-value pairs.
2. type `array`
    - if type `object` in `items`: flattened to the children property or properties
    - if type is a scalar (`string`,`integer`,`number`) in `items`,
     translated to type `string` with pattern `^(?:[^|]+\||[^|]*)(?:[^|]*\|)*[^|]*$` to indicate a string containing a pipe delimiter (i.e., a stringified array with a pipe delimiter)

### Complex `type` restrictions 

1. Currently, no complex types (`anyOf`,`oneOf`) and the `type` MUST be specified.
2. `enum` restrictions
    - following from (1), an `enum` must only contain values of the same type
    - (at least currently) MUST contain only scalar types (`string`,`integer`,`number`)


## Considerations

Please use github issues for any additional considerations. See additional comments above.