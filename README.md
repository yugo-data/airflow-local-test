# airflow-local-test
ローカルでテストする用のリポジトリ  

### 実行手順

- イメージ取得  
docker pull apache/airflow:2.10.4-python3.12
- 権限変更  
chmod +x run_airflow.sh
- imageの実行  
./run_airflow.sh