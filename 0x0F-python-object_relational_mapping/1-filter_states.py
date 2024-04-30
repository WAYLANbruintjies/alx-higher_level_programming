#!/usr/bin/python3
"""
Modules to import to list all states from hbtn_0e_0_usa database
starting with N (upper N) sorted in ascending order by states.id
"""

import MySQLdb
import sys


if __name__ == "__main__":
    try:
        # Connect to MySQL server, get login credentials from cmd arguments
        db = MySQL.connect(
                host='localhost',
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3],
                charset='utf8'
            )
    except MySQLdb.Error as e:
        print("Error connecting to database: {}".format(e))
        sys.exit(1)

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
