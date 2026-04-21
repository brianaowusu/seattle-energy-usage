import pandas as pd
import sqlite3

def export_data():
    conn = sqlite3.connect("energy.db")

    with open("sql/kpi_queries.sql", "r") as file:
        sql_text = file.read()

    queries = sql_text.split("-- kpi:")

    for q in queries:
        if q.strip() == "":
            continue

        lines = q.strip().split("\n")
        kpi_name = lines[0].strip()
        query = "\n".join(lines[1:])

        print(f"Running KPI: {kpi_name}")

        df = pd.read_sql_query(query, conn)

        df.to_csv(f"/Users/bri/Downloads/seattle-energy-usage/data/{kpi_name}.csv", index=False)

    conn.close()

    print("All KPIs exported")

if __name__ == "__main__":
    export_data()