""" 
script to generate jsonschema and frictionless schemas
 from yaml definitions
"""
import yaml
from pathlib import Path
import os
import re
import json
import copy
from collections.abc import MutableMapping, MutableSequence, MutableSet,Sequence
from functools import reduce
import jsonschema
import jinja2 
import json

os.chdir(Path(__file__).parent)

versions = json.loads(Path("../VERSIONS.json").read_text())
# load yaml
def load_yaml(filepath):
    with open(filepath) as f:
        yamlfile = yaml.safe_load(f)

    return yamlfile
# load all yamls
def load_all_yamls(directory="schemas/dictionary"):
    filepaths = Path(directory).glob("*.yaml")
    return {filepath.stem: load_yaml(filepath) for filepath in filepaths}

def resolve_refs(items, schema, parentkey=False):
    """
    resolve pseudo-json references

    item is the item to be iterated through
    and schema is the overall schema to reference

    NOTE: these are pseudo as $ref is used simply for replacement of
    any value (ie $ref doesnt have to be )
    JSON references: https://datatracker.ietf.org/doc/html/draft-pbryan-zyp-json-ref-03
    """

    schema_resolved = {}
    for key, item in items.items():
        # resolve refs
        if key == "$ref":
            path = item.split("/")
            anchor = path.pop(0)
            if anchor == "#":
                get_item = lambda _item, key: _item.get(key, {})
                _resolved = reduce(get_item, path, schema)
                resolved = resolve_refs(_resolved, schema)
                schema_resolved.update(resolved)

        # resursively call and map to output schema
        elif isinstance(item, MutableMapping):
            schema_resolved[key] = resolve_refs(item, schema)
        elif isinstance(item, (MutableSequence, MutableSet)):
            resolveditem = []
            for val in item:
                if isinstance(val, MutableMapping):
                    _resolved = resolve_refs(val, schema)
                else:
                    _resolved = val
                resolveditem.append(_resolved)

            schema_resolved[key] = resolveditem
        else:
            schema_resolved[key] = item

    return schema_resolved

def to_csv_properties(schema,**additional_props):
    """
    translate complex types (eg arrays and objects) to stringified representations
    """
    csv_schema = dict(schema)
    csv_schema["properties"] = {}
    properties = schema["properties"]
    for key, item in properties.items():
        typename = item.get("type")
        newitem = dict(item)
        if typename == "array":
            newitem["type"] = "string"
            newitem["pattern"] = "^(?:[^|]+\||[^|]*)(?:[^|]*\|)*[^|]*$"

            if item.get("examples"):
                newitem["examples"] = ["|".join(str(_e) for _e in e) for e in item["examples"]]
        elif typename == "object":
            newitem["type"] = "string"
            newitem["pattern"] = "^(?:.*?=.*?(?:\||$))+$"

            if item.get("examples"):
                newitem["examples"] = [
                    "|".join([f"{key}={val}" for key,val in e.items()])
                     for e in item["examples"]
                ]
        elif typename in ["string","integer","number","boolean"]:
            newitem = dict(item)
        else:
            raise Exception("To convert to csv, the flattened property needs to be",
                "of type array,object,boolean,string, integer, or number")
        
        csv_schema["properties"][key] = newitem
    
    # add additional properties at the beginning of the schema properties object
    csv_schema["properties"] = {**additional_props,**csv_schema["properties"]}

    return csv_schema

def flatten_properties(properties, parentkey="", sep=".",itemsep="[\d+]"):
    """
    flatten schema properties
    """
    properties_flattened = {}
    for key, item in properties.items():
        # flattened keys
        if parentkey:
            flattenedkey = parentkey + "." + key
        else:
            flattenedkey = key

        if isinstance(item, MutableMapping):
            props = item.get("properties")
            items = item.get("items",{}).get("properties")
            if props:
                newprops = flatten_properties(props, parentkey=flattenedkey)
                properties_flattened.update(newprops)

            elif items:
                newprops = flatten_properties(items,parentkey=flattenedkey+itemsep)
                properties_flattened.update(newprops)
            else:
                properties_flattened[flattenedkey] = item
        
        else:
            properties_flattened[flattenedkey] = item
    
    return properties_flattened

