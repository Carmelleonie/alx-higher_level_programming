#!/usr/bin/python3
"""A script that takes in the name of a state as an argument
    and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':
    user_name = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(user=user_name, passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON cities.id = states.id WHERE states.name = %s ORDER BY cities.id", (state_name, ))
    
    res = cur.fetchall()

    for idx in range(len(res)):
        print(res[idx][0], end=", " if idx + 1 < len(res) else "")
    print("")

