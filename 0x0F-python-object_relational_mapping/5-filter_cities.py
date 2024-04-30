#!/usr/bin/python3
"""Modules to import"""
import MySQLdb
import sys


if __name__ == "__main__":
    
    """MySQL server + db connection setup initialization"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    """Execute MySQL queries and display results"""
    cursor.execute("SELECT cities.name FROM cities INNER JOIN states ON states.id=cities.state_id \
            WHERE states.name=%s", (sys.argv[4]))

    rows = cursor.fetchall()
    temp = list(row[0] for row in rows)
        print(*temp, sep=", ")

    """Close off all connection"""
    cursor.close()
    db.close()
