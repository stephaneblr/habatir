DROP DATABASE IF EXISTS webapp;

CREATE DATABASE IF NOT EXISTS webapp;

USE webapp;

CREATE TABLE IF NOT EXISTS contientvariable (
  id_regle int,
  id_variable int
);

LOAD DATA INFILE '/var/lib/mysql-files/contientvariable.csv'
INTO TABLE contientvariable
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id_regle, id_variable);


CREATE TABLE IF NOT EXISTS  lois (
  id_loi int,
  description text,
  lien text
);

LOAD DATA INFILE '/var/lib/mysql-files/lois.csv'
INTO TABLE lois
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id_loi, description, lien);

CREATE TABLE IF NOT EXISTS regle (
  id_regle int,
  txt int,
  zone text,
  entree_graphique text,
  sujet int,
  contrainte int,
  change_def int
);

LOAD DATA INFILE '/var/lib/mysql-files/regle.csv'
INTO TABLE regle
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id_regle, txt, zone, entree_graphique, sujet, contrainte, change_def);

CREATE TABLE IF NOT EXISTS sujet (
  id_sujet int,
  nom text
);

LOAD DATA INFILE '/var/lib/mysql-files/sujet.csv'
INTO TABLE sujet
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id_sujet, nom);

CREATE TABLE IF NOT EXISTS  txt (
  id_txt int,
  txt text,
  loi text
);

LOAD DATA INFILE '/var/lib/mysql-files/txt.csv'
INTO TABLE txt
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id_txt, txt, loi);

CREATE TABLE IF NOT EXISTS variable (
  id_variable int,
  nom text
);

LOAD DATA INFILE '/var/lib/mysql-files/variable.csv'
INTO TABLE variable
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id_variable, nom);
