{% macro render_type_item(itemtitle,item) %}
{{ itemtitle }}:
{% for val in item %}
{% if val is mapping %}
- {{ render_property(None,val,schema) | indent }}
{% else %}
```json

    {{val}}

 ```
{% endif %}
{% endfor %}
{# #}
{# #}
{# #}
{# #}
{% endmacro %}
{# This macro is called for all properties and types with nested dictionary objects like anyOf and oneOf #}
{% macro render_property(itemname,item,schema) %}
{% set itemtype %}
_({{ item.type | default('of below') }}{{ ',required'  if itemname in schema.required }})_
{% endset %}
{# #}
{# #}
{{ '`' if itemname }}{{ itemname }}{{ '`' if itemname }} {{ itemtype }} {{ item.description }}
{# #}
{# #}
{% if item.enum is defined %}
{{ render_type_item('Possible values',item.enum) }}
{% endif %}
{# #}
{# #}
{% if item.anyOf is defined %}
{{ render_type_item('Any of the following',item.anyOf) }}
{% endif %}
{# #}
{# #}
{% if item.oneOf is defined %}
{{ render_type_item('One of the following',item.oneOf) }}
{% endif %}
{# #}
{# #}
{% if item.examples is defined %}
{% for val in item.examples %}
```json

    {{val}}

 ```
{% endfor %}
{% endif %}
{# #}
{# #}
{% if item.properties is defined %}

{% for propname,prop in item.properties.items() %}

{% set header %}`{{ propname }}`{% endset %}
{{ render_property(header,prop,schema) | indent(first=True) }}
{% endfor %}
{% endif %}
{% endmacro %}
{# #}
{# #}
{# #}
{# THIS STARTS THE ACTUAL SCRIPT AND CALLS THE MACRO #}
{# #}

{{ render_property(itemname,item,schema) }}