import sqlite3

# Function to login a user
def login_user(username, password):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')
    cursor = conn.cursor()

    # Check if username and password match a record in the users table
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    if cursor.fetchone() is None:
        return 'Invalid username or password'

    conn.close()
    return 'User logged in successfully'