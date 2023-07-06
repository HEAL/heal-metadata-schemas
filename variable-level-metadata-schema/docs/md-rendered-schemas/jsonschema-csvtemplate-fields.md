# HEAL Variable Level Metadata Fields

- [Property `module`](#module)
- [Property `name`](#name)
- [Property `title`](#title)
- [Property `description`](#description)
- [Property `type`](#type)
- [Property `format`](#format)
  - [Property `String Format`](#format_anyOf_i0)
  - [Property `Date Format`](#format_anyOf_i1)
  - [Property `Geopoint Format`](#format_anyOf_i2)
    - [Property `item 0`](#format_anyOf_i2_oneOf_i0)
    - [Property `item 1`](#format_anyOf_i2_oneOf_i1)
  - [Property `geojson`](#format_anyOf_i3)
- [Property `constraints.maxLength`](#constraintsmaxLength)
- [Property `constraints.enum`](#constraintsenum)
- [Property `constraints.pattern`](#constraintspattern)
- [Property `constraints.maximum`](#constraintsmaximum)
- [Property `encodings`](#encodings)
- [Property `ordered`](#ordered)
- [Property `missingValues`](#missingValues)
- [Property `trueValues`](#trueValues)
- [Property `falseValues`](#falseValues)
- [Property `repo_link`](#repo_link)
- [Property `standardsMappings.type`](#standardsMappingstype)
- [Property `standardsMappings.label`](#standardsMappingslabel)
- [Property `standardsMappings.url`](#standardsMappingsurl)
- [Property `standardsMappings.source`](#standardsMappingssource)
- [Property `standardsMappings.id`](#standardsMappingsid)
- [Property `relatedConcepts.type`](#relatedConceptstype)
- [Property `relatedConcepts.label`](#relatedConceptslabel)
- [Property `relatedConcepts.url`](#relatedConceptsurl)
- [Property `relatedConcepts.source`](#relatedConceptssource)
- [Property `relatedConcepts.id`](#relatedConceptsid)
- [Property `univarStats.median`](#univarStatsmedian)
- [Property `univarStats.mean`](#univarStatsmean)
- [Property `univarStats.std`](#univarStatsstd)
- [Property `univarStats.min`](#univarStatsmin)
- [Property `univarStats.max`](#univarStatsmax)
- [Property `univarStats.mode`](#univarStatsmode)
- [Property `univarStats.count`](#univarStatscount)
- [Property `univarStats.twentyFifthPercentile`](#univarStatstwentyFifthPercentile)
- [Property `univarStats.seventyFifthPercentile`](#univarStatsseventyFifthPercentile)
- [Property `univarStats.categoricalMarginals.name`](#univarStatscategoricalMarginalsname)
- [Property `univarStats.categoricalMarginals.count`](#univarStatscategoricalMarginalscount)

**Title:** HEAL Variable Level Metadata Fields

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** Variable level metadata individual fields integrated into the variable level
metadata object within the HEAL platform metadata service.

> Note, only `name` and `description` are required.
>  Listed at the end of the description are suggested "priority" levels in brackets (e.g., [<priority>]):
  1. [Required]: Needs to be filled out to be valid.
  2. [Highly recommended]: Greatly help using the data dictionary but not required. 
  3. [Optional, if applicable]: May only be applicable to certain fields.
  4. [Autopopulated, if not filled]: These fields are intended to be autopopulated from other fields but can be filled out if desired.
  5. [Experimental]: These fields are not currently used but are in development.

| Property                                                                           | Pattern | Type             | Deprecated | Definition | Title/Description                                                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| - [module](#module )                                                               | No      | string           | No         | -          | Module                                                                                                                                                                                                                                                       |
| + [name](#name )                                                                   | No      | string           | No         | -          | Variable Name                                                                                                                                                                                                                                                |
| - [title](#title )                                                                 | No      | string           | No         | -          | Variable Label (ie Title)                                                                                                                                                                                                                                    |
| + [description](#description )                                                     | No      | string           | No         | -          | Variable Description                                                                                                                                                                                                                                         |
| - [type](#type )                                                                   | No      | enum (of string) | No         | -          | Variable Type                                                                                                                                                                                                                                                |
| - [format](#format )                                                               | No      | Combination      | No         | -          | Frictionless Formats                                                                                                                                                                                                                                         |
| - [constraints.maxLength](#constraintsmaxLength )                                  | No      | integer          | No         | -          | Maximum Length                                                                                                                                                                                                                                               |
| - [constraints.enum](#constraintsenum )                                            | No      | string           | No         | -          | Variable Possible Values                                                                                                                                                                                                                                     |
| - [constraints.pattern](#constraintspattern )                                      | No      | string           | No         | -          | Regular Expression Pattern                                                                                                                                                                                                                                   |
| - [constraints.maximum](#constraintsmaximum )                                      | No      | integer          | No         | -          | Maximum Value                                                                                                                                                                                                                                                |
| - [encodings](#encodings )                                                         | No      | string           | No         | -          | Variable Value Encodings (i.e., mappings; value labels)                                                                                                                                                                                                      |
| - [ordered](#ordered )                                                             | No      | boolean          | No         | -          | An ordered variable                                                                                                                                                                                                                                          |
| - [missingValues](#missingValues )                                                 | No      | string           | No         | -          | Missing Values                                                                                                                                                                                                                                               |
| - [trueValues](#trueValues )                                                       | No      | string           | No         | -          | For boolean (true) variable (as defined in type field), this field allows<br />a physical string representation to be cast as true (increasing<br />readability of the field). It can include one or more values.<br /><br />[Optional, if applicable]<br /> |
| - [falseValues](#falseValues )                                                     | No      | string           | No         | -          | Boolean False Value Labels                                                                                                                                                                                                                                   |
| - [repo_link](#repo_link )                                                         | No      | string           | No         | -          | Variable Repository Link                                                                                                                                                                                                                                     |
| - [standardsMappings.type](#standardsMappingstype )                                | No      | string           | No         | -          | Standards Mapping - Title                                                                                                                                                                                                                                    |
| - [standardsMappings.label](#standardsMappingslabel )                              | No      | string           | No         | -          | Standards Mapping - Label                                                                                                                                                                                                                                    |
| - [standardsMappings.url](#standardsMappingsurl )                                  | No      | string           | No         | -          | Standards Mapping - Url                                                                                                                                                                                                                                      |
| - [standardsMappings.source](#standardsMappingssource )                            | No      | string           | No         | -          | Standard Mapping - Source                                                                                                                                                                                                                                    |
| - [standardsMappings.id](#standardsMappingsid )                                    | No      | string           | No         | -          | Standard Mapping - Id                                                                                                                                                                                                                                        |
| - [relatedConcepts.type](#relatedConceptstype )                                    | No      | string           | No         | -          | Related concepts - Type                                                                                                                                                                                                                                      |
| - [relatedConcepts.label](#relatedConceptslabel )                                  | No      | string           | No         | -          | Related Concepts - Label                                                                                                                                                                                                                                     |
| - [relatedConcepts.url](#relatedConceptsurl )                                      | No      | string           | No         | -          | Related Concepts - Url                                                                                                                                                                                                                                       |
| - [relatedConcepts.source](#relatedConceptssource )                                | No      | string           | No         | -          | Related Concepts - Source                                                                                                                                                                                                                                    |
| - [relatedConcepts.id](#relatedConceptsid )                                        | No      | string           | No         | -          | Related Concepts - Id                                                                                                                                                                                                                                        |
| - [univarStats.median](#univarStatsmedian )                                        | No      | number           | No         | -          | -                                                                                                                                                                                                                                                            |
| - [univarStats.mean](#univarStatsmean )                                            | No      | number           | No         | -          | -                                                                                                                                                                                                                                                            |
| - [univarStats.std](#univarStatsstd )                                              | No      | number           | No         | -          | -                                                                                                                                                                                                                                                            |
| - [univarStats.min](#univarStatsmin )                                              | No      | number           | No         | -          | -                                                                                                                                                                                                                                                            |
| - [univarStats.max](#univarStatsmax )                                              | No      | number           | No         | -          | -                                                                                                                                                                                                                                                            |
| - [univarStats.mode](#univarStatsmode )                                            | No      | number           | No         | -          | -                                                                                                                                                                                                                                                            |
| - [univarStats.count](#univarStatscount )                                          | No      | integer          | No         | -          | -                                                                                                                                                                                                                                                            |
| - [univarStats.twentyFifthPercentile](#univarStatstwentyFifthPercentile )          | No      | number           | No         | -          | -                                                                                                                                                                                                                                                            |
| - [univarStats.seventyFifthPercentile](#univarStatsseventyFifthPercentile )        | No      | number           | No         | -          | -                                                                                                                                                                                                                                                            |
| - [univarStats.categoricalMarginals.name](#univarStatscategoricalMarginalsname )   | No      | string           | No         | -          | -                                                                                                                                                                                                                                                            |
| - [univarStats.categoricalMarginals.count](#univarStatscategoricalMarginalscount ) | No      | integer          | No         | -          | -                                                                                                                                                                                                                                                            |
| - [](#additionalProperties )                                                       | No      | object           | No         | -          | -                                                                                                                                                                                                                                                            |

## <a name="module"></a>Property `module`

**Title:** Module

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The section, form, survey instrument, set of measures  or other broad category used 
to group variables.

**Examples:** 

```json
"Demographics"
```

```json
"PROMIS"
```

```json
"Substance use"
```

```json
"Medical History"
```

```json
"Sleep questions"
```

```json
"Physical activity"
```

## <a name="name"></a>Property `name`

**Title:** Variable Name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The name of a variable (i.e., field) as it appears in the data. 

[Required]

## <a name="title"></a>Property `title`

**Title:** Variable Label (ie Title)

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The human-readable title or label of the variable. 

[Highly recommended]

**Example:** 

```json
"My Variable (for name of my_variable)"
```

## <a name="description"></a>Property `description`

**Title:** Variable Description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** An extended description of the variable. This could be the definition of a variable or the 
question text (e.g., if a survey). 

[Required]

**Examples:** 

```json
"Definition"
```

```json
"Question text (if a survey)"
```

## <a name="type"></a>Property `type`

**Title:** Variable Type

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** A classification or category of a particular data element or property expected or allowed in the dataset.

-  `number` (A numeric value with optional decimal places. (e.g., 3.14))
-  `integer` (A whole number without decimal places. (e.g., 42))
-  `string` (A sequence of characters. (e.g., \"test\"))
-  `any` (Any type of data is allowed. (e.g., true))
-  `boolean` (A binary value representing true or false. (e.g., true))
-  `date` (A specific calendar date. (e.g., \"2023-05-25\"))
-  `datetime` (A specific date and time, including timezone information. (e.g., \"2023-05-25T10:30:00Z\"))
-  `time` (A specific time of day. (e.g., \"10:30:00\"))
-  `year` (A specific year. (e.g., 2023)
-  `yearmonth` (A specific year and month. (e.g., \"2023-05\"))
-  `duration` (A length of time. (e.g., \"PT1H\")
-  `geopoint` (A pair of latitude and longitude coordinates. (e.g., [51.5074, -0.1278]))

Must be one of:
* "number"
* "integer"
* "string"
* "any"
* "boolean"
* "date"
* "datetime"
* "time"
* "year"
* "yearmonth"
* "duration"
* "geopoint"

## <a name="format"></a>Property `format`

**Title:** Frictionless Formats

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** A format taken from one of the [frictionless specification](https://specs.frictionlessdata.io/) schemas.
For example, for tabular data, there is the [Table Schema specification](https://specs.frictionlessdata.io/table-schema)

Each format is dependent on the `type` specified. For example:
If `type` is "string", then see the String formats. 
If `type` is one of the date-like formats, then see Date formats.

| Any of(Option)                      |
| ----------------------------------- |
| [String Format](#format_anyOf_i0)   |
| [Date Format](#format_anyOf_i1)     |
| [Geopoint Format](#format_anyOf_i2) |
| [geojson](#format_anyOf_i3)         |

### <a name="format_anyOf_i0"></a>Property `String Format`

**Title:** String Format

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

Must be one of:
* "uri"
* "email"
* "binary"
* "uuid"

### <a name="format_anyOf_i1"></a>Property `Date Format`

**Title:** Date Format

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** A format for a date variable (`date`,`time`,`datetime`).  
    \n\t* **default**: An ISO8601 format string.
    \n\t* **any**: Any parsable representation of a date/time/datetime. The implementing library can attempt to parse the datetime via a range of strategies.
    \n\t* **{PATTERN}**: The value can be parsed according to `{PATTERN}`, which `MUST` follow the date formatting syntax of C / Python [strftime](http://strftime.org/).

\nExamples:

  `%Y-%m-%d` (for date, e.g., 2023-05-25)
  `%Y%-%d` (for date, e.g., 20230525) for date without dashes"
  `%Y-%m-%dT%H:%M:%S` (for datetime, e.g., 2023-05-25T10:30:45)
  `%Y-%m-%dT%H:%M:%SZ` (for datetime with UTC timezone, e.g., 2023-05-25T10:30:45Z)
  `%Y-%m-%dT%H:%M:%S%z` (for datetime with timezone offset, e.g., 2023-05-25T10:30:45+0300)
  `%Y-%m-%dT%H:%M` (for datetime without seconds, e.g., 2023-05-25T10:30)
  `%Y-%m-%dT%H` (for datetime without minutes and seconds, e.g., 2023-05-25T10)
  `%H:%M:%S` (for time, e.g., 10:30:45)
  `%H:%M:%SZ` (for time with UTC timezone, e.g., 10:30:45Z)
  `%H:%M:%S%z` (for time with timezone offset, e.g., 10:30:45+0300)

### <a name="format_anyOf_i2"></a>Property `Geopoint Format`

**Title:** Geopoint Format

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** The two types of formats for `geopoint` (describing a geographic point).

| One of(Option)                      |
| ----------------------------------- |
| [item 0](#format_anyOf_i2_oneOf_i0) |
| [item 1](#format_anyOf_i2_oneOf_i1) |

#### <a name="format_anyOf_i2_oneOf_i0"></a>Property `item 0`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** A JSON array or a string parsable as a JSON array where each item is a number with the first 
as the latitude and the second as longitude. 

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | N/A                |

#### <a name="format_anyOf_i2_oneOf_i1"></a>Property `item 1`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** Contains latitude and longitude with two keys ("lat" and "long") with number items mapped to each key.

### <a name="format_anyOf_i3"></a>Property `geojson`

**Title:** geojson

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** The JSON object according to the geojson spec.

Must be one of:
* "topojson"
* "default"

## <a name="constraintsmaxLength"></a>Property `constraints.maxLength`

**Title:** Maximum Length

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Indicates the maximum length of an iterable (e.g., array, string, or
object). For example, if 'Hello World' is the longest value of a
categorical variable, this would be a maxLength of 11.

[Optional,if applicable]

## <a name="constraintsenum"></a>Property `constraints.enum`

**Title:** Variable Possible Values

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Constrains possible values to a set of values.

[Optional,if applicable]

| Restrictions                      |                                                                                                                                                                                                    |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^(?:[^\|]+\\|\|[^\|]*)(?:[^\|]*\\|)*[^\|]*$``` [Test](https://regex101.com/?regex=%5E%28%3F%3A%5B%5E%7C%5D%2B%5C%7C%7C%5B%5E%7C%5D%2A%29%28%3F%3A%5B%5E%7C%5D%2A%5C%7C%29%2A%5B%5E%7C%5D%2A%24) |

## <a name="constraintspattern"></a>Property `constraints.pattern`

**Title:** Regular Expression Pattern

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A regular expression pattern the data MUST conform to.

[Optional,if applicable]

## <a name="constraintsmaximum"></a>Property `constraints.maximum`

**Title:** Maximum Value

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Specifies the maximum value of a field (e.g., maximum -- or most
recent -- date, maximum integer etc). Note, this is different then
maxLength property.

[Optional,if applicable]

## <a name="encodings"></a>Property `encodings`

**Title:** Variable Value Encodings (i.e., mappings; value labels)

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Variable value encodings provide a way to further annotate any value within a any variable type,
making values easier to understand. 

Many analytic software programs (e.g., SPSS,Stata, and SAS) use numerical encodings and some algorithms
only support numerical values. Encodings (and mappings) allow categorical values to be stored as
numerical values.

Additionally, as another use case, this field provides a way to
store categoricals that are stored as  "short" labels (such as
abbreviations).

[Optional,if applicable]

**Examples:** 

```json
"0=No|1=Yes"
```

```json
"HW=Hello world|GBW=Good bye world|HM=Hi,Mike"
```

| Restrictions                      |                                                                                                                                                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^(?:.*?=.*?(?:\\|\|$))+$``` [Test](https://regex101.com/?regex=%5E%28%3F%3A.%2A%3F%3D.%2A%3F%28%3F%3A%5C%7C%7C%24%29%29%2B%24&testString=%220%3DNo%7C1%3DYes%22) |

## <a name="ordered"></a>Property `ordered`

**Title:** An ordered variable

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

**Description:** Indicates whether a categorical variable is ordered. This variable  is
relevant for variables that have an ordered relationship but not
necessarily  a numerical relationship (e.g., Strongly disagree < Disagree
< Neutral < Agree).

[Optional,if applicable]

## <a name="missingValues"></a>Property `missingValues`

**Title:** Missing Values

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A list of missing values specific to a variable.

[Optional, if applicable]

| Restrictions                      |                                                                                                                                                                                                    |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^(?:[^\|]+\\|\|[^\|]*)(?:[^\|]*\\|)*[^\|]*$``` [Test](https://regex101.com/?regex=%5E%28%3F%3A%5B%5E%7C%5D%2B%5C%7C%7C%5B%5E%7C%5D%2A%29%28%3F%3A%5B%5E%7C%5D%2A%5C%7C%29%2A%5B%5E%7C%5D%2A%24) |

## <a name="trueValues"></a>Property `trueValues`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** For boolean (true) variable (as defined in type field), this field allows
a physical string representation to be cast as true (increasing
readability of the field). It can include one or more values.

[Optional, if applicable]

**Examples:** 

```json
"Required|REQUIRED"
```

```json
"required|Yes|Y|Checked"
```

```json
"Checked"
```

```json
"Required"
```

| Restrictions                      |                                                                                                                                                                                                                                         |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^(?:[^\|]+\\|\|[^\|]*)(?:[^\|]*\\|)*[^\|]*$``` [Test](https://regex101.com/?regex=%5E%28%3F%3A%5B%5E%7C%5D%2B%5C%7C%7C%5B%5E%7C%5D%2A%29%28%3F%3A%5B%5E%7C%5D%2A%5C%7C%29%2A%5B%5E%7C%5D%2A%24&testString=%22Required%7CREQUIRED%22) |

## <a name="falseValues"></a>Property `falseValues`

**Title:** Boolean False Value Labels

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** For boolean (false) variable (as defined in type field), this field allows
a physical string representation to be cast as false (increasing
readability of the field) that is not a standard false value. It can include one or more values.

| Restrictions                      |                                                                                                                                                                                                    |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^(?:[^\|]+\\|\|[^\|]*)(?:[^\|]*\\|)*[^\|]*$``` [Test](https://regex101.com/?regex=%5E%28%3F%3A%5B%5E%7C%5D%2B%5C%7C%7C%5B%5E%7C%5D%2A%29%28%3F%3A%5B%5E%7C%5D%2A%5C%7C%29%2A%5B%5E%7C%5D%2A%24) |

## <a name="repo_link"></a>Property `repo_link`

**Title:** Variable Repository Link

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A link to the variable as it exists on the home repository, if applicable

## <a name="standardsMappingstype"></a>Property `standardsMappings.type`

**Title:** Standards Mapping - Title

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The **type** of mapping linked to a published set of standard variables such as the NIH Common Data Elements program.
[Autopopulated, if not filled]

**Examples:** 

```json
"cde"
```

```json
"ontology"
```

```json
"reference_list"
```

## <a name="standardsMappingslabel"></a>Property `standardsMappings.label`

**Title:** Standards Mapping - Label

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A free text **label** of a mapping indicating a mapping(s) to a published set of standard variables such as the NIH Common Data Elements program.

[Autopopulated, if not filled]

**Examples:** 

```json
"substance use"
```

```json
"chemical compound"
```

```json
"promis"
```

## <a name="standardsMappingsurl"></a>Property `standardsMappings.url`

**Title:** Standards Mapping - Url

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

**Description:** The url that links out to the published, standardized mapping.

[Autopopulated, if not filled]

**Example:** 

```json
"https://cde.nlm.nih.gov/deView?tinyId=XyuSGdTTI"
```

## <a name="standardsMappingssource"></a>Property `standardsMappings.source`

**Title:** Standard Mapping - Source

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The source of the standardized variable.

**Example:** 

```json
"TBD (will have controlled vocabulary)"
```

## <a name="standardsMappingsid"></a>Property `standardsMappings.id`

**Title:** Standard Mapping - Id

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The id locating the individual mapping within the given source.

## <a name="relatedConceptstype"></a>Property `relatedConcepts.type`

**Title:** Related concepts - Type

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The **type** of mapping to a published set of concepts related to the given field such as 
ontological information (eg., NCI thesaurus, bioportal etc)

[Autopopulated, if not filled]

## <a name="relatedConceptslabel"></a>Property `relatedConcepts.label`

**Title:** Related Concepts - Label

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A free text **label** of mapping to a published set of concepts related to the given field such as 
ontological information (eg., NCI thesaurus, bioportal etc)

[Autopopulated, if not filled]

## <a name="relatedConceptsurl"></a>Property `relatedConcepts.url`

**Title:** Related Concepts - Url

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

**Description:** The url that links out to the published, standardized concept.

[Autopopulated, if not filled]

**Example:** 

```json
"https://cde.nlm.nih.gov/deView?tinyId=XyuSGdTTI"
```

## <a name="relatedConceptssource"></a>Property `relatedConcepts.source`

**Title:** Related Concepts - Source

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The source of the related concept.

[Autopopulated, if not filled]

**Example:** 

```json
"TBD (will have controlled vocabulary)"
```

## <a name="relatedConceptsid"></a>Property `relatedConcepts.id`

**Title:** Related Concepts - Id

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The id locating the individual mapping within the given source.

[Autopopulated, if not filled]

## <a name="univarStatsmedian"></a>Property `univarStats.median`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

## <a name="univarStatsmean"></a>Property `univarStats.mean`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

## <a name="univarStatsstd"></a>Property `univarStats.std`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

## <a name="univarStatsmin"></a>Property `univarStats.min`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

## <a name="univarStatsmax"></a>Property `univarStats.max`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

## <a name="univarStatsmode"></a>Property `univarStats.mode`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

## <a name="univarStatscount"></a>Property `univarStats.count`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

## <a name="univarStatstwentyFifthPercentile"></a>Property `univarStats.twentyFifthPercentile`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

## <a name="univarStatsseventyFifthPercentile"></a>Property `univarStats.seventyFifthPercentile`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

## <a name="univarStatscategoricalMarginalsname"></a>Property `univarStats.categoricalMarginals.name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="univarStatscategoricalMarginalscount"></a>Property `univarStats.categoricalMarginals.count`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
