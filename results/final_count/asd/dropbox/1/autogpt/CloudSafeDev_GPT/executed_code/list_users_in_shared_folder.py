import sqlite3

# Function to list all users in shared folder
def list_users_in_shared_folder(folder):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Get all users from shared_folders table for specific folder
    cursor.execute("""SELECT user FROM shared_folders WHERE folder = ?""", (folder,))
    users = cursor.fetchall()

    # Close connection
    conn.close()

    # Return list of users
    return [user[0] for user in users]

# Test function with dummy folder
print(list_users_in_shared_folder('folder1'))