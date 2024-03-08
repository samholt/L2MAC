import sqlite3

# Function to update user email
def update_email(username, new_email):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Update user email in database
    cursor.execute("""UPDATE users SET email = ? WHERE username = ?""", (new_email, username))

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Test function with dummy user details
update_email('testuser', 'newemail@example.com')