# {{ schema.title }}

{{ schema.description }}

## Properties

{% for itemname,item in schema.properties.items() %}
{% include 'properties.md' %}
{% endfor %}