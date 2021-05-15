from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.utils import timezone


def _create_homepage():
    with open("html/index.html", "w") as f:
        f.writelines("<h1>Welcome to My Course</h1>\n")
        f.writelines("<p>It's raining day.. :'(</p>\n")
        f.writelines("<p>I'm enjoying Airflow</p>")


default_args = {
    "owner": "zkan",
    "start_date": timezone.datetime(2021, 5, 15),
}
with DAG("my_dag", 
         schedule_interval="*/5 * * * *",
         default_args=default_args,
         catchup=False) as dag:

    start = DummyOperator(task_id="start")

    create_homepage = PythonOperator(
        task_id="create_homepage",
        python_callable=_create_homepage,
    )

    end = DummyOperator(task_id="end")

    start >> create_homepage >> end