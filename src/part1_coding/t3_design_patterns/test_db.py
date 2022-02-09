import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        conn.execute('CREATE TABLE contacts (name TEXT, phone INTEGER, email TEXT)')
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(
        r"/Users/paulb/Documents/GitHub/py-test-automation-course/src/part1_coding/t3_design_patterns/pythonsqlite.db")
