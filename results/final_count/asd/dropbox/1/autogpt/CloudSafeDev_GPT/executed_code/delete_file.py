import sqlite3

# Function to delete file
def delete_file(file_id):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Delete file from database
    cursor.execute("""DELETE FROM files WHERE id = ?""", (file_id,))

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Return success message
    return 'File deleted successfully'

# Test function with dummy file ID
print(delete_file(1))