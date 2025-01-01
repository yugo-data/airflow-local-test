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

### kindテスト
```
# kindをインストール
brew install kind

# クラスター作成
kind create cluster

# 作成されたクラスターを確認
kubectl get nodes
```

### ECRにpush
- リポジトリ作成  
```
aws ecr create-repository --repository-name airflow-local-test
```
- ログイン  
```
aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin 664418998238.dkr.ecr.ap-northeast-1.amazonaws.com
```
- カスタムイメージをビルド  
```
docker build -t airflow-local-test:2.10.4-python3.12 .
```
- ビルドしたイメージにtagを付ける  
```
docker tag airflow-local-test:2.10.4-python3.12 664418998238.dkr.ecr.ap-northeast-1.amazonaws.com/airflow-local-test:2.10.4-python3.12
```
- ECRにイメージをPUSH  
```
docker push 664418998238.dkr.ecr.ap-northeast-1.amazonaws.com/airflow-local-test:2.10.4-python3.12
```
