import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('cloudsafe.db')

# Create cursor object
cursor = conn.cursor()

# Create table
cursor.execute("""CREATE TABLE users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL UNIQUE,
password TEXT NOT NULL,
email TEXT NOT NULL UNIQUE,
storage_used INTEGER DEFAULT 0
)""")

# Commit changes and close connection
conn.commit()
conn.close()