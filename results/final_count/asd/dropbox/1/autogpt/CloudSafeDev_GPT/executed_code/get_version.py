import sqlite3

# Function to get version
def get_version(file_id, version_number):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Get version from versions table
    cursor.execute("""SELECT * FROM versions WHERE file_id = ? AND version_number = ?""", (file_id, version_number))
    version = cursor.fetchone()

    # Close connection
    conn.close()

    # Return version
    return version

# Test function with dummy file ID and version number
print(get_version(1, 1))