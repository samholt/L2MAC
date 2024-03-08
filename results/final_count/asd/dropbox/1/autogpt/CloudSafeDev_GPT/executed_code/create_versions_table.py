import sqlite3

# Function to create versions table
def create_versions_table():
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Create versions table
    cursor.execute("""CREATE TABLE versions (
        id INTEGER PRIMARY KEY,
        file_id INTEGER,
        version_number INTEGER,
        timestamp TEXT
    )""")

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Return success message
    return 'Versions table created successfully'

# Test function
print(create_versions_table())