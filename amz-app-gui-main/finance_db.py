import mysql.connector

def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="@Kelompok7",
        database="finance_app"
    )
    return conn

def create_record(conn, sql, data):
    cursor = conn.cursor()
    cursor.execute(sql, data)
    conn.commit()
    
def read_record(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def check_value_exists(column_value):    
    
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="@Kelompok7",
        database="finance_app"
    )
    
    # Create a cursor object
    cursor = conn.cursor()

    # SQL query to check if the column value exists in any row of the table
    sql = "SELECT COUNT(*) FROM users WHERE username = %s"
    cursor.execute(sql, (column_value,))

    # Fetch the result
    result = cursor.fetchone()[0]

    # Close the cursor and database connection
    cursor.close()
    conn.close()

    # Return True if the column value exists, False otherwise
    return result > 0