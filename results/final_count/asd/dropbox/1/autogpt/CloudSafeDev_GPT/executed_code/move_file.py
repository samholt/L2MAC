import sqlite3

# Function to move file
def move_file(file_id, new_directory):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Move file in database
    cursor.execute("""UPDATE files SET directory = ? WHERE id = ?""", (new_directory, file_id))

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Return success message
    return 'File moved successfully'

# Test function with dummy file ID and directory
print(move_file(1, '/new/directory'))