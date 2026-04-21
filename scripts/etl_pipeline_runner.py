import pandas as pd
from data_cleaning import clean_data
from data_validation import validate_data
from load_to_sql import load_to_sql
from export_to_csv import export_data

def run_pipeline():
    print("Starting pipeline...")
    # Transform
    # Clean data
    clean_data()
    # Validate data
    validate_data()

    #Load in SQL
    load_to_sql()
    
    #Export KPIs to csv file
    export_data()
    print("Pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()