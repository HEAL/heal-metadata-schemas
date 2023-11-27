# Variable Level Metadata (Data Dictionaries)

This schema defines the variable level metadata for one data dictionary for a given study.Note a given study can have multiple data dictionaries

### `title` _(string,required)_

### `description` _(string)_

### `fields` _(array,required)_

Variable level metadata individual fields integrated into the variable level
metadata object within the HEAL platform metadata service.

!!! note "NOTE"

  Only `name` and `description` properties are required. 
  For categorical variables, `constraints.enum` and `encodings` (where applicable) properties are highly encouraged. 
  For studies using HEAL or other common data elements (CDEs), `standardsMappings` information is highly encouraged.
  `type` and `format` properties may be particularly useful for some variable types (e.g. date-like variables)

#### Properties for each record

**`module`** _(string)_
 The section, form, survey instrument, set of measures  or other broad category used 
to group variables.

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


**`constraints`** _(object)_
 


- **`maxLength`** _(integer)_
     Indicates the maximum length of an iterable (e.g., array, string, or
    object). For example, if 'Hello World' is the longest value of a
    categorical variable, this would be a maxLength of 11.



- **`enum`** _(array)_
     Constrains possible values to a set of values.

    Examples:


    ```json

      [1, 2, 3, 4]

    ```

    ```json

      ['White', 'Black or African American', 'American Indian or Alaska Native', 'Native Hawaiian or Other Pacific Islander', 'Asian', 'Some other race', 'Multiracial']

    ```


- **`pattern`** _(string)_
     A regular expression pattern the data MUST conform to.



- **`maximum`** _(integer)_
     Specifies the maximum value of a field (e.g., maximum -- or most
    recent -- date, maximum integer etc). Note, this is different then
    maxLength property.



- **`minimum`** _(integer)_
     Specifies the minimum value of a field.



**`encodings`** _(object)_
 Variable value encodings provide a way to further annotate any value within a any variable type,
making values easier to understand. 


Many analytic software programs (e.g., SPSS,Stata, and SAS) use numerical encodings and some algorithms
only support numerical values. Encodings (and mappings) allow categorical values to be stored as
numerical values.

Additionally, as another use case, this field provides a way to
store categoricals that are stored as  "short" labels (such as
abbreviations).

Examples:


```json

  {'0': 'No', '1': 'Yes'}

```

```json

  {'HW': 'Hello world', 'GBW': 'Good bye world', 'HM': 'Hi, Mike'}

```

**`ordered`** _(boolean)_
 Indicates whether a categorical variable is ordered. This variable  is
relevant for variables that have an ordered relationship but not
necessarily  a numerical relationship (e.g., Strongly disagree < Disagree
< Neutral < Agree).


**`missingValues`** _(array)_
 A list of missing values specific to a variable.

Examples:


```json

  ['Missing', 'Skipped', 'No preference']

```

```json

  ['Missing']

```

**`trueValues`** _(array)_
 For boolean (true) variable (as defined in type field), this field allows
a physical string representation to be cast as true (increasing
readability of the field). It can include one or more values.

Examples:


```json

  ['required', 'Yes', 'Checked']

```

```json

  ['required']

```

**`falseValues`** _(array)_
 For boolean (false) variable (as defined in type field), this field allows
a physical string representation to be cast as false (increasing
readability of the field) that is not a standard false value. It can include one or more values.


**`standardsMappings`** _(array)_
 A published set of standard variables such as the NIH Common Data Elements program.

**`relatedConcepts`** _(array)_
 Mappings to a published set of concepts related to the given field such as ontological information (eg., NCI thesaurus, bioportal etc)

**`univarStats`** _(object)_
 Univariate statistics inferred from the data about the given variable 



- **`median`** _(number)_
     


- **`mean`** _(number)_
     


- **`std`** _(number)_
     


- **`min`** _(number)_
     


- **`max`** _(number)_
     


- **`mode`** _(number)_
     


- **`count`** _(integer)_
     


- **`twentyFifthPercentile`** _(number)_
     


- **`seventyFifthPercentile`** _(number)_
     


- **`categoricalMarginals`** _(array)_
     

