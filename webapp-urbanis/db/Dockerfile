FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD password

COPY ./init.sh /docker-entrypoint-initdb.d/init.sh
COPY ./db.sql /docker-entrypoint-initdb.d/db.sql
RUN chmod 755 /docker-entrypoint-initdb.d/init.sh
RUN chmod 755 /docker-entrypoint-initdb.d/db.sql

RUN mkdir /var/lib/mysql-files
COPY ./*.csv /var/lib/mysql-files/
COPY ./config/* /etc/mysql/conf.d/