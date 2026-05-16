#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
It uses only one execute() call.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get database credentials from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute a single SQL query using JOIN to get cities and their states
    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )

    # Fetch all the rows from the executed query
    query_rows = cursor.fetchall()

    # Format and display results
    for row in query_rows:
        print(row)

    # Clean up and close connections
    cursor.close()
    db.close()
