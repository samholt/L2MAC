import sqlite3
import hashlib
import uuid

# Function to hash password
def hash_password(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

# Function to register user
def register_user(username, password, email):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Hash password
    hashed_password = hash_password(password)

    # Insert user into database
    cursor.execute("""INSERT INTO users (username, password, email) VALUES (?, ?, ?)""", (username, hashed_password, email))

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Test function with dummy user details
register_user('testuser', 'testpassword', 'testuser@example.com')