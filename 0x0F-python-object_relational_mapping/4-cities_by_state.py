#!/usr/bin/python3

"""A script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':
    user_name = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
   
    db = MySQLdb.connect(user=user_name, passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.id = states.id ORDER BY cities.id")
    res = cur.fetchall()

    for row in res:
        print(row)

    cursor.close()
    db.close()
