from airflow import DAG
from datetime import datetime
from airflow.decorators import task, dag

@dag('mydag', start_date=datetime(2020,1,1), schedule_interval="@daily")
def mydag():

    @task
    def mytask():
        return "hello"
    
    @task
    def mytask2():
        return "hello2"
    
    mytask() >> mytask2()

mydag()