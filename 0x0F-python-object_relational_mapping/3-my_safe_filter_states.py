#!/usr/bin/python3
"""Modules to import"""
import MySQLdb
import sys

if __name__ == "__main__":

    """Connection setup to MySQL database"""
    db = MySQLdb.connect(host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset='utf8'
        )

    cursor = db.cursor()

    """Execute SQL query and print reslut"""
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY \
            %(name)s ORDER BY state.id ASC", ('name': sys.argv[4]))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    """Close MySQL server db connections"""
    cursor.close()
    db.close()
