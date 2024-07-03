from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os

# Chemin vers le script Python
script_path = '/Users/sami.hella/airflow/process_housing_data.py'

# Définir les arguments par défaut du DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Définir le DAG
dag = DAG(
    'housing_data_dag',
    default_args=default_args,
    description='Pipeline de traitement de données immobilières',
    schedule_interval=timedelta(minutes=1),
)

# Définir la tâche
def run_script():
    os.system(f'python {script_path}')

run_script_task = PythonOperator(
    task_id='run_process_housing_data_script',
    python_callable=run_script,
    dag=dag,
)

# Spécifier la séquence des tâches
run_script_task
