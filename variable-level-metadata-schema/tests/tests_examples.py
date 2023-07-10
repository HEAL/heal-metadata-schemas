import jsonschema
import frictionless
import petl as etl
from pathlib import Path

VLMD_PATH = "variable-level-metadata-schema/examples"
CSV_FRICTIONLESS_SCHEMA_PATH = Path(VLMD_PATH)/"schemas/frictionless/csvtemplate/fields.json"
JSON_SCHEMA_PATH = Path(VLMD_PATH)/"schemas/jsonschema/data-dictionary.json"
VLMD_EXAMPLE_PATH = Path(VLMD_PATH)/"examples"

def validate_against_jsonschema(json_object,schema):
    
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
        resource = frictionless.Resource(path=filepath,schema=CSV_FRICTIONLESS_SCHEMA_PATH)
        report = resource.validate()
        assert report["valid"],report.to_summary()

def test_valid_json_data_dictionaries():
    jsons = Path(VLMD_EXAMPLE_PATH).glob("valid/*.json")
    jsonreports = []
    for filepath in jsons:
        json_object = json.loads(filepath.read_text())
        report = validate_against_jsonschema(json_object, schema=JSON_SCHEMA_PATH)
        
        # report to etl to pretty print
        report_summary = str(etl.fromdicts(report["errors"]).totext())

        assert report["valid"],f"# invalid: {str(filepath)}\n\n{report_summary}"


def test_invalid_csv_data_dictionaries():
    csvs = Path(VLMD_EXAMPLE_PATH).glob("invalid/*.csv")
    csvreports = []
    for filepath in csvs:
        resource = frictionless.Resource(path=filepath,schema=CSV_FRICTIONLESS_SCHEMA_PATH)
        report = resource.validate()
        assert not report["valid"],f"{str(filepath)} should be an example of an INVALID file but is valid." 

def test_invalid_json_data_dictionaries():
    jsons = Path(VLMD_EXAMPLE_PATH).glob("invalid/*.json")
    jsonreports = []
    for filepath in jsons:
        json_object = json.loads(filepath.read_text())
        report = validate_against_jsonschema(json_object, schema=JSON_SCHEMA_PATH)
        assert not report["valid"],f"{str(filepath)} should be an example of an INVALID file but is valid." 
 

test_invalid_csv_data_dictionaries()