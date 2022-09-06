''' 
takes the filled out variable level metadata template
and converts to json, validates, and saves json template to file
based on an explicit set of mapping functions


''' 
import jsonschema 
import petl as etl
import yaml
from pathlib import Path
from functools import reduce
import json
# split array columns
def split_str_array(string,sep='|'):
    if string:
        return [s.strip() for s in string.split(sep)]
    else:
        return None

# if object within array, assign to properties
def map_keys_vals(keys,vals):
    ''' zips two lists of the same size as 
    a dictionary
    ''' 
    return dict(zip(keys,vals))

def split_and_map(string,prop):
    ''' 
    splits a stringified delimited list
    and zips/maps to a dictionary with keys of a dictionary
    TODO: rename function split_and_map_to_keys
    '''
    if string:
        return map_keys_vals(prop.keys(),split_str_array(item))
    else:
        return None

def loads_dict(string,item_sep='|',key_val_sep='='):
    if string:
        return dict([split_str_array(s,key_val_sep) 
            for s in split_str_array(string,item_sep)])

def convert_rec_to_json(record):
    ''' 
    converts a flattened dictionary to a nested dictionary
    based on JSON path dot notation indicating nesting
    '''
    record_json = {}
    for prop_path,prop in record.items():
        if prop:
            # initiate the prop to be added with the entire
            # record 
            prop_json = record_json
            # get the inner most dictionary item of the jsonpath
            nested_names = prop_path.split('.')
            for i,prop_name in enumerate(nested_names):
                is_last_nested = i+1==len(nested_names)
                if prop_json.get(prop_name) and not is_last_nested:
                    prop_json = prop_json[prop_name]
                # if no object currently 
                elif not is_last_nested:
                    prop_json[prop_name] = {}
                    prop_json = prop_json[prop_name]
                #assign property to inner most item
                else:
                    prop_json[prop_name] = prop

    return record_json

# def make_mapping_func(prop_name,schema):
#     ''' 
#     get nested prop and assign a lambda function 

# NOTE: originally tried to do mappings programmetically,
# but pivotted to explicit mappings (harder to do in PETL than pandas as I couldnt
# figure out how to reference header names within a convert function to call the schema)
#     ''' 
#     keys = prop_name.split('.')
#     prop = reduce(lambda acc,i: acc[i], keys, schema)
    
#     if prop['type']=='array':
#         func = lambda v: split_str_array(v)

#     elif prop['type']=='object':
#         if prop.get('properties'):
#             func = lambda v: map_keys_vals(prop.keys(),split_str_array(v,sep='='))
#         else:
#             func = lambda v: split_str_array(v,sep='=')



schema_path = Path(__file__).parent.parent/'schemas'/"fields.json"
tsv_path = Path(__file__).parent.parent/"templates"/"template_submission.tsv"
# read in schema
with open(schema_path) as f:
    schema = yaml.safe_load(f)

props = schema['properties']

#mappings for array of dicts, arrays, and dicts
mappings = {
    'constraints.enum': lambda v: split_str_array(v),
    'cde_id': lambda v: split_and_map(v, props['cde_id']),
    'ontology_id': lambda v: split_and_map(v, props['ontology_id']),
    'encoding':lambda v: loads_dict(v),
    #'univar_stats.cat_marginals':lambda v: split_and_map(v, prop['univar_stats']['cat_marginals']),
    'missingValues':lambda v: split_and_map(v, props['missingValues']),
    'trueValues': lambda v: split_and_map(v, props['trueValues']),
    'falseValues':lambda v: split_and_map(v, props['falseValues']),
    # TODO: add stats
}

# loop through empty json output and assign mapping type
# read in csv
template_tbl = (
    etl.fromtsv(tsv_path)
    .convert(mappings)
    .convertnumbers()
)       
data_dictionary = [convert_rec_to_json(rec) for rec in etl.dicts(template_tbl)]
template_json = data_dictionary
# TODO: use jsonschema resolver and data_dictionary.json
jsonschema.validate(template_json,schema={'type':'array','items':schema})

with open(Path(__file__).parent.parent/'templates'/'template_submission.json','w') as f:
    json.dump(template_json,f,indent=4)