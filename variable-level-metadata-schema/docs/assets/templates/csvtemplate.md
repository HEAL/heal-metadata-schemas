# {{ schema.title }} 

_version {{ schema.version }}_

<!-- Below annotation is specific for folks filling out the csv template
and so is put here rather than in the actual schema annotations.
The wording comes from a prior manual edit of the HEAL DSC data 
packaging guidance version.
 -->

The aim of this HEAL metadata piece is to track and provide basic information about variables in a tabular data file (i.e. a data file with rows and columns) from your HEAL study. The objective is to list all variables and descriptive information about those variables. This will ensure that potential secondary data users know what data has been collected or calculated and how to use these data. Note that a given study can have multiple tabular data files; You should create a data dictionary for each tabular data file. Thus, a study may have multiple data dictionaries.

{{ schema.description }}

## Properties (i.e., fields or variables)

{% for itemname,item in schema.properties.items() %}
{% include 'properties.md' %}

------

{% endfor %}

{% for itemname,item in schema.patternProperties.items() %}
{% set itemname = itemname.replace("^","").replace("$","").replace("\[\d+\]","[`number`]") %}
{% include 'properties.md' %}

------
{% endfor %}

## End of schema - Additional Property information 

{% for itemname,item in schema['properties'].items() %}
{% if 'additionalDescription' in item %}
## `{{ itemname }}` {{ item.additionalDescription }}
{% endif %}
{% endfor %}