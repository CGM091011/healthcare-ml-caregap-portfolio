import pandas as pd
import sqlite3
import logging
from pathlib import Path

# ------------------------
# CONFIG
# ------------------------
RAW_PATH = Path("KaggleV2-May-2016.csv")
PROCESSED_PATH = Path("data/processed/appointments_clean.csv")
DB_PATH = Path("database/healthcare_etl.db")
LOG_PATH = Path("logs/etl.log")

# ------------------------
# CREATE REQUIRED FOLDERS
# ------------------------
PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
DB_PATH.parent.mkdir(parents=True, exist_ok=True)
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

# ------------------------
# LOGGING SETUP
# ------------------------
logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ------------------------
# EXTRACT
# ------------------------
def extract_data():
    logging.info("Starting data extraction")
    df = pd.read_csv(RAW_PATH)
    logging.info(f"Extracted {len(df)} rows")
    return df

# ------------------------
# TRANSFORM
# ------------------------
def transform_data(df):
    logging.info("Starting data transformation")

    # Clean column names
    df.columns = df.columns.str.lower().str.strip().str.replace("-", "_")

    # Convert to datetime
    df["scheduledday"] = pd.to_datetime(df["scheduledday"])
    df["appointmentday"] = pd.to_datetime(df["appointmentday"])

    # Create waiting_days
    df["waiting_days"] = (
        df["appointmentday"].dt.normalize()
        - df["scheduledday"].dt.normalize()
    ).dt.days

    # Filter invalid values + FIX warning
    df = df[(df["age"] >= 0) & (df["waiting_days"] >= 0)].copy()

    # Create age group
    df["age_group"] = pd.cut(
        df["age"],
        bins=[0, 17, 35, 50, 65, 120],
        labels=["0-17", "18-35", "36-50", "51-65", "66+"],
        include_lowest=True
    )

    # Create target flag
    df["no_show_flag"] = df["no_show"].map({"Yes": 1, "No": 0})

    logging.info(f"Transformation complete. Clean rows: {len(df)}")

    return df

# ------------------------
# VALIDATE
# ------------------------
def validate_data(df):
    logging.info("Starting data validation")

    assert df["age"].min() >= 0, "Invalid age found"
    assert df["waiting_days"].min() >= 0, "Invalid waiting_days found"
    assert df["no_show_flag"].isnull().sum() == 0, "Missing no_show_flag values"

    logging.info("Data validation passed")

# ------------------------
# LOAD
# ------------------------
def load_data(df):
    logging.info("Starting data load")

    # Save CSV
    df.to_csv(PROCESSED_PATH, index=False)

    # Save to SQLite
    conn = sqlite3.connect(DB_PATH)
    df.to_sql("clean_appointments", conn, if_exists="replace", index=False)
    conn.close()

    logging.info("Data loaded to CSV and SQLite")

# ------------------------
# RUN PIPELINE
# ------------------------
def run_pipeline():
    logging.info("ETL pipeline started")

    df_raw = extract_data()
    df_clean = transform_data(df_raw)
    validate_data(df_clean)
    load_data(df_clean)

    logging.info("ETL pipeline completed successfully")

    print("ETL pipeline completed successfully.")
    print(f"CSV: {PROCESSED_PATH}")
    print(f"DB: {DB_PATH}")
    print(f"LOG: {LOG_PATH}")

# ------------------------
# ENTRY POINT
# ------------------------
if __name__ == "__main__":
    run_pipeline()
