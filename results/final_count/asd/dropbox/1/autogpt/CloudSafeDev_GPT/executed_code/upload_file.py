import sqlite3

# Function to upload file
def upload_file(username, file_size):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Get user's storage used from database
    cursor.execute("""SELECT storage_used FROM users WHERE username = ?""", (username,))
    storage_used = cursor.fetchone()[0]

    # Update user's storage used in database
    cursor.execute("""UPDATE users SET storage_used = ? WHERE username = ?""", (storage_used + file_size, username))

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Return success message
    return 'File uploaded successfully'

# Test function with dummy user details and file size
print(upload_file('testuser', 1000))