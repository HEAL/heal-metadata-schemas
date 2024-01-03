# {{ schema.title }} _version {{ schema.version }}_

{{ schema.description }}

## Properties

{% for itemname,item in schema.properties.items() %}
{% include 'properties.md' %}
{% endfor %}


# End of schema - Additional Property information 

{% for itemname,item in schema['properties'].items() %}
{% if 'additionalDescription' in item %}
## `{{ itemname }}` {{ item.additionalDescription }}
{% endif %}
{% endfor %}