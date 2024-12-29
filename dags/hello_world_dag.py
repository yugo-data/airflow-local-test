from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

# デフォルト引数の定義
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

# DAG の定義
with DAG(
    'hello_world_dag',           # DAG の ID（ユニークな名前）
    default_args=default_args,   # デフォルト引数
    description='A simple hello world DAG',
    schedule_interval=None,      # スケジュール（None は手動実行）
    start_date=days_ago(1),      # 開始日（過去の日付に設定）
    catchup=False,               # 過去のスケジュール分を実行しない
) as dag:
    # タスクの定義
    start = DummyOperator(
        task_id='start_task'
    )

    end = DummyOperator(
        task_id='end_task'
    )

    # タスクの依存関係
    start >> end

