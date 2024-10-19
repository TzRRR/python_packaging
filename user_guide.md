# airline_cli Script User Guide

## Overview

The airline_cli script is a command-line interface (CLI) tool that performs Extract, Transform, Load (ETL) operations and executes general queries. This guide provides instructions on how to use the script effectively.

## Startup

To access the cli command tool you would need to run setup.py by typing:

```bash
chmod +x setup.sh
./setup.sh
```

By doing so, we can now run the project as an executable via `airline_cli`

## Usage

### Running the Script

To run the airline_cli script, use the following command:

```bash
airline_cli <action>
```

### Available Actions

The script supports the following actions:

- `extract`: Extract data
- `transform_load`: Transform and load data
- `query`: Execute a general query

## Examples

### Extract Data

```bash
airline_cli extract
```

This command will extract data.

### Transform and Load Data

```bash
airline_cli transform_load
```

This command will transform and load data.

### Execute General Query

```bash
airline_cli query <query>
```

Replace `<query>` with the specific query you want to execute.

## Notes

- Ensure that you have the required dependencies installed before running the script.
