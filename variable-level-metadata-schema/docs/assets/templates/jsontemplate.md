# {{ schema.title }}

{{ schema.description }}

{% for itemname,item in schema.properties.items() %}
### `{{ itemname }}` _({{ item.type }}{{ ',required' if itemname in schema.required }})_
{{ item.description }}
{% if itemname == 'data_dictionary' %}
{{ item['items']['description'] }}
#### Properties for each record
{% set required %}{{ item['items']['required'] | list }}{% endset %}
{{ required }}
{% for itemname,item in item['items']['properties'].items() %}
{% include 'properties.md' %}
{% endfor %}
{% endif %}
{% endfor %}