# Variable Level Metadata (Data Dictionaries)

**Title:** Variable Level Metadata (Data Dictionaries)

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** This schema defines the variable level metadata for one data dictionary for a given study.Note a given study can have multiple data dictionaries

  ### 
## `title`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

  ### 
## `description`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

  ### 
## `data_dictionary`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of object` |
| **Required** | Yes               |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                               | Description                                                                      |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| [HEAL Variable Level Metadata Fields](#data_dictionary_items) | Variable level metadata individual fields integrated into the variable level ... |

### HEAL Variable Level Metadata Fields

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

  ### 
#### `module`

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

  ### 
#### `name`

**Title:** Variable Name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The name of a variable (i.e., field) as it appears in the data. 

[Required]

  ### 
#### `title`

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

  ### 
#### `description`

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

  ### 
#### `type`

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

  ### 
#### `format`

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

<!-- 
| Any of(Option)                                            |
| --------------------------------------------------------- |
| [String Format](#data_dictionary_items_format_anyOf_i0)   |
| [Date Format](#data_dictionary_items_format_anyOf_i1)     |
| [Geopoint Format](#data_dictionary_items_format_anyOf_i2) |
| [geojson](#data_dictionary_items_format_anyOf_i3)         |
 -->

##### Property `String Format`

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

##### Property `Date Format`

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

##### Property `Geopoint Format`

**Title:** Geopoint Format

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** The two types of formats for `geopoint` (describing a geographic point).

<!-- 
| One of(Option)                                            |
| --------------------------------------------------------- |
| [item 0](#data_dictionary_items_format_anyOf_i2_oneOf_i0) |
| [item 1](#data_dictionary_items_format_anyOf_i2_oneOf_i1) |
 -->

##### Property `item 0`

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

##### Property `item 1`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** Contains latitude and longitude with two keys ("lat" and "long") with number items mapped to each key.

##### Property `geojson`

**Title:** geojson

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** The JSON object according to the geojson spec.

Must be one of:
* "topojson"
* "default"

  ### 
#### `constraints`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

  ### 
##### `maxLength`

**Title:** Maximum Length

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Indicates the maximum length of an iterable (e.g., array, string, or
object). For example, if 'Hello World' is the longest value of a
categorical variable, this would be a maxLength of 11.

[Optional,if applicable]

  ### 
##### `enum`

**Title:** Variable Possible Values

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** Constrains possible values to a set of values.

[Optional,if applicable]

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | N/A                |

  ### 
##### `pattern`

**Title:** Regular Expression Pattern

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A regular expression pattern the data MUST conform to.

[Optional,if applicable]

  ### 
##### `maximum`

**Title:** Maximum Value

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Specifies the maximum value of a field (e.g., maximum -- or most
recent -- date, maximum integer etc). Note, this is different then
maxLength property.

[Optional,if applicable]

  ### 
#### `encodings`

**Title:** Variable Value Encodings (i.e., mappings; value labels)

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

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
{
    "0": "No",
    "1": "Yes"
}
```

```json
{
    "HW": "Hello world",
    "GBW": "Good bye world",
    "HM": "Hi, Mike"
}
```

  ### 
#### `ordered`

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

  ### 
#### `missingValues`

**Title:** Missing Values

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** A list of missing values specific to a variable.

[Highly recommended]

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | N/A                |

  ### 
#### `trueValues`

**Title:** Boolean True Value Labels

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

**Description:** For boolean (true) variable (as defined in type field), this field allows
a physical string representation to be cast as true (increasing
readability of the field). It can include one or more values.

[Optional, if applicable]

**Examples:** 

```json
"Required"
```

```json
"REQUIRED"
```

```json
"required"
```

```json
"Yes"
```

```json
"Checked\""
```

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                             | Description |
| ----------------------------------------------------------- | ----------- |
| [trueValues items](#data_dictionary_items_trueValues_items) | -           |

##### trueValues items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

  ### 
#### `falseValues`

**Title:** Boolean False Value Labels

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** For boolean (false) variable (as defined in type field), this field allows
a physical string representation to be cast as false (increasing
readability of the field) that is not a standard false value. It can include one or more values.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | N/A                |

  ### 
#### `repo_link`

**Title:** Variable Repository Link

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A link to the variable as it exists on the home repository, if applicable

  ### 
#### `cde_id`

**Title:** Common Data Element Id

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of object` |
| **Required** | No                |

**Description:** [FUTURE WARNING: WILL BE DEPRECATED] Use `standardsMapping`. The source and id for the NIH Common Data Elements program.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                     | Description |
| --------------------------------------------------- | ----------- |
| [cde_id items](#data_dictionary_items_cde_id_items) | -           |

##### cde_id items

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

  ### 
##### `source`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

  ### 
##### `id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

  ### 
#### `ontology_id`

**Title:** Ontology ID

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of object` |
| **Required** | No                |

**Description:** [FUTURE WARNING: WILL BE DEPRECATED] - Use `relatedConcepts`. Ontological information for the given variable as indicated  by the
source, id, and relation to the specified classification. One or more
ontology classifications can be specified. 

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                               | Description |
| ------------------------------------------------------------- | ----------- |
| [ontology_id items](#data_dictionary_items_ontology_id_items) | -           |

##### ontology_id items

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

  ### 
##### `relation`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

  ### 
##### `source`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

  ### 
##### `id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

  ### 
#### `standardsMappings`

**Title:** Standards Mappings

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of object` |
| **Required** | No                |

**Description:** A published set of standard variables such as the NIH Common Data Elements program.
[Autopopulated, if not filled]

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                           | Description |
| ------------------------------------------------------------------------- | ----------- |
| [standardsMappings items](#data_dictionary_items_standardsMappings_items) | -           |

##### standardsMappings items

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

  ### 
##### `type`

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

  ### 
##### `label`

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

  ### 
##### `url`

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

  ### 
##### `source`

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

  ### 
##### `id`

**Title:** Standard Mapping - Id

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The id locating the individual mapping within the given source.

  ### 
#### `relatedConcepts`

**Title:** Related Concepts

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of object` |
| **Required** | No                |

**Description:** Mappings to a published set of concepts related to the given field such as ontological information (eg., NCI thesaurus, bioportal etc)
[Autopopulated, if not filled]

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                       | Description |
| --------------------------------------------------------------------- | ----------- |
| [relatedConcepts items](#data_dictionary_items_relatedConcepts_items) | -           |

##### relatedConcepts items

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

  ### 
##### `type`

**Title:** Related concepts - Type

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The **type** of mapping to a published set of concepts related to the given field such as 
ontological information (eg., NCI thesaurus, bioportal etc)

[Autopopulated, if not filled]

  ### 
##### `label`

**Title:** Related Concepts - Label

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A free text **label** of mapping to a published set of concepts related to the given field such as 
ontological information (eg., NCI thesaurus, bioportal etc)

[Autopopulated, if not filled]

  ### 
##### `url`

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

  ### 
##### `source`

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

  ### 
##### `id`

**Title:** Related Concepts - Id

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The id locating the individual mapping within the given source.

[Autopopulated, if not filled]

  ### 
#### `univarStats`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** Univariate statistics inferred from the data about the given variable 

[Experimental]

  ### 
##### `median`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

  ### 
##### `mean`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

  ### 
##### `std`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

  ### 
##### `min`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

  ### 
##### `max`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

  ### 
##### `mode`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

  ### 
##### `count`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

  ### 
##### `twentyFifthPercentile`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

  ### 
##### `seventyFifthPercentile`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

  ### 
##### `categoricalMarginals`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of object` |
| **Required** | No                |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                             | Description |
| ------------------------------------------------------------------------------------------- | ----------- |
| [categoricalMarginals items](#data_dictionary_items_univarStats_categoricalMarginals_items) | -           |

##### categoricalMarginals items

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

  ### 
##### `name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

  ### 
##### `count`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

----------------------------------------------------------------------------------------------------------------------------