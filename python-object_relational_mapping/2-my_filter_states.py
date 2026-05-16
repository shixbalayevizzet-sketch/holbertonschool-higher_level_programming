#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
It takes 4 arguments: mysql username, mysql password, database name,
and state name searched.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get database credentials and search term from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_searched = sys.argv[4]

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

    # Create the SQL query using the format method as required
    query = "SELECT * FROM states WHERE name = BINARY '{}' ORDER BY id ASC".format(state_searched)
    cursor.execute(query)

    # Fetch all the rows from the executed query
    query_rows = cursor.fetchall()

    # Format and display results
    for row in query_rows:
        print(row)

    # Clean up and close connections
    cursor.close()
    db.close()
