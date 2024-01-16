# HEAL Variable Level Metadata Fields 

_version 0.2.0_

<!-- Below annotation is specific for folks filling out the csv template
and so is put here rather than in the actual schema annotations.
The wording comes from a prior manual edit of the HEAL DSC data 
packaging guidance version.
 -->

The aim of this HEAL metadata piece is to track and provide basic information about variables in a tabular data file (i.e. a data file with rows and columns) from your HEAL study. The objective is to list all variables and descriptive information about those variables. This will ensure that potential secondary data users know what data has been collected or calculated and how to use these data. Note that a given study can have multiple tabular data files; You should create a data dictionary for each tabular data file. Thus, a study may have multiple data dictionaries.



!!! note "Highly encouraged"

  Only `name` and `description` properties are required. 
  For categorical variables, `constraints.enum` and `enumLabels` (where applicable) properties are highly encouraged. 
  For studies using HEAL or other common data elements (CDEs), `standardsMappings` information is highly encouraged.
  `type` and `format` properties may be particularly useful for some variable types (e.g. date-like variables)


## Properties (i.e., fields or variables)


**`schemaVersion`** _(string)_
 The version of the schema used in agreed upon convention of major.minor.path (e.g., 1.0.2) 

NOTE: This is NOT for versioning of each indiviual data dictionary instance. 
Rather, it is the
version of THIS schema document. See `version` property (below) if specifying the individual data dictionary instance
version.

If generating a vlmd document as a csv file, include this version in 
every row/record to indicate this is a schema level property 
(not applicable for the json version as this property is already at the schema/root level)

Examples:


```
  1.0.0

```

```
  0.2.0

```

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
  Medical History

```

**`name`** _(string,required)_
 The name of a variable (i.e., field) as it appears in the data. 

Examples:


```
  gender_id

```

**`title`** _(string)_
 The human-readable title or label of the variable.

Examples:


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

Must be one of: `number`, `integer`, `string`, `any`, `boolean`, `date`, `datetime`, `time`, `year`, `yearmonth`, `duration`, `geopoint`

**`format`** _(string)_
 Indicates the format of the type specified in the `type` property. 
Each format is dependent on the `type` specified. 
See [here](https://specs.frictionlessdata.io/table-schema/#types-and-formats) 
for more information about appropriate `format` values by variable `type`.


**`constraints.required`** _(boolean)_
 If this variable is marked as true, then this variable's value must be present
(ie not missing; see missingValues). If marked as false or not present, then the 
variable CAN be missing.


**`constraints.maxLength`** _(integer)_
 Indicates the maximum length of an iterable (e.g., array, string, or
object). For example, if 'Hello World' is the longest value of a
categorical variable, this would be a maxLength of 11.


**`constraints.enum`** _(string)_
 Constrains possible values to a set of values.

Examples:


```
  1|2|3|4|5

```

```
  Poor|Fair|Good|Very good|Excellent

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

This field is intended to follow [this pattern](https://specs.frictionlessdata.io/patterns/#table-schema-enum-labels-and-ordering)

Examples:


```
  1=Poor|2=Fair|3=Good|4=Very good|5=Excellent

```

```
  HW=Hello world|GBW=Good bye world|HM=Hi, Mike

```

**`enumOrdered`** _(boolean)_
 Indicates whether a categorical variable is ordered. This variable  is
relevant for variables that have an ordered relationship but not
necessarily  a numerical relationship (e.g., Strongly disagree < Disagree
< Neutral < Agree).

This field is intended to follow the ordering aspect of this [this pattern][this pattern](https://specs.frictionlessdata.io/patterns/#table-schema-enum-labels-and-ordering)


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
  required|Yes|Checked

```

```
  required

```

**`falseValues`** _(string)_
 For boolean (false) variable (as defined in type field), this field allows
a physical string representation to be cast as false (increasing
readability of the field) that is not a standard false value. It can include one or more values.

Examples:


```
  Not required|NOT REQUIRED

```

```
  No

```

**`standardsMappings[0].instrument.url`** _(string)_
 A url (e.g., link, address) to a file or other resource containing the instrument, or
a set of items which encompass a variable in this variable level metadata document (if at the root level or the document level) 
or the individual variable (if at the field level). 

Examples:


```
  https://www.heal.nih.gov/files/CDEs/2023-05/adult-demographics-cdes.xlsx

```

**`standardsMappings[0].instrument.source`** _(string)_
 An abbreviated name/acronym from a controlled vocabulary referencing the resource (e.g., program or repository)
containing the instrument, or a set of items which encompass a variable in this variable level metadata document (if at the root level or the document level) 
or the individual variable (if at the field level). 

Must be one of: `heal-cde`

**`standardsMappings[0].instrument.title`** _(string)_
 
Examples:


```
  Adult demographics

```

```
  adult-demographics

```

**`standardsMappings[0].instrument.id`** _(string)_
 A code or other string that identifies the instrument within the source.
This should always be from the source's formal, standardized identification system 

Examples:


```
  5141

```

**`standardsMappings[0].item.url`** _(string)_
 The url that links out to the published, standardized mapping of a variable (e.g., common data element)

Examples:


```
  https://evs.nci.nih.gov/ftp1/CDISC/SDTM/SDTM%20Terminology.html#CL.C74457.RACE

```

**`standardsMappings[0].item.source`** _(string)_
 The source of the standardized variable. Note, this property is required if 
an id is specified.

Examples:


```
  CDISC

```

**`standardsMappings[0].item.id`** _(string)_
 The id locating the individual mapping within the given source. 
Note, the `standardsMappings[0].source` property is required if 
this property is specified.

Examples:


```
  C74457

```


## End of schema - Additional Property information 

## `type` enum definitions:

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

## `format` examples/definitions of patterns and possible values:

Examples of date time pattern formats

- `%Y-%m-%d` (for date, e.g., 2023-05-25)
- `%Y%-%d` (for date, e.g., 20230525) for date without dashes
- `%Y-%m-%dT%H:%M:%S` (for datetime, e.g., 2023-05-25T10:30:45)
- `%Y-%m-%dT%H:%M:%SZ` (for datetime with UTC timezone, e.g., 2023-05-25T10:30:45Z)
- `%Y-%m-%dT%H:%M:%S%z` (for datetime with timezone offset, e.g., 2023-05-25T10:30:45+0300)
- `%Y-%m-%dT%H:%M` (for datetime without seconds, e.g., 2023-05-25T10:30)
- `%Y-%m-%dT%H` (for datetime without minutes and seconds, e.g., 2023-05-25T10)
- `%H:%M:%S` (for time, e.g., 10:30:45)
- `%H:%M:%SZ` (for time with UTC timezone, e.g., 10:30:45Z)
- `%H:%M:%S%z` (for time with timezone offset, e.g., 10:30:45+0300)

Examples of string formats

- `email` if valid emails (e.g., test@gmail.com)
- `uri` if valid uri addresses (e.g., https://example.com/resource123)
- `binary` if a base64 binary encoded string (e.g., authentication token like aGVsbG8gd29ybGQ=)
- `uuid` if a universal unique identifier also known as a guid (eg., f47ac10b-58cc-4372-a567-0e02b2c3d479)


Examples of geopoint formats

The two types of formats for `geopoint` (describing a geographic point).

- `array` (if 'lat,long' (e.g., 36.63,-90.20))
- `object` (if {'lat':36.63,'lon':-90.20})

