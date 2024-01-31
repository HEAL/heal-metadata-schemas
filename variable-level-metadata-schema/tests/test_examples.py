import jsonschema
from pathlib import Path
import os
import json
import pandas as pd

VLMD_PATH = "variable-level-metadata-schema"
CSV_SCHEMA_PATH = Path(VLMD_PATH)/"schemas/csvtemplate/fields.json"
JSON_SCHEMA_PATH = Path(VLMD_PATH)/"schemas/data-dictionary.json"
VLMD_EXAMPLE_PATH = Path(VLMD_PATH)/"examples"

json_schema = json.loads(JSON_SCHEMA_PATH.read_text())
csv_schema = {"type":"array","items":json.loads(CSV_SCHEMA_PATH.read_text())}

def validate_against_jsonschema(json_object,schema):
    print(os.listdir())
    Validator = jsonschema.validators.validator_for(schema)
    validator = Validator(schema)
    report = []
    is_valid = True
    for error in validator.iter_errors(json_object):
        is_valid = False
        error_report = {
            "json_path":error.json_path,
            "message":error.message,
            "absolute_path":list(error.path),
            "relative_path":list(error.relative_path),
            "validator":error.validator,
            "validator_value":error.validator_value
        }
        report.append(error_report)

    return {"valid":is_valid,"errors":report}

def to_summary(filepath:Path):
    print("Testing:")
    print(str(filepath))
    if filepath.suffix == ".json":
        instance = json.loads(filepath.read_text())
        schema = json_schema
    elif filepath.suffix == ".csv":
        instance_w_missing = pd.read_csv(filepath).convert_dtypes().to_dict(orient="records")
        instance = [
            {colname:value for colname,value in row.items() if pd.notna(value)}
             for row in instance_w_missing
        ]
        schema = csv_schema
    report = validate_against_jsonschema(instance, schema=schema)
    return report

def test_valid_csv_data_dictionaries():
    csvs = Path(VLMD_EXAMPLE_PATH).glob("valid/*.csv")
    csvreports = []
    for filepath in csvs:
        report = to_summary(filepath)
        assert report["valid"],f"# this example is invalid but is intended to be valid:\n\n {json.dumps(report['errors'],indent=2)}"

def test_valid_json_data_dictionaries():
    jsons = Path(VLMD_EXAMPLE_PATH).glob("valid/*.json")
    jsonreports = []
    for filepath in jsons:
        report = to_summary(filepath)
        assert report["valid"],f"# this example is invalid but is intended to be valid:\n\n {str(filepath)}\n\n{report_summary}"


def test_invalid_csv_data_dictionaries():
    csvs = Path(VLMD_EXAMPLE_PATH).glob("invalid/*.csv")
    csvreports = []
    for filepath in csvs:
        report = to_summary(filepath)
        assert not report["valid"],f"{str(filepath)} should be an example of an INVALID csv file but is valid." 

def test_invalid_json_data_dictionaries():
    jsons = Path(VLMD_EXAMPLE_PATH).glob("invalid/*.json")
    jsonreports = []
    for filepath in jsons:
        report = to_summary(filepath)
        assert not report["valid"],f"{str(filepath)} should be an example of an INVALID json file but is valid." 
 