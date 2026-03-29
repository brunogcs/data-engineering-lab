from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def run_pipeline():
    # Executa o script pipeline.py que está dentro do container, na pasta dags
    subprocess.run(["python3", "/opt/airflow/dags/scripts/pipeline.py"], check=True)

dag = DAG(
    'data_pipeline',
    start_date=datetime(2026, 3, 7),
    schedule=None,  # manual
    catchup=False
)

task = PythonOperator(
    task_id='run_pipeline',
    python_callable=run_pipeline,
    dag=dag
)