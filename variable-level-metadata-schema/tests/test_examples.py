import jsonschema
import frictionless
import petl as etl
from pathlib import Path
import os
import json
print(os.getcwd())
VLMD_PATH = "variable-level-metadata-schema"
CSV_FRICTIONLESS_SCHEMA_PATH = Path(VLMD_PATH)/"schemas/frictionless/csvtemplate/fields.json"
JSON_SCHEMA_PATH = Path(VLMD_PATH)/"schemas/jsonschema/data-dictionary.json"
VLMD_EXAMPLE_PATH = Path(VLMD_PATH)/"examples"

json_schema_object = json.loads(JSON_SCHEMA_PATH.read_text())
csv_frictionless_schema_object = json.loads(CSV_FRICTIONLESS_SCHEMA_PATH.read_text())


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

# frictionless schemas --> if csv file
# json schemas --> if json file

def test_valid_csv_data_dictionaries():
    csvs = Path(VLMD_EXAMPLE_PATH).glob("valid/*.csv")
    csvreports = []
    for filepath in csvs:
        print("Testing:")
        print(str(filepath))
        resource = frictionless.Resource(path=str(filepath),schema=csv_frictionless_schema_object)
        report = resource.validate()

        assert report["valid"],f"# this example is invalid but is intended to be valid:\n\n {report.to_summary()}"

def test_valid_json_data_dictionaries():
    jsons = Path(VLMD_EXAMPLE_PATH).glob("valid/*.json")
    jsonreports = []
    for filepath in jsons:
        print("Testing:")
        print(str(filepath))
        json_object = json.loads(filepath.read_text())
        report = validate_against_jsonschema(json_object, schema=json_schema_object)
        # report to etl to pretty print
        report_summary = str(etl.fromdicts(report["errors"]))
        assert report["valid"],f"# this example is invalid but is intended to be valid:\n\n {str(filepath)}\n\n{report_summary}"


def test_invalid_csv_data_dictionaries():
    csvs = Path(VLMD_EXAMPLE_PATH).glob("invalid/*.csv")
    csvreports = []
    for filepath in csvs:
        resource = frictionless.Resource(path=str(filepath),schema=csv_frictionless_schema_object)
        report = resource.validate()
        print("Testing:")
        print(str(filepath))
        assert not report["valid"],f"{str(filepath)} should be an example of an INVALID csv file but is valid." 

def test_invalid_json_data_dictionaries():
    jsons = Path(VLMD_EXAMPLE_PATH).glob("invalid/*.json")
    jsonreports = []
    for filepath in jsons:
        json_object = json.loads(filepath.read_text())
        report = validate_against_jsonschema(json_object, schema=json_schema_object)
        print("Testing:")
        print(str(filepath))
        assert not report["valid"],f"{str(filepath)} should be an example of an INVALID json file but is valid." 
 