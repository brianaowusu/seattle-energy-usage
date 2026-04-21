import pandas as pd
def clean_data():
    df = pd.read_csv("/Users/bri/Downloads/seattle-energy-usage/data/Building_Energy_Benchmarking_Data,_2015-Present_20260416.csv", low_memory=False)
    
    # Clean electricity kwh
    df.rename(columns={'Electricity(kWh)': 'electricity_kwh'}, inplace=True)
    df["electricity_kwh"] = (
        df["electricity_kwh"]
        .str.replace(",", "")
        .astype(str)
    )
    df["electricity_kwh"] = pd.to_numeric(df["electricity_kwh"], errors="coerce")

    # Clean Site EUI
    df.rename(columns={'SiteEUI(kBtu/sf)': 'site_eui'}, inplace=True)
    df["site_eui"] = (
        df["site_eui"]
        .str.replace(",", "")
        .astype(str)
    )
    df["site_eui"] = pd.to_numeric(df["site_eui"], errors="coerce")

    # Clean Source EUI
    df.rename(columns={'SourceEUI(kBtu/sf)': 'source_eui'}, inplace=True)
    df["source_eui"] = (
        df["source_eui"]
        .str.replace(",", "")
        .astype(str)
    )
    df["source_eui"] = pd.to_numeric(df["source_eui"], errors="coerce")
   
   # Clean Gross floor Area
    df.rename(columns={'PropertyGFATotal': 'gross_floor_area'}, inplace=True)
    df["gross_floor_area"] = (
        df["gross_floor_area"]
        .str.replace(",", "")
        .astype(str)
    )
    df["gross_floor_area"] = pd.to_numeric(df["gross_floor_area"], errors="coerce")
    
    # Clean Total Emissions
    df.rename(columns={'TotalGHGEmissions': 'total_emissions'}, inplace=True)
    df["total_emissions"] = (
        df["total_emissions"]
        .astype(str)
        .str.replace(",", "")
    )
    df["total_emissions"] = pd.to_numeric(df["total_emissions"], errors="coerce")

    # Create efficiency score
    df['efficiency_score'] = df['site_eui'] / df['gross_floor_area']

     # Create emissions intensity scale
    df['emissions_intensity'] = df['total_emissions'] / df['gross_floor_area']

    # Clean year
    df.rename(columns = {'DataYear' : 'year'}, inplace=True)

    # Clean Building ID
    df.rename(columns ={'OSEBuildingID' : 'building_id'}, inplace=True)

    # Clean Building Type
    df.rename(columns ={'BuildingType' : 'property_type'}, inplace=True)
    
    # Drop null values
    df.dropna()

    # Drop duplicate values 
    df.drop_duplicates()

    # Drop all other values
    cols_to_keep = ['building_id', 'year', 'property_type', 'gross_floor_area', 'site_eui', 'source_eui', 'electricity_kwh', 'total_emissions', 'efficiency_score']
    df_filtered = df[cols_to_keep]

    # Save cleaned data as csv file
    df_filtered.to_csv('/Users/bri/Downloads/seattle-energy-usage/data/energy_usage_cleaned.csv', index=False)

if __name__ == "__main__":
    clean_data()
