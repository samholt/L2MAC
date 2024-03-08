import sqlite3
import time

# Function to add version
def add_version(file_id, version_number):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Get current timestamp
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    # Add version to versions table
    cursor.execute("""INSERT INTO versions (file_id, version_number, timestamp) VALUES (?, ?, ?)""", (file_id, version_number, timestamp))

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Return success message
    return 'Version added successfully'

# Test function with dummy file ID and version number
print(add_version(1, 1))