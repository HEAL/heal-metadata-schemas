# HEAL Variable Level Metadata Fields

Variable level metadata individual fields integrated into the variable level
metadata object within the HEAL platform metadata service.

!!! note "NOTE"

  Only `name` and `description` properties are required. 
  For categorical variables, `constraints.enum` and `encodings` (where applicable) properties are highly encouraged. 
  For studies using HEAL or other common data elements (CDEs), `standardsMappings` information is highly encouraged.
  `type` and `format` properties may be particularly useful for some variable types (e.g. date-like variables)


## Properties


**`section`** _(string)_
 The section, form, survey instrument, set of measures  or other broad category used 
to group variables. Previously called "module."

Examples:


```
  Demographics

```

```
  PROMIS

```

```
  Substance use

```

```
  Medical History

```

```
  Sleep questions

```

```
  Physical activity

```

**`name`** _(string,required)_
 The name of a variable (i.e., field) as it appears in the data. 


**`title`** _(string)_
 The human-readable title or label of the variable. 

Examples:


```
  My Variable

```

```
  Gender identity

```

**`description`** _(string,required)_
 An extended description of the variable. This could be the definition of a variable or the 
question text (e.g., if a survey). 

Examples:


```
  The participant's age at the time of study enrollment

```

```
  What is the highest grade or level of school you have completed or the highest degree you have received?

```

**`type`** _(string)_
 A classification or category of a particular data element or property expected or allowed in the dataset.

Definitions:

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

Possible values:

- ```

    number

  ```
- ```

    integer

  ```
- ```

    string

  ```
- ```

    any

  ```
- ```

    boolean

  ```
- ```

    date

  ```
- ```

    datetime

  ```
- ```

    time

  ```
- ```

    year

  ```
- ```

    yearmonth

  ```
- ```

    duration

  ```
- ```

    geopoint

  ```


**`format`** _(string)_
 Indicates the format of the type specified in the `type` property. 
