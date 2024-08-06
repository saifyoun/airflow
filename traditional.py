from airflow import DAG
from datetime import datetime
from airflow.decorators import task, dag
from airflow.operators.python import PythonOperator

with DAG('mydag', start_date=datetime(2020,1,1), schedule_interval="@daily") as dag:

    myfirsttask = PythonOperator(task_id="myfirsttask", python_callable=lambda : print("hello"))

    myfirsttask2 = PythonOperator(task_id="myfirsttask2", python_callable=lambda : print("hello2"))

    myfirsttask >> myfirsttask2