from setuptools import setup, find_packages

setup(
    name="airline_cli_tool",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "databricks-sql-connector",
        "pandas",
        "python-dotenv",
    ],
    entry_points="""
        [console_scripts]
        airline_cli=main:cli
    """,
)