def flatten_schema(schema):
    schema_flattened = dict(schema)
    if "properties" in schema:
        properties = schema_flattened.pop("properties")
        schema_flattened["properties"] = flatten_properties(properties,itemsep="[\d+]")
        schema_flattened["patternProperties"] = {}
        for propname in list(schema_flattened["properties"].keys()):
            if "[\d+]" in propname:
                var0 = propname.replace("[\d+]","[0]")
                var1 = propname.replace("[\d+]","[1]")
                var2 = propname.replace("[\d+]","[2]")
                pattern_property_note = (
                    "\n\n"
                    "Specifying field names:\n\n"
                        "\tThis field can have 1 or more columns using the digit index number in brackets (`[0]` --> `[1]` --> `[n]`)\n\n"
                        "\tFor 1 value, you will have the columns: "
                        "`{0}`\n"
                        # "\tFor 2 values, you will have the columns: "
                        # "`{0},`{1}`\n"
                        "\tFor 3 values, you will have the columns:"
                        "`{0},`{1}, `{2}`\n\n"
                ).format(var0,var1,var2)
                pattern_prop = schema_flattened["properties"].pop(propname)
                pattern_prop["description"] = pattern_prop.get("description","") + pattern_property_note
                schema_flattened["patternProperties"]["^"+propname+"$"] = pattern_prop

    return schema_flattened

def run_pipeline_step(input, step):
    """function for input into the reduce functool
    function where the input is the instance and fxn is
    a tuple of either length 1 if only param is input
    and greater than eq 1 if there are additional paramters to fxn
    with dict of parameters second item in tuple
    """
    step = [_step for _step in step if _step]
    fxn = step[0]
    if len(step) > 1:
        params = step[1]
        return fxn(input, **params)
    elif len(step) == 1:
        return fxn(input)
    else:
        raise Exception("Step must be at least of length 1")

def render_markdown(item,schema,templatefile):

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader("docs/assets/templates"),
        trim_blocks=True,
        lstrip_blocks=True
    )

    template = env.get_template(templatefile)
    output = template.render(item=item,schema=schema)
    return output


def generate_template(schema):
    template = {}
    schema = dict(schema)
    if 'patternProperties' in schema:
        schema["properties"] = schema.get("properties",{})
        for patternname,prop in schema["patternProperties"].items():
            propname = (
                patternname
                .replace("^","")
                .replace("$","")
                .replace("[\d+]","[0]")
            )
            schema["properties"][propname] = prop
    if 'properties' in schema:
        for prop, prop_schema in schema['properties'].items():
            if 'type' in prop_schema:
                if prop_schema['type'] == 'object':
                    template[prop] = generate_template(prop_schema)
                elif prop_schema['type'] == 'array':
                    if prop_schema.get("items"):
                        template[prop] = [generate_template(prop_schema['items'])]
                    else:
                        template[prop] = []
                else:
                    template[prop] = None
            elif '$ref' in prop_schema:
                ref_schema = get_referenced_schema(prop_schema['$ref'])
                template[prop] = generate_template(ref_schema)
    return template
    
if __name__ == "__main__":
    # compile frictionless schema fields
    dictionary = load_all_yamls()

    # compile json schema fields
    json_pipeline = [
        # recursive fxn so need to grab items from overall dictionary for json paths
        (resolve_refs, {"schema": dictionary}),
        # no longer need the definitons as they have been resolved
        (lambda _schema: _schema["data-dictionary"], None),
        (lambda _schema: {"version":versions["vlmd"],**_schema},None)
    ]
    json_data_dictionary = reduce(run_pipeline_step, json_pipeline, dictionary)
    Path("schemas/data-dictionary.json").write_text(json.dumps(json_data_dictionary, indent=4))

    schema_version_prop = {"schemaVersion":json_data_dictionary["properties"]["schemaVersion"]}
    # compile json schema fields
    csv_pipeline = [
        # recursive fxn so need to grab items from overall dictionary for json paths
        (resolve_refs, {"schema": dictionary}),
        # no longer need the definitons as they have been resolved
        (lambda _schema: _schema["fields"], None),  
        (flatten_schema, None),
        (to_csv_properties,schema_version_prop),
        (lambda _schema: {"version":versions["vlmd"],**_schema},None)
    ]
    csvfields = reduce(run_pipeline_step, csv_pipeline, dictionary)
    Path("schemas/csvtemplate/fields.json").write_text(json.dumps(csvfields, indent=4))

    # render and write markdown versions
    csvfields_md = render_markdown(
        item=csvfields,
        schema=csvfields,
        templatefile="csvtemplate.md")
    json_dd_md = render_markdown(
        item=json_data_dictionary,
        schema=json_data_dictionary,
        templatefile="jsontemplate.md"
    )
    Path("docs/csvtemplate-fields.md").write_text(csvfields_md)
    Path("docs/jsontemplate-data-dictionary.md").write_text(json_dd_md)

    # generate templates
    Path("templates/template_submission.json").write_text(json.dumps([generate_template(json_data_dictionary)],indent=4))
    Path("templates/template_submission.csv").write_text(",".join((generate_template(csvfields)).keys()))