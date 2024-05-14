import os
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from google.cloud import storage
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define local CSV file paths
local_csv_path_world_bank = '/home/sapphire/data/final_dataset.csv'
local_csv_path_world_bank_scaled = '/home/sapphire/data/final_scaled_dataset.csv'

# Function to upload CSV files to Google Cloud Storage
def upload_to_gcs():
    service_account_path = os.getenv('SERVICE_ACCOUNT_PATH')
    client = storage.Client.from_service_account_json(service_account_path)
    bucket_name = os.getenv('BUCKET_NAME')

    file_paths = [
        (local_csv_path_world_bank, "merged_final_df.csv"),
        (local_csv_path_world_bank_scaled, "merged_final_scaled_df.csv")
    ]

    for file_path, file_name in file_paths:
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(file_name)
        blob.upload_from_filename(file_path)

        print(f"File {file_name} successfully uploaded to GCS bucket {bucket_name}.")

# Define default arguments
default_args = {
    "owner": "rayhan",
    "retries": 2,
    "retry_delay": timedelta(minutes=1),
}

# Define DAG
dag = DAG(
    'mini_project_load_to_gcs_dag',
    default_args=default_args,
    description='Mini Project DAG for loading to warehouse GCS',
    start_date=datetime(2024, 5, 13),
    schedule_interval='@daily'
)

# Define tasks
task_upload_to_gcs = PythonOperator(
    task_id='upload_to_gcs',
    python_callable=upload_to_gcs,
    dag=dag,
)

# Define task dependencies
task_upload_to_gcs
