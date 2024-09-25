from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['JimmyUnelus@gmail.com'],
    'email_on_failure': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def run_dbt():
    subprocess.run(['dbt', 'run'], check=True)

with DAG(
    'etl_pipeline',
    default_args=default_args,
    description='A simple ETL pipeline',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    ingest = BashOperator(
        task_id='ingest_data',
        bash_command='python3 data_ingestion/kafka_consumer.py',
    )

    transform = PythonOperator(
        task_id='transform_data',
        python_callable=run_dbt,
    )

    ingest >> transform
