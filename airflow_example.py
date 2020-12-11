# -*- coding: utf-8 -*-
# Version: 0.1a1

import datetime

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


def task2():
    print('task2')


default_args = {
    'owner': 'Ruslan Korniichuk',
    'start_date': datetime.datetime(2020, 12, 11)
}

with DAG('example',
         default_args=default_args,
         schedule_interval='@daily') as dag:

    task1 = BashOperator(task_id='task1', bash_command='echo task1')
    task2 = PythonOperator(task_id='task2', python_callable=task2)

task1 >> task2
