from airflow.operators.python_operator import PythonOperator
from airflow.operators.python import PythonVirtualenvOperator
from airflow import DAG

from datetime import datetime

def params_step(params):
    print(params)
    print("yay it works!")

default_args = {
    'owner': 'Vivek Bhadane',
    'depends_on_past': False,
    'start_date': datetime(2021, 10, 15)
}

with DAG(
    dag_id='PropertyData_buildingPermit',
    default_args=default_args,
    schedule_interval=None,
    tags=['Property Data']
) as buildingPermit_dag:
    copy_to_redshift = PythonVirtualenvOperator(
        task_id='test_params',
        provide_context=True,
        python_callable=params_step,
        params={'bucket_name':'sthomeowner', 'fileType':'BUILDINGPERMIT_', 'prefix':'attom/permit/building_permits/','stg_table':'homeowner.attom_building_permit_delta'},
        dag=buildingPermit_dag
    )

copy_to_redshift
