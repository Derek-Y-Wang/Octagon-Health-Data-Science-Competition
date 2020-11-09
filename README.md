# Octagon-Health-Data-Science-Competition
Octagon Health Data Science Competition hosted by the University of Toronto.
November 6th, 2020 - November 9th, 2020

## Scenario
You work for a company called "Octagon Insurance".										
Your boss is wondering how many patients use a TKI for hepatocellular carcinoma and for how long. 										
You are given this dataset containing everyone who used sorafenib from 2016-2019.										
Your director wants your report to include:										
	1. How many patients stay on treatment for at least 9 months?									
	2. What might predict successful therapy?									
	3. What is the monthly rate of discontinuation?									
	4. What are some potential reasons for discontinuation of therapy?						
  
## Introduction
Data science techniques can be used in the medical field to provide useful insights on the effectiveness of treatments. The goal of this project is to find how many Canadians use Sorafenib, a Tyrosine Kinase Inhibitor (TKI) drug, for hepatocellular carcinoma, and for how long. This project explores a dataset of all Canadians who used Sorafenib between 2016 and 2019. The project will aim to look into variables presented in the data and analyze how these variables can lead to success and failure of the drug on the patient.

## Dataset
We are provided with one excel file for the data containing Canadians that have used the Sorafenib drug between 2016 and 2019.
The dataset contain 44 columns which are listed in the following order: 

- **Prov**: Province
- **Con-ACT**: Does patient use another anti-cancer therapy concurrently?
- **Age**: Age
- **Measure**:
  - **Tx**: Treatment
  - **event**: Event
  - **censored**: Censor
- **M0**: Starting treatment (month 0)
- **M1-MX**: Continuing treatment in months following M0

## Assumptions
We are interpreting **Measure-Tx** rows of the dataset as the number of patients being treated in this current study. 
We are interpreting the **Measure-event** as the number of patients that leave the study due to adverse events caused by the drug in question
We are interpreting **Measure-censored** to represent interval censoring, such that we will assume Measure-censored represents the patients who finish the study successfully within the given time period.

## Requirements For Running
- Python 3.6+
- Python Packages:NumPy, Matplotlib.pyplot, scikit-learn

## File Information
These are the files that you should be running
- question_1.py 
	- Analyzes overall patient drop/retenation rate over the course of the treatment time 
- question_2.py 
	- Uses SelectKBest Algorithm inorder to determine which variables are valued the most and correlate heaviest towards successful therapy.
- question_3_4.py
	- Looks at monthly discontinuation rates and uses SelectKBest Algorithm to determine what maybe resulting in the observed disconinuation rates.
- grapher.py 
	- Generates graphs based on given data that can be analyzed

## Technical Details
###### Deeper Look into Questions 2 and 4
In both cases we need to determine the dependence between each factor in the dataset and the success percentage. To do this, we used the chi-square test along with scikit-learn’s SelectKBest implementation. We then determined which values for the most correlated features provide the greatest chance of success. With the given results we then used scikit-learn’s LinearRegression model, which performs linear regression on the most correlated factors against the success rate. However we realized that some optimal results occurred in values like “ALL”, “UNKWN” or “Null”, but excluded these results as they do not provide specific conclusive results.

**For more results on our findings refer to the [pdf](OctagonDataScienceCompetitionResults.pdf)**


