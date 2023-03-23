#!/usr/bin/python3

"""A script that lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(user="{}", passwd="{}", db="{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name
        FROM cities, states
        
        WHEREcities.state_id = states.id
        
        ORDER BY cities.id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)
