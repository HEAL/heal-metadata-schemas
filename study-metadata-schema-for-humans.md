# HEAL Platform Study

*A study hosted and indexed on the HEAL Platform*

## Properties

- **`minimal_info`** *(object)*
  - **`study_name`** *(string)*: Generally equivalent to the NIH application ID title.
  - **`study_description`** *(string)*: Generally equivalent to the NIH application ID abstract text.
  - **`study_nickname`** *(string)*: Study nickname or alternative title.
- **`metadata_location`** *(object)*
  - **`nih_application_id`** *(string)*: NIH application ID; only applicable if study is funded by NIH.
  - **`nih_reporter_link`** *(string)*: URL link to the NIH application ID NIH RePORTER webpage; only applicable if study is funded by NIH. Refer to *#/definitions/saneUrl*.
  - **`clinical_trials_study_ID`** *(string)*: ClinicalTrials.gov study ID; only applicable if study is a reportable clinical trial and registered on ClinicalTrials.gov.
  - **`data_repositories`** *(array)*
    - **Items** *(object)*
      - **`repository_name`** *(string)*: Name of a repository in which data or other shareable research products are submitted for storage by study author.
      - **`repository_study_ID`** *(string)*: Study unique identifier at that repository.
      - **`repository_doi`** *(string)*: Study unique persistent identifier at that repository; usually a doi.
  - **`cedar_study_level_metadata_template_instance_ID`** *(string)*: ID of the CEDAR HEAL Study-level Core Metadata Template instance created for this study.
  - **`other_study_websites`** *(array)*: enter any other websites officially associated with this study that provide additional information about the study.
    - **Items** *(string)*: Refer to *#/definitions/saneUrl*.
## Definitions

- **`saneUrl`**

