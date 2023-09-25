# {{ schema.title }}

{{ schema.description }}

{% for itemname,item in schema.properties.items() %}
### `{{ itemname }}` _({{ item.type }}{{ ',required' if itemname in schema.required }})_
{{ item.description }}
{% if itemname == 'data_dictionary' %}
{{ item['items']['description'] }}
#### Properties for each record
{% set schema %}{{ item['items'] }}{% endset %}
{% for itemname,item in item['items']['properties'].items() %}
{% include 'properties.md' %}
{% endfor %}
{% endif %}
{% endfor %}