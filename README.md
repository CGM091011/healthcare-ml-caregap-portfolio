# Healthcare Analytics Portfolio: From Data Pipelines to Predictive Modeling

This portfolio is dedicated to solving operational and clinical challenges in healthcare through advanced analytics. By combining scalable data engineering architectures with machine learning, these projects illustrate how to ingest complex government and clinical datasets, ensure data quality, and build predictive models that prioritize patient outreach (HEDIS), reduce wasted resources, and improve health outcomes.

## Projects

### 1. HEDIS Care Gap Outreach Prioritization

Built a machine learning model to predict whether a patient is likely to have an unresolved care gap and should be prioritized for outreach.

Skills demonstrated:

- Synthetic healthcare data generation
- Feature engineering
- Classification modeling
- Missing value imputation
- Model evaluation
- Healthcare quality analytics
- HEDIS care gap logic
- Outreach prioritization

### 2. Patient No-Show Prediction

Built a machine learning model to predict whether a patient will miss a scheduled medical appointment and should be prioritized for outreach.

Skills demonstrated:

- Feature engineering (SDOH, behavioral patterns)
- Classification modeling
- Model evaluation (ROC-AUC, Recall, F1-score)
- Healthcare quality analytics
- Patient risk stratification
- Appointment adherence analysis

### 3. Healthcare Data Engineering Pipeline

Built a Python-based ETL pipeline to extract, transform, validate, and load healthcare appointment data into a structured SQLite database for downstream analytics.

Skills demonstrated:

- Data extraction and ingestion (CSV → pipeline)
- Data cleaning and transformation (Pandas)
- Data validation and quality checks
- Database loading (SQLite)
- Logging and pipeline monitoring
- Reproducible data workflow design


### 4. Medicare Part D Big Data Pipeline

Built an end-to-end PySpark data pipeline to ingest, clean, and aggregate large-scale government healthcare data using the Medallion Architecture.

Skills demonstrated:

    Distributed data processing (PySpark)

    Medallion Architecture design (Bronze, Silver, Gold)

    Large-scale data cleaning and aggregation

    Infrastructure and memory optimization

    Columnar data storage (Parquet)

## Background

This portfolio is designed around healthcare analytics workflows such as A1c monitoring, blood pressure control, kidney health evaluation, diabetic eye exams, appointment scheduling, care gap closure, and population health outreach.

## Tools & Technologies

* **Languages & Core Libraries:** Python, pandas, NumPy, SQL (SQLite)
* **Big Data & Data Engineering:** Apache Spark (PySpark), Parquet, Medallion Architecture
* **Machine Learning & Analytics:** scikit-learn, matplotlib, Streamlit, Healthcare Analytics
* **Environment & Infrastructure:** JupyterHub, Java (JDK 11)
