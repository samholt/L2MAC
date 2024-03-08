import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('cloudsafe.db')

# Create cursor object
cursor = conn.cursor()

# Create table for user accounts
cursor.execute('''CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    storage_used INTEGER DEFAULT 0
)''')

# Create table for file information
cursor.execute('''CREATE TABLE files (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    filename TEXT NOT NULL,
    size INTEGER NOT NULL,
    upload_date TEXT NOT NULL,
    version INTEGER DEFAULT 1,
    FOREIGN KEY(user_id) REFERENCES users(id)
)''')

# Commit changes and close connection
conn.commit()
conn.close()