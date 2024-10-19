import pytest
import os
import pandas as pd
from main import extract, load
from mylib.query import query

# Test for the extract function
def test_extract():
    # Call the extract function and check the file is created
    file_path = extract()
    
    assert os.path.exists(file_path), "Extracted file does not exist"
    
    # Check the content of the extracted CSV file
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # Verify the first few lines of the CSV content
    assert len(lines) > 1, "CSV file is empty or incomplete"
    assert "airline" in lines[0], "CSV header is incorrect"
    assert "Aer Lingus" in lines[1], "First row of CSV is not as expected"

# Test for the load function
def test_load():
    # Ensure the load function runs successfully
    result = load()

    assert result == "success", "Load function did not return success"

    # Ensure the datasets have been properly loaded into the database
    # Check the data from the 'airline.csv' file
    df1 = pd.read_csv("airline.csv")
    assert len(df1) > 0, "Data from airline.csv was not loaded correctly"

    # Check the data from the 'airline2.csv' file
    df2 = pd.read_csv("airline2.csv")
    assert len(df2) > 0, "Data from airline2.csv was not loaded correctly"

# Test for the query function
def test_query():
    # Query the database and verify the results
    query_str = "SELECT airline, region FROM AdditionalAirlineDB"
    results = query(query_str)

    assert len(results) > 0, "Query returned no results"

    for row in results:
        print(row)
    
    # Verify the first few results
    assert results[0][0] == "Air Canada", "First airline is incorrect"
    assert results[0][1] == "North America", "First region is incorrect"
    assert results[1][0] == "Virgin Atlantic", "Second airline is incorrect"
    assert results[1][1] == "Africa", "Second region is incorrect"
