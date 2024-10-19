#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv myenv

# Activate the virtual environment
echo "Activating virtual environment..."
source myenv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install required dependencies from requirements.txt
echo "Installing dependencies..."
pip install -r requirements.txt

# Install the package in editable mode
echo "Installing the package in editable mode..."
pip install -e .

# Confirm installation success
echo "Installation complete. You can now use the CLI tool by running 'airline_cli'."
