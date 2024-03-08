import sqlite3

# Function to remove user from shared folder
def remove_user_from_shared_folder(user, folder):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Remove user from shared_folders table
    cursor.execute("""DELETE FROM shared_folders WHERE user = ? AND folder = ?""", (user, folder))

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Return success message
    return 'User removed from shared folder successfully'

# Test function with dummy user and folder
print(remove_user_from_shared_folder('user1', 'folder1'))