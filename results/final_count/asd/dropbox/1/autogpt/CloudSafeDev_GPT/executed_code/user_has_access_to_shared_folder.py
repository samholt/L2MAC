import sqlite3

# Function to check if user has access to shared folder
def user_has_access_to_shared_folder(user, folder):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Check if user is in shared_folders table for specific folder
    cursor.execute("""SELECT user FROM shared_folders WHERE user = ? AND folder = ?""", (user, folder))
    users = cursor.fetchall()

    # Close connection
    conn.close()

    # Return True if user has access, False otherwise
    return len(users) > 0

# Test function with dummy user and folder
print(user_has_access_to_shared_folder('user1', 'folder1'))