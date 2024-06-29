#!/usr/bin/python3
"""A script that takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb
if __name__ == '__main__':
    user_name = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    
    db = MySQLdb.connect(user=user_name, passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name = %s ORDER BY states.id".format(state_name))
    res = cur.fetchall()

    for row in res:
        print(row)

