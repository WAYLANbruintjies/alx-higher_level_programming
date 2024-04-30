#!/usr/bin/python3
"""Modules to import to list all states from hbtn_0e_0_usa database"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL server, get login credentials from cmd arguments
    db = MySQL.connect(host='localhost', port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    # SQL query to retrieve all states, where name starts with 'N' and ordered by id
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC")
    rows = cursor.fetchall()

    # Return/print the results of the above query
    for row in rows:
        print(row)

    # Close database connection
    cursor.close()
    db.close()
