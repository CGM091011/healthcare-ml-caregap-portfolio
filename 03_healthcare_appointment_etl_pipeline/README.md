### 3. Healthcare Appointment ETL Pipeline

Built an automated Python data pipeline to extract, transform, validate, and load raw medical appointment records into a relational database for downstream machine learning.

Skills demonstrated:

    Python Data Engineering (Pandas)

    ETL Pipeline Architecture (Extract, Transform, Validate, Load)

    Data Quality Assurance (Assertions & Automated Validation)

    Feature Engineering (Datetime manipulation, categorical binning)

    Relational Database Integration (SQLite)

    Pipeline Monitoring (Automated logging)

### Project Overview
This project automates the critical data preparation phase for healthcare analytics. It ingests raw medical appointment records, applies business logic to clean the data, engineers new predictive features, and strictly validates the output. The finalized, high-quality dataset is then loaded into a SQLite database, creating a single source of truth for downstream predictive modeling.

Business Problem
Data scientists spend up to 80% of their time cleaning raw data. Healthcare datasets are particularly prone to human entry errors (e.g. appointments scheduled after they already occurred). This pipeline automates the ingestion and cleansing process, acting as a "firewall" to ensure that the No-Show Prediction model only trains on logically sound, validated data.

### Core Output

    Cleaned Database (healthcare_etl.db): A lightweight SQLite database ready for SQL querying.

    Processed CSV: A finalized, tabular dataset ready for direct injection into a Scikit-Learn model.

    Execution Logs (etl.log): An automated audit trail tracking rows processed, validations passed, and execution times.

### Data Source & Engineered Features

    Source: Medical Appointment No Shows dataset (Kaggle).

    Engineered Features:

        waiting_days: The calculated delta between the scheduling date and the actual appointment date.

        age_group: Standardized demographic bins (0-17, 18-35, 36-50, 51-65, 66+).

        no_show_flag: A sanitized binary target variable (1 = Missed, 0 = Attended).

### Architecture & Tools

    Framework: Python (Pandas)

    Design Pattern: ETL with dedicated Validation stage

    Storage Output: SQLite & CSV

    Monitoring: Python built-in logging module

### Data Quality Validations Enforced

    Strict positive-integer checks for patient ages.

    Chronological validation (ensuring waiting_days is never negative).

    Null-value tracking on the primary target flag to prevent model corruption.
