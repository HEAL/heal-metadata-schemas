""" 
script to compile data dictionaries from
yaml definitions


""" 


# flatten json schema using flatten_if function
import yaml 
from pathlib import Path
import os
import re
import copy
from collections.abc import MutableMapping,MutableSequence,MutableSet
from functools import reduce
from frictionless import Schema
os.chdir(Path(__file__).parent)

# load yaml
def load_yaml(filepath):
    with open(filepath) as f:
        yamlfile = yaml.safe_load(f)

    return yamlfile

# load all yamls
def load_all_yamls(directory="schemas/dictionary"):
    filepaths = Path(directory).glob("*.yaml")
    return {filepath.stem:load_yaml(filepath) for filepath in filepaths}
    
def select_specs(items,schema,specname="_csvSpec"):
    """ 
    select all items with the key specname and delete
    all other items that have keys with regular expression
    that starts with underscore and ends with word Spec.

    This function is useful when building multiple versions of schemas
    conditional on the type of specificaiton (eg csv tabular data vs. json 
    for a workflow that may except csv that is translated into the json file.)

    """ 
    assert isinstance(schema,MutableMapping),"schema must be dictionary-like"
    #loop through schema
    schema_selected = {}
    for key,item in items.items():
        if key==specname:
            spec = item
            schema_selected.update(spec)
        elif re.search("^_.*Spec$",key):
            pass 
        elif isinstance(item,MutableMapping):
            schema_selected[key] = select_specs(item,schema,specname)
        else: 
            schema_selected[key] = item
    return schema_selected

# resolve refs (and select type of schema spec)
def resolve_refs(items,schema,parentkey=False):
    """
    resolve pseudo-json references

    item is the item to be iterated through
    and schema is the overall schema to reference

    NOTE: these are pseudo as $ref is used simply for replacement of 
    any value (ie $ref doesnt have to be )
    JSON references: https://datatracker.ietf.org/doc/html/draft-pbryan-zyp-json-ref-03
    """

    schema_resolved = {}
    for key,item in items.items():
        #resolve refs
        if key=="$ref":
            path = item.split("/")
            anchor = path.pop(0)
            if anchor=="#":
                get_item = lambda _item,key: _item.get(key,{})
                _resolved = reduce(get_item,path,schema)
                resolved = resolve_refs(_resolved,schema)
                schema_resolved.update(resolved)

        #resursively call and map to output schema
        elif isinstance(item,MutableMapping):
            schema_resolved[key] = resolve_refs(item,schema)
        elif isinstance(item,(MutableSequence,MutableSet)):
            resolveditem = []
            for val in item:
                if isinstance(val,MutableMapping):
                    _resolved = resolve_refs(val,schema)
                else:
                    _resolved = val
                resolveditem.append(_resolved)
            
            schema_resolved[key] = resolveditem
        else:
            schema_resolved[key] = item

    return schema_resolved


def flatten(items,schema,parentkey="",sep="."):
    """ 
    flatten schema in place
    """ 
    schema_flattened = {}
    for key,item in items.items():

        # flattened keys
        if parentkey:
            flattenedkey = parentkey+"."+key
        else:
            flattenedkey = key
        
        
        if isinstance(item,MutableMapping):
            props = item.get('properties')
            if props:
                schema_flattened.update(flatten(
                    props,schema,parentkey=flattenedkey))
            else:
                schema_flattened[flattenedkey] = item
        else:
            schema_flattened[flattenedkey] = item

    return schema_flattened

class JsonSchema:
    def __init__(self,schema):
        self.schema = copy.deepcopy(schema)
    
    def flatten(self):
        self.schema['properties'] = flatten(self.schema['properties'],self.schema)
        return self

    def select_specs(self):
        self.schema = select_specs(self.schema,self.schema)
        return self
    
    def resolve_refs(self):
        self.schema = resolve_refs(self.schema,self.schema)
        return self
    
    def select_properties(self,jsonpath):
        path = jsonpath.split("/")
        get_item = lambda item,key: item.get(key,{})
        self.schema = reduce(get_item,path,self.schema)
        return self

    def _to_frictionless_field(self,propname,prop):

        get_anyof = lambda propname: [_prop.get(propname) for _prop in prop.get("oneOf",[])]
        
        # anyof is convenient way to reference multiple enum lists of same type
        anyof = {
            'type':[t for t in get_anyof('type') if t],
            'enum':[val for enumlist in get_anyof('enum') for val in enumlist],
        }
        
        jsonfields = {
            'name':propname,
            'description':prop.get('description'),
            'title':prop.get('title'),
            'examples':prop.get('examples'),
            'type':list(set(anyof.get('type',[])+[p for p in [prop.get('type')] if p])),
            'enum':list(set(anyof.get('enum',[])+prop.get('enum',[]))),
            'pattern':prop.get('pattern'),
        }

        constraintfields = ['enum','pattern']
        targetfield = {}

        for propname,prop in jsonfields.items():
            if propname=='type' :
                targetfield[propname] = prop[0] if len(prop)==1 else 'any'
            elif propname in constraintfields and prop:
                if targetfield.get('constraint'):
                    targetfield['constraint'][propname] = prop
                else:
                    targetfield['constraint'] = {propname:prop}
            elif prop:
                targetfield[propname] = prop

        return targetfield

    def to_frictionless(self):
        
        assert self.schema['type']=='object'
        assert 'properties' in self.schema

        frictionless = Schema()
        for propname in ['description','title','name','examples']:
            if self.schema.get(propname):
                frictionless[propname] = self.schema[propname]
        # get fields subschema
        fields = self.schema['properties']
        frictionlessfields = []
        for name,field in fields.items():
            assert isinstance(field,MutableMapping),"all field properties must be jsons"
            frictionlessfields.append(self._to_frictionless_field(name,field))

        frictionless['fields'] = frictionlessfields
        self.frictionless_schema = frictionless
        return self

csvfields = (
    JsonSchema(load_all_yamls())
    .select_specs()
    .resolve_refs()
    .select_properties(jsonpath="fields")
    .flatten()
    .to_frictionless()
)
csvfields.frictionless_schema.to_json("schemas/frictionless/csvtemplate.json")
# schema = {
#     "type": "object",
#     "properties": {
#         "foo": {"$ref": "#/definitions/footest"},
#         "foo2": [{"$ref": "#/definitions/footest"}],
#     },
#     "definitions": {
#         "footest": {
#             "type": "string"
#         }
#     }
# }

# test = resolve_refs(schema,schema)

# test = {
#   "type": "object",
#   "properties": {
#     "name": {
#       "type": "string",
#       "enum": [
#         "Sally",
#         "Ann"
#       ]
#     }
#   }
# }