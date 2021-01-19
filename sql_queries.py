# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplays"

user_table_drop = "DROP table IF EXISTS users"

song_table_drop = "DROP table IF EXISTS songs"

artist_table_drop = "DROP table IF EXISTS artists"

time_table_drop = "DROP table IF EXISTS time"


# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
     songplay_id serial primary key, 
     start_time timestamp without time zone,
     user_id int NOT NULL, 
     level Varchar, 
     song_id Varchar,                                                           
     artist_id Varchar, 
     session_id int, 
     location Varchar, 
     user_agent Varchar);
""")


user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
    user_id int primary key, 
    first_name Varchar,
    last_name Varchar, 
    gender Varchar, 
    level Varchar);
""")
                                                            

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
    song_id Varchar primary key, 
    title Varchar,
    artist_id Varchar NOT NULL, 
    year int, 
    duration numeric);
""")


artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
    artist_id Varchar primary key, 
    name Varchar,
    location Varchar, 
    latitude real, 
    longitude real);
""")


time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
    start_time timestamp without time zone primary key, 
    hour int, 
    day int, 
    week int, 
    month Varchar, 
    year int, 
    weekday Varchar);
""")


# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays(
    start_time, 
    user_id, 
    level, 
    song_id, 
    artist_id, 
    session_id, 
    location, 
    user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
    INSERT INTO users( 
    user_id, 
    first_name, 
    last_name, 
    gender, 
    level)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level || ';' || users.level
""")

song_table_insert = ("""
    INSERT INTO songs( 
    song_id, 
    title, 
    artist_id, 
    year, 
    duration)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = ("""
    INSERT INTO artists( 
    artist_id, 
    name, 
    location, 
    latitude, 
    longitude)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO NOTHING
""")


time_table_insert = ("""
    INSERT INTO time(
    start_time, 
    hour, 
    day, 
    week,
    month, 
    year, 
    weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) DO NOTHING
""")


# FIND SONGS

song_select = ("""
    SELECT songs.song_id, songs.artist_id 
    from songs INNER JOIN artists 
    ON songs.artist_id=artists.artist_id 
    WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]