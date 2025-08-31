#!/bin/bash

echo "Starting Roomsy Application..."
echo "================================"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create sample data (optional)
echo "Creating sample data..."
python sample_data.py

# Start the application
echo "Starting the application..."
echo "Open your browser and go to: http://localhost:5000"
echo "Press Ctrl+C to stop the application"
python run.py
