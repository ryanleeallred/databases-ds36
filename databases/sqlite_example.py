'''module docstring'''
# step 0 - import sqlite
# Also get the database file into the folder where we're working.
import sqlite3
import queries as q
# from queries import select_all, other_query, another_query


def connect_to_db(db_name='rpg_db.sqlite3'):
    '''DB Connect Function'''
    return sqlite3.connect(db_name)


def execute_q(conn, query):
    '''Make a cursor and execute query function'''
    curs = conn.cursor()
    curs.execute(query)
    return curs.fetchall()


# ensure that the queries are only being run when
# the file is executed as a script
# `python sqlite_example.py`
if __name__ == '__main__':
    # print(queries.select_all)
    conn = connect_to_db()
    # results = execute_q(conn, q.select_all)
    results2 = execute_q(conn, q.items_per_character)
    # results3 = execute_q(conn, q.other_query)
    print(results2)
