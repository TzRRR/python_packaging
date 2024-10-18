import pandas as pd


def generate_additional_airline_data(output_file="additional_airline_data.csv"):
    # Define the additional data to be joined with the original airline data
    additional_data = {
        "airline": [
            "Air France",
            "China Airlines",
            "Air Canada",
            "Gulf Air",
            "Virgin Atlantic",
        ],
        "airline_code": ["AA", "BB", "CC", "DD", "EE"],
        "region": ["Europe", "Asia", "North America", "South America", "Africa"],
    }

    # Create a DataFrame from the additional data
    df_additional = pd.DataFrame(additional_data)

    # Save the DataFrame to a CSV file
    df_additional.to_csv(output_file, index=False)

    return f"Additional airline data saved to {output_file}"


# Generate the additional airline data CSV
generate_additional_airline_data("./airline2.csv")
