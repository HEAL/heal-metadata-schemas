# HEAL Platform Study

*A study hosted and indexed on the HEAL Platform*

## Properties

- **`minimal_info`** *(object)*
  - **`study_name`** *(string)*: The title or name of the study. For NIH-funded studies, this will generally be equivalent to the NIH application ID title.
  - **`study_description`** *(string)*: A description of or abstract for the study. For NIH-funded studies , this will generally be equivalent to the NIH application ID abstract text.
  - **`study_nickname`** *(string)*: Study nickname, alternative title, abbreviation, or acronym (e.g. many people shorten the name of the HEAL Adolescent Brain Cognitive Development study to ABCD).
- **`metadata_location`** *(object)*
  - **`nih_application_id`** *(string)*: NIH application ID; only applicable if study is funded by NIH.
  - **`nih_reporter_link`** *(string)*: URL link to the NIH application ID NIH RePORTER webpage; only applicable if study is funded by NIH. Refer to *#/definitions/saneUrl*.
  - **`clinical_trials_study_ID`** *(string)*: ClinicalTrials.gov study ID; only applicable if study is a reportable clinical trial and registered on ClinicalTrials.gov.
  - **`data_repositories`** *(array)*: Describe the data repositories to which data or other shareable products produced by the study will be submitted by the study authors and stored for long-term access; one item in this array per repository.
    - **Items** *(object)*
      - **`repository_name`** *(string)*: Name of a repository in which data or other shareable research products are submitted for storage by study author.
      - **`repository_study_ID`** *(string)*: Unique identifier assigned to the study at that repository; usually a number or combination of standard letters and numbers (e.g. study identifiers on ClinicalTrials.gov are generally in the format: NCT12345678).
      - **`repository_persistent_ID`** *(string)*: Unique persistent identifier assigned to the study at that repository; usually a doi.
      - **`repository_citation`** *(string)*: The official citation the repository requests be used to cite the study/data when the study/data is discovered/accessed via the repository; will likely follow the format: Principal Investigator(s). Title. Place-of-Distribution and Distributor, Date-of-Distribution. DOI. version (where distributor will be the repository name).
  - **`cedar_study_level_metadata_template_instance_ID`** *(string)*: ID of the CEDAR HEAL Study-level Core Metadata Template instance created for this study.
  - **`other_study_websites`** *(array)*: any other websites officially associated with this study that provide additional information about the study.
    - **Items** *(string)*: Refer to *#/definitions/saneUrl*.
- **`citation`** *(object)*
  - **`heal_funded_status`** *(boolean)*: Whether or not the study is funded by the NIH HEAL initiative.
  - **`study_collection_status`** *(boolean)*: Whether or not the study is related to a study group or collection(s) by some administrative mechanism, or belongs to a group or collection of studies (e.g. SAMHSA performs a survey called the National Survey of Substance Abuse Treatment Services (N-SSATS) every year; each annual survey may be registered as a separate study that belongs to a collection called the N-SSATS collection).
  - **`study_collections`** *(array)*: If this study belongs to a study group or collection(s), this is the name or identifier of the study group or collection(s) (e.g. SAMHSA performs a survey called the National Survey of Substance Abuse Treatment Services (N-SSATS) every year; each annual survey may be registered as a separate study that belongs to a collection called the N-SSATS collection).
    - **Items** *(string)*
  - **`funding`** *(array)*: Describe the grants and other funding supporting the study; one item in this array per grant/award or funding source.
    - **Items** *(object)*
      - **`funder_name`** *(array)*: Name of a the granting agency or organization funding the study; include sub-agency administrative entity as second element in array if applicable (e.g. National Institute of Health, National Institute on Drug Abuse).
        - **Items** *(string)*
      - **`funder_abbreviation`** *(array)*: Abbreviation for the name of the granting agency or organization funding the study; include abbreviation for sub-agency administrative entity as second element in array if applicable (e.g. NIH, NIDA).
        - **Items** *(string)*
      - **`funder_type`** *(string)*: Type of granting agency or organization funding the study. Must be one of: `['governmental', 'non-governmental, non-profit, not corporate affiliated', 'non-governmental, non-profit, corporate affiliated', 'non-governmental, for-profit']`.
      - **`funder_geographic_reach`** *(string)*: The geographic reach of the granting agency or organization funding the study. Must be one of: `['international', 'national - non-US', 'national - US', 'state - US', 'local - US']`.
      - **`funding_award_ID`** *(string)*: The grant award ID or number. For NIH-funded studies this will be the project or award number and is distinct from the NIH application ID.
      - **`funding_award_name`** *(string)*: The grant award name. For NIH-funded studies this will be the project or award name and is distinct from the name or title associated with the NIH application ID.
  - **`investigators`** *(array)*: Describe the primary and co-investigators of the study; one item in this array per investigator.
    - **Items** *(object)*
      - **`investigator_first_name`** *(string)*: First name of study primary or co-investigator.
      - **`investigator_middle_initial`** *(string)*: Middle initial of study primary or co-investigator.
      - **`investigator_last_name`** *(string)*: Last name of study primary or co-investigator.
      - **`investigator_affiliation`** *(string)*: Institutional affiliation of study primary or co-investigator.
      - **`investigator_ID`** *(array)*: Add a structured identifier(s) for the investigator; one item in this array per structured identifier; e.g. one item for providing ORCID, another for providing RAS passport.
        - **Items** *(object)*
          - **`investigator_ID_type`** *(string)*: Type of identifier that will be provided. Must be one of: `['internal NIH RePORTER ID', 'doi', 'ORCID', 'eRA Commons ID', 'RAS Passport']`.
          - **`investigator_ID_value`** *(string)*: Value of the identifier of the type specified by ID_type.
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
  - **`produce_data`** *(boolean)*: Indicate whether or not the study will collect/produce (primary or secondary) data.
  - **`data_available`** *(string)*: If study will collect/produce data, indicate whether all, some, or none of the data will be made available. Must be one of: `['all', 'some', 'none']`.
  - **`data_restricted`** *(string)*: If study will collect/produce data, and make at least some of that data available, indicate whether all, some, or none of the data will have restriction(s) on access beyond acknowledgement and signing of a minimal DSA. Must be one of: `['all', 'some', 'none']`.
  - **`data_collection_status`** *(string)*: If study will collect/produce data, indicate whether the study has not started, has started, or has finished data collection/production activities. Must be one of: `['not started', 'started', 'finished']`.
  - **`data_release_status`** *(string)*: If the study will collect/produce data and make at least some of the data available, indicate whether the study has not started, has started, or has finished data release activities. Must be one of: `['not started', 'started', 'finished']`.
  - **`data_collection_start_date`** *(string)*: If the study will collect/produce data, indicate the anticipated date when data collection/production will begin.
  - **`data_collection_finish_date`** *(string)*: If the study will collect/produce data, indicate the anticipated date when data collection/production will end (data collection/production is complete).
  - **`data_release_start_date`** *(string)*: If study will collect/produce data and make at least some of the data available, indicate the anticipated date when first data will be released.
  - **`data_release_finish_date`** *(string)*: If study will produce data and make at least some of the data available, indicate the anticipated date when last data will be released (data release is complete).
  - **`produce_other`** *(boolean)*: Indicate whether or not the study will produce shareable products other than data.
## Definitions

- **`saneUrl`**

