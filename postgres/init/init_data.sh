#!/bin/bash
psql postgres postgres << "EOSQL"
create table meibo (id serial, name text);
insert into meibo (id, name) values (1, 'hoge');
EOSQL
