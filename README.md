# SQLite Lab: CRUD Operations

[![CI](https://github.com/TzRRR/databricks_lab/actions/workflows/cicd.yml/badge.svg)](https://github.com/TzRRR/databricks_lab/actions/workflows/cicd.yml)

## Overview

A Python project for performing a complex SQL query on Databricks database storing airline data.

## Installation

1. **Clone the repository**

   ```bash
   git clone <REPOSITORY_URL>
   cd databricks_lab
   ```

2. **Set up a virtual environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Purpose of the Query:

The query is designed to provide insights into airline safety over two distinct periods (1985-1999 and 2000-2014) by combining data from two tables:

- **AirlineDB1** (containing information on incidents, accidents, and fatalities by airline).
- **AdditionalAirlineDB** (containing additional airline metadata such as airline code and region).

The query aims to:

- **Aggregate incidents and fatalities** over the two periods (1985-1999 and 2000-2014) for each airline.
- **Group the results by airline and region** to calculate the total incidents and fatalities by region.
- **Sort the results** by the total number of incidents and fatalities per region.

## What the Query is Doing:

### Selecting and Aggregating Data:

The query sums up the total number of incidents and fatalities for each airline over the two time periods (`incidents_85_99 + incidents_00_14` for incidents and `fatalities_85_99 + fatalities_00_14` for fatalities).

### Joining Two Tables:

The `JOIN` operation combines data from **AirlineDB1** (containing incident and fatality information) with **AdditionalAirlineDB** (containing metadata such as airline code and region) based on the common `airline` field.

### Grouping Data:

The data is **grouped by airline and region**, which allows for calculating the total number of incidents and fatalities for each airline, and also for calculating the total for each region.

### Filtering Data:

The **HAVING** clause ensures that only airlines with at least one incident are included in the final result. Airlines with zero incidents across both periods are excluded.

### Sorting Data:

The results are **sorted first by the total number of incidents per region** (`total_incidents_per_region`), and in case of a tie, by the total number of fatalities per region (`total_fatalities_per_region`), both in descending order.

### Results:

Row(airline='Air France', total_incidents=20, total_fatalities=416, airline_code='AA', region='Europe', total_incidents_per_region=20, total_fatalities_per_region=416)  
Row(airline='China Airlines', total_incidents=14, total_fatalities=760, airline_code='BB', region='Asia', total_incidents_per_region=14, total_fatalities_per_region=760)  
Row(airline='Gulf Air', total_incidents=4, total_fatalities=143, airline_code='DD', region='South America', total_incidents_per_region=4, total_fatalities_per_region=143)  
Row(airline='Air Canada', total_incidents=4, total_fatalities=0, airline_code='CC', region='North America', total_incidents_per_region=4, total_fatalities_per_region=0)  
Row(airline='Virgin Atlantic', total_incidents=1, total_fatalities=0, airline_code='EE', region='Africa', total_incidents_per_region=1, total_fatalities_per_region=0)
