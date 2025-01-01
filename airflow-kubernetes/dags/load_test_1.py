from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# DAGの定義
with DAG(
    dag_id='load_test',
    default_args={'retries': 1},
    schedule_interval=None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
) as dag:

    # 10個のタスクを並列で実行
    tasks = [
        BashOperator(
            task_id=f'task_{i}',
            bash_command='echo "Task $((RANDOM % 10 + 1)) running on $(hostname)" && sleep $((RANDOM % 5 + 1))',
        )
        for i in range(10)  # タスク数を調整可能
    ]
