import MySQLdb
import sys


def states(username, password, database):
    try:
        conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=username,
                passwd=password,
                db=database
            )
        cursor = conn.cursor()
        query ="""SELECT * FROM states"""
        cursor.execute(query)
        rows = cursor.fetchall()

        if rows:
            for row in rows:
             print(row)
        else:
            # print()
            pass
        cursor.close()
        conn.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)
if __name__ == "__main__":
   
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
   
    states(username, password, database)
    



