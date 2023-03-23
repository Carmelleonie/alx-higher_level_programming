#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa: """
from sys import argv
import MySQLdb

if __name__ == "__main__":
    sql_user = argv[1]
    sql_passwd = argv[2]
    sql_db = argv[3]

    db= MySQLdb.connect(user=sql_user, passwd=sql_passwd, db=sql_db)
    cur= db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
