
# Introduction

Sparkify, a startup company, needs to analyze the data they collected on songs and user activity on the new music streaming app. The data resides in a directory of JSON logs. Sparkify's analytics team wants to know what songs users are listening to on the app, so they want to query their data easily, quering from Postgres database.

A star database schema in the Postgres database and ETL pipeline need to be created to load data from JSON logs to Sparkify database schema, and optimized queries on song play analysis. There are five files created for this project, sql_queries.py, create_tables.py, test.ipynb, etl.ipynb and etl.py.

# Summary of Project

### Schema for Song Play Analysis

#### Fact Table
Songplays Table

Attributes | Datatype 
------ | ------ 
songplay_id | int 
start_time | timestamp
user_id | int 
level | Varchar
artist_id | Varchar
session_id | int
location | Varchar
user_agent | Varchar

#### Dimension Tables

Users Table

Attributes | Datatype 
------ | ------ 
user_id | int 
first_name | Varchar
last_name | Varchar
gender | Varchar
level | Varchar


Songs Table

Attributes | Datatype 
------ | ------ 
song_id | Varchar 
title | Varchar
artist_id | Varchar
year | int
duration | numeric

Artists Table

Attributes | Datatype 
------ | ------ 
artist_id | Varchar 
name | Varchar
location | Varchar
latitude | real
longitude | real

Time Table

Attributes | Datatype 
------ | ------ 
start_time | timestamp 
hour | int
day | int
week | int
month | Varchar
year | int
weekday | Varchar

### Files

* test.ipynb: this notebook file displays the first five rows of each table for checking each table

* sql_queries.py: this python file contains sql queries to create tables and insert data into tables. It is imported to create_tables.py, etl.pyynb, and etl.py files.

* create_tables.py: this python file creates database sparkifydb if it does not exist, connects to the Sparkifydb database, drops any tables if they exist, and creates the five tables. This file needs to be run to reset tables before running the etl.py file.

* etl.ipynb: this notebook file reads and processes a single file from song_data and log_data and loads the data into the five tables.

* etl.py: this python file built ETL to reads and process files from song_data and log_Data and loads them into the five tables created in Sparkify database schema.

# User Guide

1. run create_tables.py to connect and build tables at Sparkify database

2. run etl.py to build ETL to load data into Sparkify database

# Example of Query

#### Count the gender of users
SELECT gender, COUNT(user_id) FROM users GROUP BY users.gender;





gender | count
:------: | :------:
M | 14
F | 8


