#!/usr/bin/python3
"""Modules to import"""
import MySQLdb
import sys


if __name__ == "__main__":

    """MySQL server+db connection/setup instantiated"""
    db = MySQL.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    
    cursor = db.cursor()

    """SQL query execution and print result"""
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
            INNER JOIN states ON states.id=cities.state_id")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
