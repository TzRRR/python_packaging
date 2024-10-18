"""Query the database"""
from databricks.sql import connect
from dotenv import load_dotenv
import os

def query_complex_airline_data():
    """Perform the complex query with joins, aggregation, and sorting in Databricks"""
    
    # Load environment variables
    load_dotenv()
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

        # Perform the complex SQL query
        query = """
        SELECT 
            A.airline, 
            SUM(A.incidents_85_99 + A.incidents_00_14) AS total_incidents, 
            SUM(A.fatalities_85_99 + A.fatalities_00_14) AS total_fatalities, 
            B.airline_code, 
            B.region,
            SUM(A.incidents_85_99 + A.incidents_00_14) AS total_incidents_per_region,
            SUM(A.fatalities_85_99 + A.fatalities_00_14) AS total_fatalities_per_region
        FROM 
            AirlineDB1 A
        JOIN 
            AdditionalAirlineDB B
        ON 
            A.airline = B.airline
        GROUP BY 
            A.airline, B.airline_code, B.region
        HAVING 
            SUM(A.incidents_85_99 + A.incidents_00_14) > 0 
        ORDER BY 
            total_incidents_per_region DESC, 
            total_fatalities_per_region DESC;
        """
        
        # Execute the query
        c.execute(query)
        
        # Fetch and return all the results
        results = c.fetchall()
        c.close()

    return results