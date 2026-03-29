from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def run_pipeline():
    # Executa seu script Python existente
    subprocess.run(["python3", "/home/brunoserver/projetos/data-engineering-lab/scripts/pipeline.py"], check=True)

dag = DAG('data_pipeline', start_date=datetime(2026, 3, 7), schedule=None)

task = PythonOperator(
    task_id='run_pipeline',
    python_callable=run_pipeline,
    dag=dag
)