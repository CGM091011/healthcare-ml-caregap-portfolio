# HEDIS Care Gap Outreach Prioritization Using Machine Learning

## Project Overview

This project uses a synthetic healthcare dataset to build a machine learning model that predicts whether a patient is likely to have an unresolved care gap and should be prioritized for outreach.

The dataset is synthetic and does not contain PHI. It was designed to reflect common healthcare quality and HEDIS-related workflows, including A1c testing, blood pressure control, diabetic eye exams, kidney health evaluation, appointment status, emergency utilization, and due date timing.

## Business Problem

Population health and quality teams often manage large lists of patients with open care gaps. Outreach resources are limited, so teams need a way to identify which patients should be contacted first.

This model helps prioritize patients based on clinical indicators, appointment history, utilization, and measure type.

## Target Variable

care_gap_unresolved

- 1 = patient likely has an unresolved care gap
- 0 = patient is lower priority or likely closed the gap

## Features Used

- Age
- Gender
- Diabetes status
- HEDIS measure type
- A1c value
- A1c category
- Systolic blood pressure
- Diastolic blood pressure
- BMI
- eGFR availability
- Microalbumin availability
- Eye exam completion
- Upcoming appointment status
- Days until due date
- Prior emergency visits
- Last cancelled appointment
- Current admission status
- Language
- Clinic location
- Care gap flag

## Models Used

- Logistic Regression
- Random Forest
- Gradient Boosting

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion matrix

## Key Healthcare Consideration

Recall was prioritized because false negatives are costly in outreach workflows. A false negative means a patient with an unresolved care gap may not be contacted.

## Business Value

The model can help healthcare organizations:

- Prioritize outreach
- Improve care gap closure
- Support HEDIS performance
- Improve value-based care outcomes
- Identify patients needing appointment scheduling, lab completion, or care coordination

## Tools Used

Python, pandas, NumPy, scikit-learn, matplotlib, machine learning, healthcare analytics, HEDIS quality measures.

## Disclaimer

This project uses synthetic data only. No real patient data or PHI was used.