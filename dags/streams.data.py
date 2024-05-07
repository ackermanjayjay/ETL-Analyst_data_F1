from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from airflow import DAG
import logging
from read_data import read_data
from transformation_data import transformation_columns

default_args = {"owner": "mad", "retry": 5, "retry_delay": timedelta(minutes=5)}


def get_data():
    data = read_data()
    return data.to_json()


def transformation():
    try:
        data = transformation_columns()
        return data.to_json(indent=4, orient="records")
    except Exception as e:
        logging.error(f"Error data in transformation : {e}")


def insert_data():
    import psycopg2
    import time
    from sqlalchemy import create_engine

    res = transformation_columns()
    # # Example: 'postgresql://username:password@localhost:5432/your_database'
    # code from https://medium.com/@askintamanli/fastest-methods-to-bulk-insert-a-pandas-dataframe-into-postgresql-2aa2ab6d2b24
    engine = create_engine("postgresql://airflow:airflow@host.docker.internal/data-f1")

    start_time = time.time()  # get start time before insert
    # Create a connection to your PostgreSQL database
    conn = psycopg2.connect(
        database="data-f1",
        user="airflow",
        password="airflow",
        host="host.docker.internal",
        port="5432",
    )
    cur = conn.cursor()
    try:
        res.to_sql(name="f1_drivers", con=engine, if_exists="replace")
        conn.commit()
        end_time = time.time()  # get end time after insert
        total_time = end_time - start_time  # calculate the time
        logging.info(
            f"Insert affected : {cur.rowcount} and Insert time: {total_time} seconds"
        )

    except Exception as e:
        logging.error(f"could not insert data due to {e}")


with DAG(
    default_args=default_args,
    dag_id="ETL-analyst-data-F1-to_table_v02",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@once",
) as dag:
    task1 = PythonOperator(task_id="read_data", python_callable=get_data)
    task2 = PythonOperator(
        task_id="transformation_data", python_callable=transformation
    )
    task3 = PythonOperator(task_id="insert_data_to_table", python_callable=insert_data)

    task1 >> task2 >> task3
