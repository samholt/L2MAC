import sqlite3

# Function to rename file
def rename_file(file_id, new_filename):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Check if new file name is already in use
    cursor.execute("""SELECT * FROM files WHERE filename = ?""", (new_filename,))
    if cursor.fetchone() is not None:
        return 'File name already in use'

    # Rename file in database
    cursor.execute("""UPDATE files SET filename = ? WHERE id = ?""", (new_filename, file_id))

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Return success message
    return 'File renamed successfully'

# Test function with dummy file ID and filename
print(rename_file(1, 'newfile'))