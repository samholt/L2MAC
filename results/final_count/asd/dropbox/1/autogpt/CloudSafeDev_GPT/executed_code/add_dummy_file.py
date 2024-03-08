import sqlite3

# Function to add dummy file to files table
def add_dummy_file():
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Add dummy file to files table
    cursor.execute("""INSERT INTO files (id, user_id, filename, size) VALUES (?, ?, ?, ?)""", (1, 1, 'oldfile', 1000))

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Return success message
    return 'Dummy file added successfully'

# Test function
print(add_dummy_file())