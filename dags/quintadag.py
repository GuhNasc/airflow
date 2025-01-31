from time import sleep

from airflow.decorators import dag, task
from datetime import datetime
from airflow.models.baseoperator import chain

@dag(
        dag_id='quintadag',
        description='ETl do pai',
        schedule="* * * * *",
        start_date= datetime(2025,1,27),
        catchup=False # backfill
)

def pipeline(): 
    @task
    def primeira_atividade():
        return "Minha quinta dag executando"

    @task
    def segunda_atividade(response):
        print("Atividade 2")
        sleep(2)
        
    @task
    def terceira_atividade():
        print("Atividade 3")
        sleep(2)

    @task
    def quarta_atividade():
        print("Atividade 4")
        sleep(2)    
    
    t1 = primeira_atividade()
    t2 = segunda_atividade(t1)
    t3 = terceira_atividade()
    t4 = quarta_atividade()

    chain(t1,t2,t3,t4)
 
pipeline()
    
