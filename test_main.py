from mylib.query import query_complex_airline_data


results = query_complex_airline_data()


def test_query_result_length():
    """Test that the length of the query result is correct"""
    expected_length = 5  # The expected length based on the result data
    assert (
        len(results) == expected_length
    ), f"Expected {expected_length} rows, but got {len(results)}."


def test_first_row_contents():
    """Test that the first row of the query result matches expected values"""
    first_row = results[0]

    assert first_row.airline == "Air France"
    assert first_row.total_incidents == 20
    assert first_row.total_fatalities == 416
    assert first_row.airline_code == "AA"
    assert first_row.region == "Europe"
    assert first_row.total_incidents_per_region == 20
    assert first_row.total_fatalities_per_region == 416


# def test_create():
#     """Test inserting a new row into the database"""
#     create("Airline C", 3000000, 4, 1, 20, 2, 1, 50, db_name=TEST_DB)
#     result = query(db_name=TEST_DB)
#     assert len(result) == 3, "Create did not add a new row"
#     assert result[2][0] == "Airline C", "New airline name does not match expected"


# def test_update():
#     """Test updating an existing row in the database"""
#     update("Airline A", 5, db_name=TEST_DB)
#     result = query(db_name=TEST_DB)
#     updated_row = next(row for row in result if row[0] == "Airline A")
#     assert (
#         updated_row[5] == 5
#     ), "Update did not change the incidents_00_14 value correctly"


# def test_delete():
#     """Test deleting a row from the database"""
#     delete("Airline B", db_name=TEST_DB)
#     result = query(db_name=TEST_DB)
#     assert len(result) == 2, "Delete did not remove the row correctly"
#     assert not any(
#         row[0] == "Airline B" for row in result
#     ), "Deleted airline still found in the table"
