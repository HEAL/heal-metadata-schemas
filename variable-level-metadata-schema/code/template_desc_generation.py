import json
from pathlib import Path
import pandas as pd

def flatten_jsonschema(d:dict, parent_key: str = '', sep: str ='.'):
    flat_items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            if v.get('properties'):
                new_item = flatten_jsonschema(v['properties'], new_key, sep=sep).items()
                flat_items.extend(new_item)
            else:
                flat_items.append((new_key, v))
        else:
            flat_items.append((new_key, v))
    return dict(flat_items)
import csv
with open(Path(__file__).parent.parent/'schemas'/'fields.json','r') as f:
    fields = json.load(f)

desc = pd.DataFrame(flatten_jsonschema(fields['properties'])).T
desc.to_csv(Path(__file__).parent.parent/'docs'/'template-descriptions.csv')