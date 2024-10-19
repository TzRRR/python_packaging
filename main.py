"""
ETL-Query script
"""
import click
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query as run_custom_query

@click.group()
def cli():
    """CLI tool for interacting with airline data."""
    pass

@cli.command()
def extract_data():
    """Extract data."""
    extract()

@cli.command()
def transform_load_data():
    """Transform and load the data."""
    load()

@cli.command(name="query")
@click.argument("query_str", nargs=-1)
def run_query(query_str):
    """Run a SQL query."""
    # Join the query arguments into a single string (in case it's split)
    query = " ".join(query_str)
    run_custom_query(query)

if __name__ == '__main__':
    cli()
