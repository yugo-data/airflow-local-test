#!/bin/bash

# 環境変数の設定
EXECUTOR="SequentialExecutor"
DAGS_FOLDER="/opt/airflow/dags"
SQL_ALCHEMY_CONN="sqlite:////opt/airflow/airflow.db"
CONSTRAINTS_URL="https://raw.githubusercontent.com/apache/airflow/constraints-2.10.4/constraints-3.12.txt"

# Docker Run コマンド
docker run -d --name airflow-webserver \
  -p 8080:8080 \
  -e AIRFLOW__CORE__EXECUTOR=$EXECUTOR \
  -e AIRFLOW__CORE__DAGS_FOLDER=$DAGS_FOLDER \
  -e AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=$SQL_ALCHEMY_CONN \
  -e AIRFLOW_CONSTRAINTS=$CONSTRAINTS_URL \
  -v $(pwd)/dags:/opt/airflow/dags \
  apache/airflow:2.10.4-python3.12 bash -c "airflow db init && airflow webserver"
