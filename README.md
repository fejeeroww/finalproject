# finalproject
## Income Spending Survey Tool

## Project Overview
This project is a survey tool designed to collect and analyze participants' income spending data for a new product launch in the healthcare industry. It includes a web application for data collection, a backend for data storage, data processing and visualization components.

## Features
- Web-based survey form using Flask
- Data storage in MongoDB
- Data processing with Python
- Data visualization using Jupyter Notebook
- Deployment instructions for AWS

## Project Component
-flaskapp.py (Flask application)

-flaskapphtml.html (HTML template for the survey form)

-process_data.py (Script to process data and create CSV)

-data_visualization.ipynb (Jupyter notebook for data analysis)

-README.md

## Setup and Installation
1. Download this repository
2. Install required Python packages
3. Ensure MongoDB is installed and running on your local machine or set up a cloud-based MongoDB instance.
4. Update the MongoDB connection string in `flaskapp.py` and `process_data.py` if necessary.

## Running the Application Locally
1. Start the Flask application: flaskapp.py
2. Access the survey form at `http://localhost:5000` in your web browser.
3. To process the collected data and create the CSV file: Access process_data.py
4. Open `data_visualization.ipynb` in Jupyter Notebook to perform data analysis and create visualizations.

## Data Visualization
The Jupyter Notebook `data_visualization.ipynb` includes:
- Analysis of ages with the highest income
- Gender distribution across spending categories
- Exported charts for use in presentations

## Deployment on AWS
1. Set up  EC2 instance on AWS.
2. Install necessary dependencies on the EC2 instance.
3. Transfer your application files to the EC2 instance.
4. Run the application using Gunicorn:

