#!/usr/bin/python3
"""Modules to import"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connection to MySQL database
    db = MySQL.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], name=sys.argv[4])
    cursor = db.cursor()

    # Execute SQL query
    search = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY state.id ASC", (search, ))

    # Return SQL query result and print
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close MySQL server connection
    db.close()
