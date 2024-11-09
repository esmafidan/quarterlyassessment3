import sqlite3

def read_database(db_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Retrieve and print all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    if not tables:
        print("No tables found in the database.")
        return
    
    print("Tables in the database:")
    for table in tables:
        print(f"- {table[0]}")
    
    # Ask user to select a table
    table_name = input("Enter the name of the table you want to query: ")
    
    # Validate table name
    if (table_name,) not in tables:
        print("Invalid table name. Please try again.")
        conn.close()
        return
    
    # Retrieve and print data from the selected table
    cursor.execute(f"SELECT * FROM \"{table_name}\";")
    rows = cursor.fetchall()
    
    if not rows:
        print(f"No data found in the table '{table_name}'.")
    else:
        print(f"Data from table '{table_name}':")
        for row in rows:
            print(row)
    
    # Close the database connection
    conn.close()

# Example usage
read_database('quiz_questions.db')
