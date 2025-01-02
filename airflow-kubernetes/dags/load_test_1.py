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
    max_active_runs=5,  # DAGインスタンスの最大同時実行数
) as dag:

    # 10個のタスクを並列で実行
    tasks = [
        BashOperator(
            task_id=f'task_{i}',
            bash_command='echo "Task $((RANDOM % 10 + 1)) running on $(hostname)" && sleep $((RANDOM % 5 + 1))',
            task_concurrency=2,  # このタスクの最大並列実行数
            executor_config={
                "KubernetesExecutor": {
                    "image": "664418998238.dkr.ecr.ap-northeast-1.amazonaws.com/airflow-local-test:2.10.4-python3.12"
                }
            }
        )
        for i in range(2)  # タスク数を調整可能
    ]
