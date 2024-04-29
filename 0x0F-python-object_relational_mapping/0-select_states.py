#!/usr/bin/pyhton3
"""Modules to import"""
import MySQLdb
import sys

def list_of_states(username, password, database):
    # MySQL server connection
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Execute a MySQL query to fetch the states
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Get all the rows from the query result
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close database connection
    db.close()

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_of_states(username, password, database)
