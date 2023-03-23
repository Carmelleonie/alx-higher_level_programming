#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa: """
import sys
import MySQLdb

if __name__ == "__main__":
    usr = sys.argv[1]
    psw = sys.argv[2]
    nme = sys.argv[3]


    db= MySQLdb.connect(user="usr", password="psw", database="nme")
    c= db.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)
