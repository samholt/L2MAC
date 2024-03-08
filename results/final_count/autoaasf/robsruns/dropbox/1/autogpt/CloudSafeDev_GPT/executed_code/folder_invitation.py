import sqlite3

# Function to invite a user to a folder
def invite_user_to_folder(folder_id, invitee_username):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')
    cursor = conn.cursor()

    # Check if invitee exists
    cursor.execute('SELECT * FROM users WHERE username = ?', (invitee_username,))
    if cursor.fetchone() is None:
        return 'Invitee does not exist'

    # Insert record into shared_folders table
    cursor.execute('INSERT INTO shared_folders (folder_id, username) VALUES (?, ?)', (folder_id, invitee_username))
    conn.commit()
    conn.close()
    return 'User invited successfully'