# Variable Level Metadata (Data Dictionaries)

This schema defines the variable level metadata for one data dictionary for a given study.Note a given study can have multiple data dictionaries

### `title` _(string,required)_

### `description` _(string)_

### `data_dictionary` _(array,required)_

Variable level metadata individual fields integrated into the variable level
metadata object within the HEAL platform metadata service.

> Note, only `name` and `description` are required.
>  Listed at the end of the description are suggested "priority" levels in brackets (e.g., [<priority>]):
  1. [Required]: Needs to be filled out to be valid.
  2. [Highly recommended]: Greatly help using the data dictionary but not required. 
  3. [Optional, if applicable]: May only be applicable to certain fields.
  4. [Autopopulated, if not filled]: These fields are intended to be autopopulated from other fields but can be filled out if desired.
  5. [Experimental]: These fields are not currently used but are in development.

#### Properties for each record
['name', 'description']


['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
`module` _(string,required)_
 The section, form, survey instrument, set of measures  or other broad category used 
to group variables.

```json

    Demographics

 ```
```json

    PROMIS

 ```
```json

    Substance use

 ```
```json

    Medical History

 ```
```json

    Sleep questions

 ```
```json

    Physical activity

 ```


['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
`name` _(string,required)_
 The name of a variable (i.e., field) as it appears in the data. 

[Required]



['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
`title` _(string,required)_
 The human-readable title or label of the variable. 

[Highly recommended]

```json

    My Variable

 ```
```json

    Gender identity

 ```


['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
`description` _(string,required)_
 An extended description of the variable. This could be the definition of a variable or the 
question text (e.g., if a survey). 

[Required]

```json

    The participant's age at the time of study enrollment

 ```
```json

    What is the highest grade or level of school you have completed or the highest degree you have received?

 ```


['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
`type` _(string,required)_
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
```json

    number

 ```
```json

    integer

 ```
```json

    string

 ```
```json

    any

 ```
```json

    boolean

 ```
```json

    date

 ```
```json

    datetime

 ```
```json

    time

 ```
```json

    year

 ```
```json

    yearmonth

 ```
```json

    duration

 ```
```json

    geopoint

 ```



['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
`format` _(of below,required)_
 Indicates the format of the type specified in the `type` property.

Each format is dependent on the `type` specified. For example:
If `type` is "string", then see the String formats. 
If `type` is one of the date-like formats, then see Date formats.

Sources:

- [Frictionless standard formats associated with types](https://specs.frictionlessdata.io/table-schema/#types-and-formats)

Any of the following:
- ['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
    None _(of below,required)_
     A format for a specialized type of string of:

    - "`email` if valid emails (e.g., test@gmail.com)"
    - "`uri` if valid uri addresses (e.g., https://example.com/resource123)"
    - "`binary` if a base64 binary encoded string (e.g., authentication token like aGVsbG8gd29ybGQ=)"
    - "`uuid` if a universal unique identifier also known as a guid (eg., f47ac10b-58cc-4372-a567-0e02b2c3d479)"

    Possible values:
    ```json

        uri

     ```
    ```json

        email

     ```
    ```json

        binary

     ```
    ```json

        uuid

     ```


- ['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
    None _(string,required)_
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


- ['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
    None _(string,required)_
     The two types of formats for `geopoint` (describing a geographic point).

    - `array` (if 'lat,long' (e.g., 36.63,-90.20))
    - `object` (if {'lat':36.63,'lon':-90.20})

    Possible values:
    ```json

        array

     ```
    ```json

        object

     ```


- ['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
    None _(string,required)_
     The JSON object according to the geojson spec.
    Possible values:
    ```json

        topojson

     ```
    ```json

        default

     ```





['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
`constraints` _(object,required)_
 


    ['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
    `maxLength` _(integer,required)_
     Indicates the maximum length of an iterable (e.g., array, string, or
    object). For example, if 'Hello World' is the longest value of a
    categorical variable, this would be a maxLength of 11.

    [Optional,if applicable]



    ['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
    `enum` _(array,required)_
     Constrains possible values to a set of values.

    [Optional,if applicable]

    ```json

        [1, 2, 3, 4]

     ```
    ```json

        ['White', 'Black or African American', 'American Indian or Alaska Native', 'Native Hawaiian or Other Pacific Islander', 'Asian', 'Some other race', 'Multiracial']

     ```


    ['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
    `pattern` _(string,required)_
     A regular expression pattern the data MUST conform to.

    [Optional,if applicable]



    ['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
    `maximum` _(integer,required)_
     Specifies the maximum value of a field (e.g., maximum -- or most
    recent -- date, maximum integer etc). Note, this is different then
    maxLength property.

    [Optional,if applicable]



    ['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
    `minimum` _(integer,required)_
     Specifies the minimum value of a field.

    [Optional,if applicable]




['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
`encodings` _(object,required)_
 Variable value encodings provide a way to further annotate any value within a any variable type,
making values easier to understand. 


Many analytic software programs (e.g., SPSS,Stata, and SAS) use numerical encodings and some algorithms
only support numerical values. Encodings (and mappings) allow categorical values to be stored as
numerical values.

Additionally, as another use case, this field provides a way to
store categoricals that are stored as  "short" labels (such as
abbreviations).

[Optional,if applicable]

```json

    {'0': 'No', '1': 'Yes'}

 ```
```json

    {'HW': 'Hello world', 'GBW': 'Good bye world', 'HM': 'Hi, Mike'}

 ```


['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
`ordered` _(boolean,required)_
 Indicates whether a categorical variable is ordered. This variable  is
relevant for variables that have an ordered relationship but not
necessarily  a numerical relationship (e.g., Strongly disagree < Disagree
< Neutral < Agree).

[Optional,if applicable]



['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
`missingValues` _(array,required)_
 A list of missing values specific to a variable.

[Highly recommended]

```json

    ['Missing', 'Skipped', 'No preference']

 ```
```json

    ['Missing']

 ```


['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
`trueValues` _(array,required)_
 For boolean (true) variable (as defined in type field), this field allows
a physical string representation to be cast as true (increasing
readability of the field). It can include one or more values.

[Optional, if applicable]

```json

    ['required', 'Yes', 'Checked']

 ```
```json

    ['required']

 ```


['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
`falseValues` _(array,required)_
 For boolean (false) variable (as defined in type field), this field allows
a physical string representation to be cast as false (increasing
readability of the field) that is not a standard false value. It can include one or more values.



['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
`repo_link` _(string,required)_
 A link to the variable as it exists on the home repository, if applicable



['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
`standardsMappings` _(array,required)_
 A published set of standard variables such as the NIH Common Data Elements program.
[Autopopulated, if not filled]


['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
`relatedConcepts` _(array,required)_
 Mappings to a published set of concepts related to the given field such as ontological information (eg., NCI thesaurus, bioportal etc)
[Autopopulated, if not filled]


['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
`univarStats` _(object,required)_
 Univariate statistics inferred from the data about the given variable 

[Experimental]



    ['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
    `median` _(number,required)_
     


    ['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
    `mean` _(number,required)_
     


    ['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
    `std` _(number,required)_
     


    ['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
    `min` _(number,required)_
     


    ['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
    `max` _(number,required)_
     


    ['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
    `mode` _(number,required)_
     


    ['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
    `count` _(integer,required)_
     


    ['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
    `twentyFifthPercentile` _(number,required)_
     


    ['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
    `seventyFifthPercentile` _(number,required)_
     


    ['[', "'", 'n', 'a', 'm', 'e', "'", ',', ' ', "'", 'd', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n', "'", ']']
    `categoricalMarginals` _(array,required)_
     

