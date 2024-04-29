#!/usr/bin/python3
"""Modules to import"""
import MySQLdb
import sys

if __name__ == "__main__":
    # MySQL server connection instantiated
    db = MySQL.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    # Execute SQL query
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities
            INNER JOIN states ON states.id=cities.state_id")

    # Print result from query
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close MySQL server connection
    db.close()
