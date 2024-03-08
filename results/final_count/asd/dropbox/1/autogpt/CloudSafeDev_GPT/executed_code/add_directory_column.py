import sqlite3

# Function to add directory column to files table
def add_directory_column():
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Add directory column to files table
    cursor.execute("""ALTER TABLE files ADD COLUMN directory TEXT""")

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Return success message
    return 'Directory column added successfully'

# Test function
print(add_directory_column())