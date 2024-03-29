from airflow.operators.python import PythonVirtualenvOperator, PythonOperator
from airflow import DAG

from datetime import datetime

def params_step(params):
    print(params)
    print("yay it works!")
    print("and maybe nyet")
    print("and maybe nyet123")

def params_kwargs_step(params, **kwargs):
    print(params)
    print(kwargs)
    print("this works too")

default_args = {
    'owner': 'Vivek Bhadane',
    'depends_on_past': False,
    'start_date': datetime(2021, 1, 1)
}

with DAG(
    dag_id='dag-id-from-test',
    default_args=default_args,
    schedule=None,
    tags=['Property Data']
) as buildingPermit_dag:
    params = PythonVirtualenvOperator(
        task_id='test_params2',
        provide_context=True,
        python_callable=params_step,
        params={'bucket_name':'sthomeowner', 'fileType':'BUILDINGPERMIT_', 'prefix':'attom/permit/building_permits/','stg_table':'homeowner.attom_building_permit_delta'},
        dag=buildingPermit_dag
    )
    params_kwargs = PythonVirtualenvOperator(
        task_id='test_params',
        provide_context=True,
        python_callable=params_kwargs_step,
        params={'bucket_name':'sthomeowner', 'fileType':'BUILDINGPERMIT_', 'prefix':'attom/permit/building_permits/','stg_table':'homeowner.attom_building_permit_delta'},
        dag=buildingPermit_dag
    )

params >> params_kwargs
