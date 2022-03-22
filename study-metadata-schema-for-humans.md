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
      - **`repository_persistent_ID`** *(string)*: Study unique persistent identifier at that repository; usually a doi.
      - **`repository_citation`** *(string)*: The official citation the repository requests be used to cite the study/data when the study/data is discovered/accessed via the repository; will likely follow the format: Principal Investigator(s). Title. Place-of-Distribution and Distributor, Date-of-Distribution. DOI. version (where distributor will be the repository name).
  - **`cedar_study_level_metadata_template_instance_ID`** *(string)*: ID of the CEDAR HEAL Study-level Core Metadata Template instance created for this study.
  - **`other_study_websites`** *(array)*: any other websites officially associated with this study that provide additional information about the study.
    - **Items** *(string)*: Refer to *#/definitions/saneUrl*.
- **`citation`** *(object)*
  - **`heal_funded_status`** *(boolean)*: Whether or not the study is funded by the NIH HEAL initiative.
  - **`study_collection_status`** *(boolean)*: Whether or not the study is related to other studies by some administrative mechanism.
  - **`study_collections`** *(array)*: Name or Identifier of the study group or collection(s) this study is related to by some administrative mechanism.
    - **Items** *(string)*
  - **`funding`** *(array)*: Describe the grants and other funding supporting the study; one item in this array per grant/award or funding source.
    - **Items** *(object)*
      - **`funder_name`** *(array)*: Name of a the granting agency or organization funding the study; include sub-agency administrative entity as second element in array if applicable (e.g. National Institute of Health, National Institute on Drug Abuse).
        - **Items** *(string)*
      - **`funder_abbreviation`** *(array)*: Abbreviation for the name of the granting agency or organization funding the study; include abbreviation for sub-agency administrative entity as second element in array if applicable (e.g. NIH, NIDA).
        - **Items** *(string)*
      - **`funder_type`** *(string)*: Type of granting agency or organization funding the study. Must be one of: `['governmental', 'non-governmental, non-profit, not corporate affiliated', 'non-governmental, non-profit, corporate affiliated', 'non-governmental, for-profit']`.
      - **`funder_geographic_reach`** *(string)*: The geographic reach of the granting agency or organization funding the study. Must be one of: `['international', 'national - non-US', 'national - US', 'state - US', 'local - US']`.
      - **`funding_award_ID`** *(string)*: The grant award ID or number.
      - **`funding_award_name`** *(string)*: The grant award name.
  - **`investigators`** *(array)*: Describe the primary and co-investigators of the study; one item in this array per investigator.
    - **Items** *(object)*
      - **`investigator_first_name`** *(string)*: First name of study primary or co-investigator.
      - **`investigator_middle_initial`** *(string)*: Middle initial of study primary or co-investigator.
      - **`investigator_last_name`** *(string)*: Last name of study primary or co-investigator.
      - **`investigator_ID`** *(array)*: Add a structured identifier(s) for the investigator; one item in this array per structured identifier; e.g. one item for providing ORCID, another for providing RAS passport.
        - **Items** *(object)*
          - **`ID_type`** *(string)*: Type of identifier that will be provided. Must be one of: `['internal NIH RePORTER ID', 'doi', 'ORCID', 'eRA Commons ID', 'RAS Passport']`.
          - **`ID_value`** *(string)*: Value of the identifier of the type specified by ID_type.
  - **`heal_platform_persistent_ID`** *(string)*: Persistent identifier assigned to the study on the HEAL Platform; probably a HEAL Platform-branded doi.
  - **`heal_platform_citation`** *(string)*: The official citation the HEAL Platform will request be used to cite the study/data when the study/data is discovered/accessed via the Platform; will likely follow the format: Principal Investigator(s). Title. Place-of-Distribution and Distributor, Date-of-Distribution. DOI. version (where distributor will be: Platform via [Repository Name]).
- **`contacts_and_registrants`** *(object)*
  - **`contacts`** *(array)*: Describe the contact person(s) for the study. This is the person(s) who should be contacted for questions about the study; will be auto-set as NIH contact PI(s) if NIH-funded; one item in this array per contact person.
    - **Items** *(object)*
      - **`contact_first_name`** *(string)*: First name of study contact.
      - **`contact_middle_initial`** *(string)*: Middle initial of study contact.
      - **`contact_last_name`** *(string)*: Last name of study contact.
      - **`contact_affiliation`** *(string)*: Institutional affiliation of study contact.
      - **`contact_email`** *(string)*: Institutional email of study contact.
  - **`registrants`** *(array)*: Describe the person(s) who will register the study on the HEAL Platform. This person(s) must be authorized to access the study registration page/process on the HEAL Platform; will be auto-set as NIH contact PI(s) if NIH-funded; one item in this array per registrant.
    - **Items** *(object)*
      - **`registrant_first_name`** *(string)*: First name of study registrant.
      - **`registrant_middle_initial`** *(string)*: Middle initial of study registrant.
      - **`registrant_last_name`** *(string)*: Last name of study registrant.
      - **`registrant_affiliation`** *(string)*: Institutional affiliation of study registrant.
      - **`registrant_email`** *(string)*: Institutional email of study registrant.
- **`data_availability`** *(object)*
  - **`produce_data`** *(boolean)*: Indicate whether or not the study will produce (primary or secondary) data.
  - **`data_available`** *(string)*: If study will produce data, indicate whether all, some, or none of the data will be made available. Must be one of: `['all', 'none', 'some']`.
  - **`data_restricted`** *(string)*: If study will produce data, and make at least some of that data available, indicate whether all, some, or none of the data will have restriction(s) on access beyond acknowledgement and signing of a minimal DSA. Must be one of: `['all', 'none', 'some']`.
  - **`data_collection_status`** *(string)*: If study will produce data, indicate whether the study has not started, has started, or has finished data collection activities. Must be one of: `['not started', 'started', 'finished']`.
  - **`data_release_status`** *(string)*: If study will produce data and make at least some of the data available, indicate whether the study has not started, has started, or has finished data release activities. Must be one of: `['not started', 'started', 'finished']`.
  - **`data_release_start_date`** *(string)*: If study will produce data and make at least some of the data available, indicate the anticipated date when first data will be released. Must be one of: `['not started', 'started', 'finished']`.
  - **`produce_other`** *(boolean)*: Indicate whether or not the study will produce shareable products other than data.
## Definitions

- **`saneUrl`**

