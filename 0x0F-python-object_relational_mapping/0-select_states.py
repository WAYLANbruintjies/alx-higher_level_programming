#!/usr/bin/pyhton3
"""Modules to import"""
import MySQLdb
import sys


if __name__ == "__main__":
    # MySQL server connection
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    # Execute a MySQL query to fetch all states
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Get all the rows from the query result
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close all onnections
    cursor.close()
    db.close()
