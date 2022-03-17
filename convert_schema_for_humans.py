from json_schema_for_humans.generate import generate_from_filename
from json_schema_for_humans.generation_configuration import GenerationConfiguration

config = GenerationConfiguration(copy_css=False,expand_buttons=True)

json_schema_path = r"C:\Users\tentner-andrea\project_repositories\heal-metadata-schemas\study-metadata-schema.json"
json_schema_for_humans_path = r"C:\Users\tentner-andrea\project_repositories\heal-metadata-schemas\study-metadata-schema-for-humans.html"

generate_from_filename(json_schema_path,json_schema_for_humans_path, config=config) 
