import sqlite3

# Function to update a user's profile
def update_profile(id, new_username, new_password, new_email):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')
    cursor = conn.cursor()

    # Update user's profile in the users table
    cursor.execute('UPDATE users SET username = ?, password = ?, email = ? WHERE id = ?', (new_username, new_password, new_email, id))
    conn.commit()
    conn.close()
    return 'Profile updated successfully'