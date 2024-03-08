import sqlite3
import hashlib
import uuid

# Function to check password
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

# Function to login user
def login_user(username, password):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Get user from database
    cursor.execute("""SELECT password FROM users WHERE username = ?""", (username,))
    result = cursor.fetchone()

    # Check password
    if result is None:
        return 'Username not found'
    elif check_password(result[0], password):
        return 'Login successful'
    else:
        return 'Incorrect password'

    # Close connection
    conn.close()

# Test function with dummy user details
print(login_user('testuser', 'testpassword'))