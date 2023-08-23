import MySQLdb
import sys


def search_states(username, password, database, state_name):
    try:
        # Connect to MySQL server
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Prepare the SQL query with a parameterized query
        query = """SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC;""".format(state_name)

        # Execute the query with the state name as a parameter
        cursor.execute(query)

        # Fetch all the rows returned by the query
        # -------
        # may be diferent in some cases read the instructions
        
        rows = cursor.fetchall()
        

        # Display the results not the same for all change as the task demands 
        
        if rows:
            for row in rows:
                print(row)
        else:
            # print()
            pass
        # -------

        # Close the cursor and connection
        cursor.close()
        conn.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

if __name__ == "__main__":
    # Get the arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the search_states function with the provided arguments
    search_states(username, password, database, state_name)