Census Data Analysis

This repository contains a Python application built with Streamlit for analyzing census data. It fetches Census data, performs data standardization, loads data into MongoDB and Oracle DB, and provides various analyses based on user-selected questions.

Features:
Fetch Census Data: Fetches census data from a source.
Data Standardization: Standardizes data by renaming columns, formatting the state names, and filling null values.
Load Data to MongoDB: Loads standardized data into MongoDB.
Load Data to Oracle DB: Creates tables such as Districts, Demographics, Household on Oracle DB and loads data into it. Further it displays district-wise, demographics-wise, and household-wise data using Streamlit.
SQL Analysis: Executes SQL queries to answer predefined analysis questions about population, literacy, workers, household amenities, religious composition, education levels, transportation access, housing conditions, household size, and more.
Interactive GUI: Sidebar for actions and selection of analysis questions with an analyze button for results.

Installation

Clone the repository:

git clone (https://github.com/MalathiDurai/Capstone_Census_Data.git)
cd <cloning_repository-directory>

Install dependencies:

pip install pandas
pip install pymongo
pip install streamlit
pip install cx_Oracle

To run the application:

streamlit run Census_2011.py

Usage:

Use the sidebar to perform actions like fetching data, standardizing data, loading data into databases, and selecting analysis questions.
Click on "Analyze" to view analysis results based on the selected question.
Dataframes and results are displayed using Streamlit components directly in the web interface.
