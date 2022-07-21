import sqlite3
from sqlite3 import Error


def sql_connection():
    """Tries to make a database"""

    con = None
    try:
        con = sqlite3.connect('ironcrow.db')
        print("Connection successful")
        cur = con.cursor()
        cur.execute("")
    except Error:
        print(Error)
    finally:
        con.close()


sql_connection()
