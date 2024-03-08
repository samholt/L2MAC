import sqlite3

# Function to register a new user
def register_user(username, password, email):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')
    cursor = conn.cursor()

    # Check if username or email already exists
    cursor.execute('SELECT * FROM users WHERE username = ? OR email = ?', (username, email))
    if cursor.fetchone() is not None:
        return 'Username or email already exists'

    # Insert new user into users table
    cursor.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)', (username, password, email))
    conn.commit()
    conn.close()
    return 'User registered successfully'