DROP DATABASE  IF EXISTS signals_db;
CREATE DATABASE IF NOT EXISTS signals_db;
USE signals_db;
DROP TABLE  IF EXISTS signals;
DROP TABLE  IF EXISTS keyWords;
CREATE TABLE  IF NOT EXISTS signals(
node_id VARCHAR(250) NOT NULL,
sampling_interval_ms INT NULL,
deadband_value INT NULL,
deadband_type VARCHAR(25) NULL,
active BOOL NULL ,
keywords VARCHAR(25),
PRIMARY KEY (node_id)
);

CREATE TABLE  IF NOT EXISTS keyWords(
id TINYINT NOT NULL,
name VARCHAR(10),
description VARCHAR(25),
PRIMARY KEY (id)
)
