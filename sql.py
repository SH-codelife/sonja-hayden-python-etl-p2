insert_movie = ('''
    TODO
''')

create_schema = ('''
    CREATE SCHEMA IF NOT EXISTS petl2;
''')

drop_table = ('''
    DROP TABLE IF EXISTS  petl2.movie_list
''')

create_table = ('''
    CREATE TABLE IF NOT EXISTS  petl2.movie_list (
        title TEXT,
        rated TEXT,
        released DATE,
        runtime INT,
        genre TEXT[],
        director TEXT,
        writer TEXT[],
        actors TEXT[],
        plot TEXT,
        awards TEXT,
        poster TEXT)
''')

insert_data = ('''
    INSERT INTO petl2.movie_list (TITLE, RATED, RELEASED, RUNTIME, GENRE, DIRECTOR, WRITER, ACTORS, PLOT, AWARDS, POSTER) 
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
''')


