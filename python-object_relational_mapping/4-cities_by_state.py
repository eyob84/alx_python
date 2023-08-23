import MySQLdb
import sys


def search_states(username, password, database):
    try:
        # Connect to MySQL server
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        
        cursor = conn.cursor()

        # Prepare the SQL query with a parameterized query
        query = """ SELECT cities.id, cities.name, states.name FROM cities
        JOIN states ON  cities.state_id = states.id ORDER BY cities.id ASC; """
        cursor.execute(query)
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            pass

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


    # Call the search_states function with the provided arguments
    search_states(username, password, database)
