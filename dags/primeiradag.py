from time import sleep

from airflow.decorators import dag, task
from datetime import datetime

@dag(
        dag_id='primeiradag',
        description='ETl do pai',
        schedule="* * * * *",
        start_date= datetime(2025,1,27),
        catchup=False # backfill
)

def pipeline(): 
    @task
    def primeira_atividade():
        print("Atividade 1")
        sleep(2)
    @task
    def segunda_atividade():
        print("Atividade 2")
        sleep(2)
    @task
    def terceira_atividade():
        print("Atividade 3")
        sleep(2)    
    
    t1 = primeira_atividade()
    t2 = segunda_atividade()
    t3 = terceira_atividade()

    t1 >> t2 >> t3

pipeline()
    
