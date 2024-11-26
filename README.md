# Bender-Gestalt Test Dataset

## Executive Summary
The Bender-Gestalt Test (BGT), or Bender Visual-Motor Gestalt Test, is commonly used in pre-employment psychological assessments to evaluate candidates' cognitive and motor skills, particularly visual-motor integration. By reproducing geometric figures, candidates showcase their ability to process and organize visual information. The test can also identify potential neurological or developmental disorders, providing insights into cognitive and emotional functioning that may affect workplace performance.

The Bender-Gestalt Test dataset aims to automate the scoring process of pre-employment psychological assessments. This project addresses the time-consuming and subjective nature of manual BGT evaluations by creating a dataset to train machine learning models for automated scoring.

![Bender-Gestalt Test Example](./dataset/standard/Pattern.png)

## Description of Data
The dataset comprises 20 participant records with:

### Scores Summary:
- 14 scoring parameters
- Total scores
- Diagnosis

### Metadata:
- Age range: 22-57 years
- Nationalities: Argentine, Indian, American, Portuguese, Tunisian, Uruguayan
- Education levels: High School, Bachelor's Degree and Master's Degree

### Images:
- 20 images with the drawing of each participant

### Score:
- 20 csv files containing the detail score calculation per participant


## Power Analysis
- H₀: There is no difference between manually and automatically scored Bender-Gestalt Test results.
- H₁: There is a significant difference between manually and automatically scored results.
- Statistical Test: Two-sample t-test for independent groups, comparing manual and automated scores.
- Effect Size: A large effect size of 0.8 is expected, based on Cohen’s recommendations.
- Statistical Significance Level and Power: Set at 0.05 and 0.80, respectively.
  
The recommended sample size is 52 participants; however, this dataset currently contains 20, representing a shortfall of 32 participants.

## Exploratory Data Analysis
Score Distribution:
- Mean total score: 2.65
- Most common diagnosis: Absence of brain impairment (14 cases)
- Borderline cases: 5
- Strong evidence for brain impairment: 1 case

## Data Collection Protocol
Participants were recruited from Duke University and through social media to ensure broad outreach. Only candidates aged 18 and older were accepted. The data collection process involved the following steps:
1.	Google Form Completion: Participants filled out a Google Form that collects personal information, including age, nationality, highest level of education and whether they have previously taken the Bender-Gestalt Test.
2.	Drawing Task: Participants were instructed to copy the pattern drawing. They will also start a timer to record the time taken to complete the drawing.
3.	Image Upload: After completing the drawing, participants uploaded an image of their work through the Google Form.
4.	Data Storage: All collected data were stored in a Google Sheet linked to the Google Form.
5.	Scoring: Each participant's set of images was manually evaluated based on Lacks' Scoring System criteria outlined in the [scoring table](./dataset/standard/Scoring%20table%20criteria.png).


## Link to access

[Github Repository](https://github.com/iaravagni/Bender-Gestalt-dataset)

[Hugging Face Dataset](https://huggingface.co/datasets/iaravagni/BenderGestalt)


## Ethics Statement
This research:
- Only includes participants aged 18 and older
- Collects minimal personal information
- Ensures voluntary participation
- Maintains data privacy


## License
This project is released under the MIT License, permitting:
- Free use and modification
- Commercial use
- Distribution
- Integration with other software

