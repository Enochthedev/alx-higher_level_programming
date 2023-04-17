#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create cursor
    cursor = db.cursor()

    # Execute SQL query to select all states
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch all rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
