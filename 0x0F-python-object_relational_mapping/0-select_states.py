#!/usr/bin/pyhton3
"""
Modules to import in order to list all states from the database hbtn_0e_0_usa
sorted by state.id in ascending order
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # MySQL server connection
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database
                charset="utf8")

    except MySQLdb.Error as e:
        print("Error connecting to database: {}".format(e))
        sys.exit(1)

        # Cursor instantiation
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
