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
from collections.abc import MutableMapping, MutableSequence, MutableSet
from functools import reduce


os.chdir(Path(__file__).parent)


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


def select_specs(schema, specsuffix="CsvSpec"):
    """
    select given specification type and remove other specification types.
    These are denoted with the suffix <specsuffix> (eg encodingsCsvSpec) in property name

    This function is useful when building multiple versions of schemas
    conditional on the type of specificaiton (eg csv tabular data vs. json
    for a workflow that may except csv that is translated into the json file.)

    """
    # loop through schema
    schema_selected = {}
    for key, item in schema.items():
        if re.search(f"{specsuffix}$", key):
            newkey = key.replace(specsuffix, "")
            schema_selected[newkey] = item
        elif re.search("Spec$", key):
            pass
        elif isinstance(item, MutableMapping):
            schema_selected[key] = select_specs(item, specsuffix)
        else:
            schema_selected[key] = item
    return schema_selected


# resolve refs (and select type of schema spec)

def get_ref(path,schema):
    pass 

# loop through all iterables in a dictionary 
# if key = $ref --> get_ref



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


def flatten_properties(properties, parentkey="", sep="."):
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
            if props:
                newprops = flatten_properties(props, parentkey=flattenedkey)
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


if __name__ == "__main__":
    # compile frictionless schema fields
    dictionary = load_all_yamls()
    csv_pipeline = [
        (select_specs, {"specsuffix": "CsvSpec"}),
        # recursive fxn so need to grab items from overall dictionary for json paths
        (resolve_refs, {"schema": dictionary}),
        # no longer need the definitons as they have been resolved
        (lambda _schema: _schema["fields"], None),        
        (flatten_schema, None),
        (to_frictionless, None),
    ]
    csvfields = reduce(run_pipeline_step, csv_pipeline, dictionary)
    Path("schemas/frictionless/csvtemplate/fields.json").write_text(
        json.dumps(csvfields, indent=2)
    )

    # compile json schema fields
    json_pipeline = [
        (select_specs, {"specsuffix": "JsonSpec"}),
        # recursive fxn so need to grab items from overall dictionary for json paths
        (resolve_refs, {"schema": dictionary}),
        # no longer need the definitons as they have been resolved
        (lambda _schema: _schema["fields"], None),
    ]
    jsonfields = reduce(run_pipeline_step, json_pipeline, dictionary)
    Path("schemas/jsonschema/fields.json").write_text(json.dumps(jsonfields, indent=4))
