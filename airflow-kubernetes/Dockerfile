# ベースイメージとして公式の Airflow イメージを使用
FROM apache/airflow:2.10.4-python3.12

# パッケージリストを更新し、vim をインストール
USER root
RUN apt-get update && apt-get install -y vim

# デフォルトではWebサーバーが起動される
CMD ["webserver"]