Each format is dependent on the `type` specified. 
For example: If `type` is "string", then see the [String formats](https://specs.frictionlessdata.io/table-schema/#string). 
If `type` is "date", "datetime", or "time", default format is ISO8601 formatting for those respective types (see details on ISO8601 format for [Date](https://specs.frictionlessdata.io/table-schema/#date),
[Datetime](https://specs.frictionlessdata.io/table-schema/#datetime), 
or [Time](https://specs.frictionlessdata.io/table-schema/#time)) - If you want to specify a date-like variable using standard Python/C strptime syntax, see [here](#format-details-for-date-datetime-time-type-variables) for details. 
See [here](https://specs.frictionlessdata.io/table-schema/#types-and-formats) for more information about appropriate `format` values by variable `type`. 

[Additional information]

Date Formats (date, datetime, time `type` variable):

A format for a date variable (`date`,`time`,`datetime`).  
**default**: An ISO8601 format string.
**any**: Any parsable representation of a date/time/datetime. The implementing library can attempt to parse the datetime via a range of strategies.

**{PATTERN}**: The value can be parsed according to `{PATTERN}`,
which `MUST` follow the date formatting syntax of 
C / Python [strftime](http://strftime.org/) such as:

- "`%Y-%m-%d` (for date, e.g., 2023-05-25)"
- "`%Y%-%d` (for date, e.g., 20230525) for date without dashes"
- "`%Y-%m-%dT%H:%M:%S` (for datetime, e.g., 2023-05-25T10:30:45)"
- "`%Y-%m-%dT%H:%M:%SZ` (for datetime with UTC timezone, e.g., 2023-05-25T10:30:45Z)"
- "`%Y-%m-%dT%H:%M:%S%z` (for datetime with timezone offset, e.g., 2023-05-25T10:30:45+0300)"
- "`%Y-%m-%dT%H:%M` (for datetime without seconds, e.g., 2023-05-25T10:30)"
- "`%Y-%m-%dT%H` (for datetime without minutes and seconds, e.g., 2023-05-25T10)"
- "`%H:%M:%S` (for time, e.g., 10:30:45)"
- "`%H:%M:%SZ` (for time with UTC timezone, e.g., 10:30:45Z)"
- "`%H:%M:%S%z` (for time with timezone offset, e.g., 10:30:45+0300)"

String formats:

- "`email` if valid emails (e.g., test@gmail.com)"
- "`uri` if valid uri addresses (e.g., https://example.com/resource123)"
- "`binary` if a base64 binary encoded string (e.g., authentication token like aGVsbG8gd29ybGQ=)"
- "`uuid` if a universal unique identifier also known as a guid (eg., f47ac10b-58cc-4372-a567-0e02b2c3d479)"


Geopoint formats:

The two types of formats for `geopoint` (describing a geographic point).

- `array` (if 'lat,long' (e.g., 36.63,-90.20))
- `object` (if {'lat':36.63,'lon':-90.20})


**`constraints.maxLength`** _(integer)_
 Indicates the maximum length of an iterable (e.g., array, string, or
object). For example, if 'Hello World' is the longest value of a
categorical variable, this would be a maxLength of 11.


**`constraints.enum`** _(string)_
 Constrains possible values to a set of values.

Examples:


```
  1|2|3|4|5|6|7|8

```

```
  White|Black or African American|American Indian or Alaska Native|Native Hawaiian or Other Pacific Islander|Asian|Some other race|Multiracial

```

**`constraints.pattern`** _(string)_
 A regular expression pattern the data MUST conform to.


**`constraints.maximum`** _(integer)_
 Specifies the maximum value of a field (e.g., maximum -- or most
recent -- date, maximum integer etc). Note, this is different then
maxLength property.


**`constraints.minimum`** _(integer)_
 Specifies the minimum value of a field.


**`enumLabels`** _(string)_
 Variable value encodings provide a way to further annotate any value within a any variable type,
making values easier to understand. 


Many analytic software programs (e.g., SPSS,Stata, and SAS) use numerical encodings and some algorithms
only support numerical values. Encodings (and mappings) allow categorical values to be stored as
numerical values.

Additionally, as another use case, this field provides a way to
store categoricals that are stored as  "short" labels (such as
abbreviations).

Examples:


```
  0=No|1=Yes

```

```
  HW=Hello world|GBW=Good bye world|HM=Hi,Mike

```

**`enumOrdered`** _(boolean)_
 Indicates whether a categorical variable is ordered. This variable  is
relevant for variables that have an ordered relationship but not
necessarily  a numerical relationship (e.g., Strongly disagree < Disagree
< Neutral < Agree).


**`missingValues`** _(string)_
 A list of missing values specific to a variable.

Examples:


```
  Missing|Skipped|No preference

```

```
  Missing

```

**`trueValues`** _(string)_
 For boolean (true) variable (as defined in type field), this field allows
a physical string representation to be cast as true (increasing
readability of the field). It can include one or more values.

Examples:


```
  Required|REQUIRED

```

```
  required|Yes|Y|Checked

```

```
  Checked

```

```
  Required

```

**`falseValues`** _(string)_
 For boolean (false) variable (as defined in type field), this field allows
a physical string representation to be cast as false (increasing
readability of the field) that is not a standard false value. It can include one or more values.


**`standardsMappings[0].instrument.url`** _(string)_
 

**`standardsMappings[0].instrument.source`** _(string)_
 
Possible values:

- ```

    heal-cde

  ```


**`standardsMappings[0].instrument.title`** _(string)_
 

**`standardsMappings[0].instrument.id`** _(string)_
 

**`standardsMappings[0].item.url`** _(string)_
 The url that links out to the published, standardized mapping.

Examples:


```
  https://cde.nlm.nih.gov/deView?tinyId=XyuSGdTTI

```

**`standardsMappings[0].item.source`** _(string)_
 The source of the standardized variable.


**`standardsMappings[0].item.id`** _(string)_
 The id locating the individual mapping within the given source.


**`relatedConcepts[0].url`** _(string)_
 The url that links out to the published, standardized concept.


**`relatedConcepts[0].type`** _(string)_
 The **type** of mapping to a published set of concepts related to the given field such as 
ontological information (eg., NCI thesaurus, bioportal etc)


**`relatedConcepts[0].label`** _(string)_
 A free text **label** of mapping to a published set of concepts related to the given field such as 
ontological information (eg., NCI thesaurus, bioportal etc)


**`relatedConcepts[0].source`** _(string)_
 The source of the related concept.

Examples:


```
  TBD (will have controlled vocabulary)

```

**`relatedConcepts[0].id`** _(string)_
 The id locating the individual mapping within the given source.
