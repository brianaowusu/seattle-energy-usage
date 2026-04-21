-- kpi: Average_efficiency
SELECT building_id,
       site_eui
FROM energy_cleaned;

-- kpi: energy_trend_over_time
SELECT year, 
        AVG(site_eui) AS avg_eui 
FROM energy_cleaned
GROUP BY year
ORDER BY year;

-- kpi: Average_efficiency_by_property_type
SELECT property_type,
       AVG(site_eui) AS avg_eui
FROM energy_cleaned
GROUP BY property_type
ORDER BY avg_eui;

-- kpi: Average_Emissions_over_time
SELECT year,
       SUM(total_emissions) as total_emissions
FROM energy_cleaned
GROUP BY year
ORDER BY year;

-- kpi: Average_Emissions_by_property_type
SELECT property_type,
       SUM(total_emissions) as total_emissions
FROM energy_cleaned
GROUP BY property_type
ORDER BY year;

-- kpi: Energy_efficient_buildings
SELECT building_id, site_eui
FROM energy_cleaned
ORDER BY site_eui ASC
LIMIT 10; 

-- kpi: Energy_inefficient_buildings
SELECT building_id, site_eui
FROM energy_cleaned
ORDER BY site_eui DESC
LIMIT 10;

-- kpi: Outliers 
SELECT 
    COUNT(*) FILTER (WHERE site_eui > 200) * 1.0 / COUNT(*) AS outlier_rate
FROM energy_cleaned;