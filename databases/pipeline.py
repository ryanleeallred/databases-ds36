import psycopg2
import sqlite3
import queries as q

# PostgreSQL Connection Credentials
DBNAME = 'pzulbxyo'
USER = 'pzulbxyo'
PASSWORD = '9GvtSD87TCn21DMW25jUbtnkIdQxFT7Y'
HOST = 'raja.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=DBNAME,
                           user=USER,
                           password=PASSWORD,
                           host=HOST)

pg_curs = pg_conn.cursor()

# SQLite Connection
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()


def modify_table(curs, conn, query):
    curs.execute(query)
    conn.commit()


def query_table(curs, query):
    curs.execute(query)
    return curs.fetchall()


if __name__ == '__main__':
    # Test query_table function
    # print(query_table(pg_curs, q.GET_TEST_TABLE))
    # print(query_table(sl_curs, q.GET_CHARACTERS))

    # Query charactercreator_character from SL and insert into PG
    modify_table(pg_curs, pg_conn, q.DROP_CHARACTER_TABLE)
    sl_characters = query_table(sl_curs, q.GET_CHARACTERS)
    modify_table(pg_curs, pg_conn, q.CREATE_CHARACTER_TABLE)
    for character in sl_characters:
        modify_table(pg_curs,
                     pg_conn,
                     f'''INSERT INTO characters ("name", "level", "exp", "hp", "strength", "intelligence", "dexterity", "wisdom")
                 VALUES ('{character[1]}', {character[2]}, {character[3]}, {character[4]}, {character[5]}, {character[6]}, {character[7]}, {character[8]});''')

    # modify_table(pg_curs, pg_conn, q.INSERT_RYAN)
