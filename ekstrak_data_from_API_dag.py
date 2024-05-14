import pandas as pd
import requests
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from airflow.utils.dates import days_ago

# Define function to extract data from API
def extract_population_data():
    # API endpoint
    url = "https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json&per_page=30000"

    # Send GET request
    response = requests.get(url)

    # Check if request was successful (status code 200)
    if response.status_code == 200:
        # Extract relevant data from JSON response
        data = response.json()[1]  # Data starts from index 1

        # Create a list of dictionaries containing relevant data
        records = []
        for entry in data:
            record = {
                "Country Name": entry["country"]["value"],
                "Country Code": entry["countryiso3code"],
                "Year": entry["date"],
                "Population": entry["value"]
            }
            records.append(record)

        # Convert list of dictionaries into DataFrame
        population5_API_df = pd.DataFrame(records)

        # Print the number of records extracted
        print("Number of records extracted:", len(population5_API_df))
    else:
        print("Error:", response.status_code)

# Define default arguments for the DAG
default_args = {
    'owner': 'rayhan',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

# Define DAG parameters
dag = DAG(
    'population_extraction_API_dag',
    default_args=default_args,
    description='A DAG to extract population data from API',
    schedule_interval='@daily',
)

# Define task to extract data from API
extract_data_task = PythonOperator(
    task_id='extract_population_data',
    python_callable=extract_population_data,
    dag=dag,
)

# Set task dependencies
extract_data_task