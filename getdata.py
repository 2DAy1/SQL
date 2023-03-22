import psycopg2

def check_data_added():
    # Connect to the database
    conn = psycopg2.connect(
        host="localhost",
        database="db_st",
        user="postgres",
        password="davdad2002"
    )

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query to retrieve table names
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")

    # Fetch all the table names
    table_names = cur.fetchall()

    # Loop through the table names and check if each table has data
    for table_name in table_names:
        cur.execute("SELECT COUNT(*) FROM {}".format(table_name[0]))
        count = cur.fetchone()[0]
        if count == 0:
            print("No data found in table {}".format(table_name[0]))
        else:
            print("Data found in table {}".format(table_name[0]))

    # Close the cursor and connection
    cur.close()
    conn.close()

def get_data():
    # Connect to the database
    conn = psycopg2.connect(
        host="localhost",
        database="db_st",
        user="postgres",
        password="davdad2002"
    )

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query to retrieve table names
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")

    # Fetch all the table names
    table_names = cur.fetchall()

    # Loop through the table names and retrieve all data from each table
    for table_name in table_names:
        cur.execute("SELECT * FROM {}".format(table_name[0]))
        rows = cur.fetchall()
        print("Data from table {}: ".format(table_name[0]))
        for row in rows:
            print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()


if __name__ == '__main__':
    # check_data_added()
    get_data()
    print('finish')