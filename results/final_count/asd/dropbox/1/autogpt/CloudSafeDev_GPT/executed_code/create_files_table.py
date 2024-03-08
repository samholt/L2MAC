import sqlite3

# Function to create files table
def create_files_table():
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Create files table
    cursor.execute("""CREATE TABLE files (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        filename TEXT,
        size INTEGER
    )""")

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Return success message
    return 'Files table created successfully'

# Test function
print(create_files_table())