"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query_complex_airline_data

# Extract
print("Extracting data...")
extract()

# Transform and load
print("Transforming data...")
load()


results = query_complex_airline_data()
for row in results:
    print(row)


# # Create new entry
# create("Test Airline", 5000000, 2, 1, 100, 3, 1, 150)

# # Update existing entry
# update("Test Airline", 5)

# # Delete entry
# delete("Test Airline")
