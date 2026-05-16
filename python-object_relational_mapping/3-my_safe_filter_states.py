#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument safely.
This script is secure against MySQL injections.
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

    # Execute query using a placeholder (%s) to prevent SQL Injection.
    # Note: Binary comparison is applied dynamically if needed,
    # or via safe parameter substitution.
    query = "SELECT * FROM states WHERE name = BINARY %s ORDER BY id ASC"
    cursor.execute(query, (state_searched,))

    # Fetch all the rows from the executed query
    query_rows = cursor.fetchall()

    # Format and display results
    for row in query_rows:
        print(row)

    # Clean up and close connections
    cursor.close()
    db.close()
