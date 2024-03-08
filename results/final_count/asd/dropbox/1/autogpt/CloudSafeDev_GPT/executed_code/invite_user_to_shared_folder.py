import sqlite3

# Function to invite user to shared folder
def invite_user_to_shared_folder(user, folder):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Add user to shared_folders table
    cursor.execute("""INSERT INTO shared_folders (user, folder) VALUES (?, ?)""", (user, folder))

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Return success message
    return 'User invited to shared folder successfully'

# Test function with dummy user and folder
print(invite_user_to_shared_folder('user1', 'folder1'))