# {{ schema.title }} 

_version {{ schema.version }}_

{{ schema.description }}

{% for itemname,item in schema.properties.items() %}
## `{{ itemname }}` _({{ item.type }}{{ ',required' if itemname in schema.required }})_
{{ item.description }}
{% if itemname == 'fields' %}
{{ item['items']['description'] }}
### Properties for each `fields` record
{% set schema = item['items'] %}
{% for itemname,item in item['items']['properties'].items() %}

{% include 'properties.md' %}

------

{% endfor %}
{% endif %}
{% endfor %}

### Additional `fields` property information

{% for itemname,item in schema["properties"]["fields"]["items"]["properties"].items() %}
{% if 'additionalDescription' in item %}
#### `{{ itemname }}` {{ item.additionalDescription }}
{% endif %}
{% endfor %}
