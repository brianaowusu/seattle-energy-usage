import pandas as pd
from sqlalchemy import create_engine

def load_to_sql():
    # Load cleaned data
    df = pd.read_csv("/Users/bri/Downloads/seattle-energy-usage/data/energy_usage_cleaned.csv")

    # Connect to PostgreSQL
    engine = create_engine("sqlite:///energy.db")

    # Load into SQL table
    df.to_sql(
        "energy_cleaned",
        engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded into SQLite")

if __name__ == "__main__":
    load_to_sql()