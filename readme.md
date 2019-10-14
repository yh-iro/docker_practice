build flask container and postgresql container using docker-compose. then checked if flask container search the postresql and return the results to host PC.

docker-composeでflaskコンテナとpostgresコンテナを起動してhostから5000番でflaskコンテナを叩き、postgresのSQL結果を表示できることを確認した練習コード。
dockerを初めて使う練習のため、設定ファイルの一つ一つの内容はそこまで熟慮されていない。

Usage: 
`
cd docker-practice
docker-compose up -d

docker-compose exec postgres psql postgres postgres

postgres=# create table meibo (id serial, name text);
postgres=# insert into meibo (id, name) values (1, 'hoge');
`

then access localhost:5000 with host browser and check if the result of sql is shown.
