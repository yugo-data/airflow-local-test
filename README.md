# airflow-local-test
ローカルでテストする用のリポジトリ  

### 実行手順
- イメージ取得  
docker pull apache/airflow:2.10.4-python3.12
- 権限変更  
chmod +x run_airflow.sh
- imageの実行  
./run_airflow.sh

### ユーザ作成
docker exec -it airflow-webserver airflow users create \
  --username admin \
  --password admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com

### コンテナ内で作業
- コンテナに入る  
docker exec -u root -it airflow-webserver bash
- WEBサーバ立ち上げ  
airflow webserver -D

- スケジューラ立ち上げ  
airflow scheduler -D