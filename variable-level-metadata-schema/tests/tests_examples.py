import jsonschema
import frictionless

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


csvs = Path("examples").glob("*/*.csv")
jsons = Path("examples").glob("*/*.json")

csvreports = []
for filepath in csvs:
    resource = Resource(path=filepath,schema="schemas/frictionless/csvtemplate/fields.json")
    report = resource.validate()
    csvreports.append(report)

jsonreports = []
for filepath in jsons:
    json_object = json.loads(filepath.read_text())
    report = validate_against_jsonschema(json_object, schema="schemas/jsonschema/data-dictionary.json")
    jsonreports.append(report)
