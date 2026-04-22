# Seattle Energy Use Analytics Pipeline

An end-to-end data pipeline that processes and analyzes building energy benchmarking data to generate insights on energy efficiency, emissions, and consumption trends.

This project simulates a real-world utility analytics workflow similar to those used by municipal energy providers.

---

## 📌 Project Overview

This project ingests raw building energy data, performs data cleaning and validation, stores the processed data in a SQL database, and generates key performance indicators (KPIs) for visualization in Tableau Public.

The goal is to demonstrate data engineering and analytics skills, including ETL pipelines, SQL transformations, and data visualization.

---

## 📊 Tableau Dashboard
(https://public.tableau.com/views/SeattleEnergyUse/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

---

## 🛠️ Tech Stack

- Python (pandas)
- SQL (SQLite)
- Tableau Public
- Git


---

## ⚙️ Pipeline Steps

1. **Data Cleaning**
   - Remove duplicates and invalid values  
   - Handle missing data  
   - Standardize formats  

2. **Data Validation**
   - Schema checks  
   - Range validation  
   - Data quality checks  

3. **Data Storage**
   - Load cleaned data into SQLite database  

4. **KPI Generation**
   - Execute SQL queries to calculate metrics  
   - Export results as CSV files  

5. **Visualization**
   - Connect CSV outputs to Tableau Public  
   - Build interactive dashboards  

---

## 📊 Key KPIs

- Energy Use Intensity (EUI) by neighborhood and property type
- Emissions Intensity by property type
- Energy consumption trends over time
- Efficiency by property type
- Top efficient and inefficient buildings

---

## 🔍 Key Insights

- Identified significant variation in energy usage across building types  
- Found that a small subset of buildings contributes disproportionately to total emissions  
- Observed trends indicating gradual improvements in energy efficiency over time  
- Automated KPI generation reduced manual analysis effort and improved consistency  

---

## 🚀 How to Run the project

1. Clone the repository  
2. Place raw dataset in `data/raw/`  
3. Run the pipeline: `python scripts/etl_pipeline_runner.py`
4. Open Tableau Public and connect to files in `data/analytics/`

---

## 💡 Future Improvements

- Integrate PostgreSQL or cloud data warehouse (e.g., AWS Redshift)  
- Add pipeline scheduling (Airflow orchestration) 
- Implement automated alerts for data quality issues  
- Expand KPI set for deeper analysis  

---

## 👤 Author

Briana Oppong-Owusu

## License
<!--
 Copyright 2026 brianaowusu
 
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 
     https://www.apache.org/licenses/LICENSE-2.0
 
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
------- b182b8e (other updates)