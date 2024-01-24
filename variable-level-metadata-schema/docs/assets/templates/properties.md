{% macro render_type_item(itemtitle,item) %}
{{ itemtitle }}:

{% for val in item %}
{% if val is mapping %}
- {{ render_property(None,val,schema) | indent }}
{% else %}
- ```

    {{ val }}

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
{% if itemname %}
**`{{ itemname }}`** {{ itemtype }} {{ item.description }}
{% elif item.title %}
__{{ item.title }}__ {{ itemtype }} {{ item.description }}
{% else %}
{{ itemtype }} {{ item.description }}
{% endif %}
{# #}
{# #}
{% if item.enum is defined %}
Must be one of: {{ "`" + "`, `".join(item.enum) + "`" }}
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
Examples:

{% for val in item.examples %}

 {% if val is string %}
```
  {{ val }}

```
 {% elif val is mapping or val is sequence %}
```json

  {{ val }}

```
{% else %}
```
  {{ val }}
```
{% endif %}
{% endfor %}
{% endif %}
{# #}
{# #}
{% if item.properties is defined %}

{% for propname,prop in item.properties.items() %}

- {{ render_property(propname,prop,schema) | indent }}
{% endfor %}
{% endif %}
{% endmacro %}
{# #}
{# #}
{# #}
{# THIS STARTS THE ACTUAL SCRIPT AND CALLS THE MACRO #}
{# #}

{{ render_property(itemname,item,schema) }}