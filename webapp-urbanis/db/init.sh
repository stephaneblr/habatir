#!/usr/bin/env bash

mysql -uroot -ppassword < /docker-entrypoint-initdb.d/db.sql