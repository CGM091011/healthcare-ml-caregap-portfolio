### 2. Patient No-Show Prediction

Built a machine learning model to predict whether a patient will miss a scheduled medical appointment and should be prioritized for outreach.

Skills demonstrated:
- Feature engineering (SDOH, behavioral patterns)
- Classification modeling
- Model evaluation (ROC-AUC, Recall, F1-score)
- Healthcare quality analytics
- Patient risk stratification
- Appointment adherence analysis

### Project Overview
This project uses a synthetic healthcare dataset to build a machine learning model that predicts whether a patient is likely to miss an appointment. By identifying high-risk patients, healthcare providers can prioritize outreach to reduce no-show rates.

### Business Problem
Healthcare organizations struggle with no-show patients, which impacts both operational efficiency and patient care. This model helps healthcare teams identify patients who are most likely to miss appointments so that they can be contacted and reminded.

### Target Variable
**no_show_binary**
- 1: Patient likely to miss appointment
- 0: Patient will attend appointment

### Features Used
- Age
- Gender
- Scholarship status
- Hypertension
- Diabetes
- Alcoholism
- Handicap status
- SMS reminder received
- Waiting days
- SDOH features (financial strain, transportation barriers, etc.)
- Zip code (geographic feature)

### Models Used
- Logistic Regression
- Random Forest
- Gradient Boosting

### Evaluation Metrics
- **Accuracy**
- **Precision**
- **Recall**
- **F1-score**
- **ROC-AUC**

### Key Healthcare Consideration
Recall was prioritized because false negatives are costly in outreach workflows. A false negative means a patient who is likely to miss an appointment may not receive a reminder and might not show up.

### Business Value
This model can help healthcare organizations:
- Prioritize outreach for high-risk patients
- Improve appointment adherence
- Support healthcare quality measures and value-based care
- Optimize scheduling and reduce missed appointments

### Tools Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

### Outputs
- Model predictions (CSV format)
- Cleaned dataset (CSV format)
- Model comparison (CSV format)

### Future Work
Future improvements include adding more granular features (e.g., past medical history, medication adherence) and incorporating real-world data for better generalization.
