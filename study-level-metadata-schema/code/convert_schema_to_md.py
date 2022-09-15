
file_to_convert = "clean json"
for_investigators = True

# https://github.com/RalfG/jsonschema2md

import os
import sys
import json
import jsonschema2md

repo_path = r"C:\Users\tentner-andrea\project_repositories\heal-metadata-schemas"

##input_clean_json = r"C:\Users\tentner-andrea\project_repositories\heal-metadata-schemas\study-metadata-schema.json"
##output_clean_md = r"C:\Users\tentner-andrea\project_repositories\heal-metadata-schemas\study-metadata-schema-for-humans.md"
##
##input_cedar_json = r"C:\Users\tentner-andrea\project_repositories\heal-metadata-schemas\study-metadata-schema-cedar-template.json"
##output_cedar_md = r"C:\Users\tentner-andrea\project_repositories\heal-metadata-schemas\study-metadata-schema-cedar-template-for-humans.md"

input_clean_json = os.path.join(repo_path,"study-level-metadata-schema","schema-clean","json","study-metadata-schema.json")
output_clean_md = os.path.join(repo_path,"study-level-metadata-schema","schema-clean","md","study-metadata-schema-for-humans.md")
output_clean_md_2 = os.path.join(repo_path,"for-investigators-how-to","study-level-metadata-fields","study-metadata-schema-for-humans.md")

##input_cedar_json = os.path.join(repo_path,"study-level-cedar-template-metadata-schema","json","study-metadata-schema-cedar-template.json")
##output_cedar_md = os.path.join(repo_path,"study-level-cedar-template-metadata-schema","md","study-metadata-schema-cedar-template-for-humans.md")

if file_to_convert == "clean json":
    input_json = input_clean_json
    output_md = output_clean_md
    output_md_2 = output_clean_md_2
elif file_to_convert == "cedar json":
    input_json = input_cedar_json
    output_md = output_cedar_md
else: 
    raise ValueError("file_to_convert must be one of clean json or cedar json")




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

# if generating for clean json, also add to the 'for-investigators-how-to' folder
if file_to_convert == "clean json" and for_investigators:
    with open(output_md_2,"w") as f:
        sys.stdout = f # change stdout to output md file we created
        print(''.join(md_lines))
        sys.stdout = original_stdout # reset stdout to original value
