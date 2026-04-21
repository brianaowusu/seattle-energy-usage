CREATE TABLE energy_cleaned (
    building_id INT,
    year INT,
    property_type VARCHAR(100),
    gross_floor_area FLOAT,
    site_eui FLOAT,
    source_eui FLOAT,
    electricity_kwh FLOAT,
    total_emissions FLOAT,
    efficiency_score FLOAT
);

SELECT * FROM CREATE TABLE energy_cleaned;
