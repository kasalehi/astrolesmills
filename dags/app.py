from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# lets define a function that we will use in our PythonOperator
def my_function():
    print("Hello from my_function!")


def your_function():
    print("Hello from your_function!")  

# define the DAG
with DAG(
    dag_id="example_dag",
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    # define the PythonOperator
    my_task = PythonOperator(
        task_id="my_task",
        python_callable=my_function,
    )

    your_task = PythonOperator(
        task_id="your_task",    
    python_callable=your_function,
    )
    # set the task dependencies (if any)
    my_task >> your_task