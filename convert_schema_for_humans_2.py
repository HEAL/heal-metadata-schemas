
# https://github.com/RalfG/jsonschema2md

import sys
import json
import jsonschema2md

input_json = r"C:\Users\tentner-andrea\project_repositories\heal-metadata-schemas\study-metadata-schema.json"
output_md = r"C:\Users\tentner-andrea\project_repositories\heal-metadata-schemas\study-metadata-schema-for-humans.md"

parser = jsonschema2md.Parser(
    examples_as_yaml=False,
    show_examples="all",
    )

with open(input_json,"r") as json_file:
    md_lines = parser.parse_schema(json.load(json_file))

original_stdout = sys.stdout # save ref to original stdout of print

with open(output_md,"w") as f:
    sys.stdout = f # change stdout to output md file we created
    print(''.join(md_lines))
    sys.stdout = original_stdout # reset stdout to original value
