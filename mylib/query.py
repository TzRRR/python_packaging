"""Query the database"""
from databricks.sql import connect
from dotenv import load_dotenv
import os

def query(query):
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
        # Execute the query
        c.execute(query)
        
        # Fetch and return all the results
        results = c.fetchall()
        c.close()
    
    for row in results:
        print(row)

    return results