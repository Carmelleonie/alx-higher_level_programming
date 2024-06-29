#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa: """
import sys
import MySQLdb
if __name__ == '__main__':
    user_name = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    db = MySQLdb.connect(user=user_name, passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name LIKE('N%') ORDER BY states.id ")
    
    res = cur.fetchall()
    for row in res:
        print(row)

