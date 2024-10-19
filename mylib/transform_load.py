"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products,avg_distance_root,
ingred_normalization_term,semantic_tree_name,semantic_tree_node
"""


import os
import pandas as pd
from databricks.sql import connect
from dotenv import load_dotenv


def load(dataset1="airline.csv", dataset2="airline2.csv"):
    """Transforms and Loads data into the local databricks database"""
    print("Transforming and loading data...")

    # Load data from both CSV files
    df1 = pd.read_csv(dataset1, delimiter=",")
    df2 = pd.read_csv(dataset2, delimiter=",")

    df1['airline'] = df1['airline'].str.replace(r'[^\w\s]', '', regex=True).str.strip()

    # Load environment variables
    load_dotenv()

    # Databricks credentials
    server_h = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("ACCESS_TOKEN")
    http_path = os.getenv("HTTP_PATH")

    # Connect to Databricks SQL Warehouse
    with connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()

        # Create and populate AirlineDB1 from airline.csv
        c.execute("DROP TABLE IF EXISTS AirlineDB1")
        c.execute("""
            CREATE TABLE AirlineDB1 (
                airline STRING,
                avail_seat_km_per_week FLOAT,
                incidents_85_99 INT,
                fatal_accidents_85_99 INT,
                fatalities_85_99 INT,
                incidents_00_14 INT,
                fatal_accidents_00_14 INT,
                fatalities_00_14 INT
            )
        """)
        
        for _, row in df1.iterrows():
            c.execute("""
                INSERT INTO AirlineDB1 (
                    airline, avail_seat_km_per_week, incidents_85_99, 
                    fatal_accidents_85_99, fatalities_85_99, 
                    incidents_00_14, fatal_accidents_00_14, fatalities_00_14
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                row['airline'], 
                row['avail_seat_km_per_week'], 
                row['incidents_85_99'], 
                row['fatal_accidents_85_99'], 
                row['fatalities_85_99'], 
                row['incidents_00_14'], 
                row['fatal_accidents_00_14'], 
                row['fatalities_00_14']
            ))

        # Create and populate AdditionalAirlineDB from additional_airline_data.csv
        c.execute("DROP TABLE IF EXISTS AdditionalAirlineDB")
        c.execute("""
            CREATE TABLE AdditionalAirlineDB (
                airline STRING,
                airline_code STRING,
                region STRING
            )
        """)
        for _, row in df2.iterrows():
            c.execute("""
                INSERT INTO AdditionalAirlineDB (
                    airline, airline_code, region
                ) VALUES (?, ?, ?)
            """, (
                row['airline'], 
                row['airline_code'], 
                row['region']
            ))
        
        # Query the size of AirlineDB1
        c.execute("SELECT COUNT(*) FROM AirlineDB1")
        airline_db1_size = c.fetchone()[0]
        print(f"AirlineDB1 size: {airline_db1_size} rows")

        # Query the size of AdditionalAirlineDB
        c.execute("SELECT COUNT(*) FROM AdditionalAirlineDB")
        additional_airline_db_size = c.fetchone()[0]
        print(f"AdditionalAirlineDB size: {additional_airline_db_size} rows")

        c.close()
    
    print("Data transformation and loading completed.")

    return "success"
