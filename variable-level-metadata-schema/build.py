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
from json_schema_for_humans.generate import generate_from_filename
import jinja2 
import json

os.chdir(Path(__file__).parent)

versions = json.loads(Path("../VERSIONS.json").read_text())
# load yaml
def load_yaml(filepath):
    with open(filepath) as f:
        yamlfile = yaml.safe_load(f)

    return yamlfile

test = load_yaml("schemas/dictionary/definitions.yaml")
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

def flatten_properties(properties, parentkey="", sep=".",itemsep="[0]"):
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
    properties = schema.get("properties")
    if properties:
        schema_flattened["properties"] = flatten_properties(properties)
    return schema_flattened

def _to_frictionless_field(propname, prop, schema):
    get_anyof = lambda propname: [
        _prop.get(propname) for _prop in prop.get("oneOf", [])
    ]

    # anyof is convenient way to reference multiple enum lists of same type
    anyof = {
        "type": [t for t in get_anyof("type") if t],
        "enum": [val for enumlist in get_anyof("enum") for val in enumlist],
    }
    jsonfields = {
        "name": propname,
        "description": prop.get("description"),
        "title": prop.get("title"),
        "examples": prop.get("examples"),
        "type": list(set(anyof.get("type", []) + [p for p in [prop.get("type")] if p])),
        "enum": list(set(anyof.get("enum", []) + prop.get("enum", []))),
        "pattern": prop.get("pattern"),
    }
    # add required
    if propname in schema.get("required", []):
        jsonfields["required"] = True

    constraintfields = ["enum", "pattern", "required"]
    targetfield = {}

    for propname, prop in jsonfields.items():
        if propname == "type":
            targetfield[propname] = prop[0] if len(prop) == 1 else "any"
        elif propname in constraintfields and prop:
            if targetfield.get("constraints"):
                targetfield["constraints"][propname] = prop
            else:
                targetfield["constraints"] = {propname: prop}
        elif prop:
            targetfield[propname] = prop

    return targetfield


def to_frictionless(schema):
    assert schema["type"] == "object"
    assert "properties" in schema

    frictionless_schema = {}

    # schema level annotations
    for propname in ["description", "title", "name", "examples"]:
        if schema.get(propname):
            frictionless_schema[propname] = schema[propname]

    # get fields subschema
    fields = schema["properties"]
    frictionless_fields = []
    for name, field in fields.items():
        assert isinstance(field, MutableMapping), "all field properties must be jsons"
        frictionless_fields.append(_to_frictionless_field(name, field, schema))

    frictionless_schema["fields"] = frictionless_fields
    frictionless_schema["missingValues"] = [
        ""
    ]  # TODO: have a way to specify if anyOf is a missing val
    return frictionless_schema


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
    Path("schemas/jsonschema/data-dictionary.json").write_text(json.dumps(json_data_dictionary, indent=4))

    schema_version_prop = {"schemaVersion":json_data_dictionary["properties"]["schemaVersion"]}
    csv_pipeline = [
        # recursive fxn so need to grab items from overall dictionary for json paths
        (resolve_refs, {"schema": dictionary}),
        # no longer need the definitons as they have been resolved
        (lambda _schema: _schema["fields"], None),        
        (flatten_schema, None),
        (to_csv_properties,schema_version_prop),
        (to_frictionless, None),
        (lambda _schema: {"version":versions["vlmd"],**_schema},None)
    ]
    frictionlessfields = reduce(run_pipeline_step, csv_pipeline, dictionary)
    Path("schemas/frictionless/csvtemplate/fields.json").write_text(
        json.dumps(frictionlessfields, indent=2)
    )
    

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
    Path("schemas/jsonschema/csvtemplate/fields.json").write_text(json.dumps(csvfields, indent=4))

    # generate json schema versions of field schemas for documentation 

    # generate html using the json-schema for human library
    generate_from_filename("schemas/jsonschema/csvtemplate/fields.json",
        "docs/html-rendered-schemas/jsonschema-csvtemplate-fields.html")
    generate_from_filename("schemas/jsonschema/data-dictionary.json",
        "docs/html-rendered-schemas/jsonschema-jsontemplate-data-dictionary.html")

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
    Path("docs/md-rendered-schemas/jsonschema-csvtemplate-fields.md").write_text(csvfields_md)
    Path("docs/md-rendered-schemas/jsonschema-jsontemplate-data-dictionary.md").write_text(json_dd_md)

    # generate templates
    Path("templates/template_submission.json").write_text(json.dumps([generate_template(json_data_dictionary)],indent=4))
    Path("templates/template_submission.csv").write_text(",".join((generate_template(csvfields)).keys()))