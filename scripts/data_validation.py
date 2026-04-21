import pandas as pd
import numpy as np

def validate_data():
    df = pd.read_csv("/Users/bri/Downloads/seattle-energy-usage/data/energy_usage_cleaned.csv", low_memory=False)
    missing_values = df.isnull().sum()
    missing_values
    df.duplicated()

    df["electricity_kwh"] = pd.to_numeric(df["electricity_kwh"], errors="coerce")
    df["site_eui"] = pd.to_numeric(df["site_eui"], errors="coerce")
    df["source_eui"] = pd.to_numeric(df["source_eui"], errors="coerce")
    df["gross_floor_area"] = pd.to_numeric(df["gross_floor_area"], errors="coerce")
    df["total_emissions"] = pd.to_numeric(df["total_emissions"], errors="coerce")
   
if __name__ == "__main__":
    validate_data()