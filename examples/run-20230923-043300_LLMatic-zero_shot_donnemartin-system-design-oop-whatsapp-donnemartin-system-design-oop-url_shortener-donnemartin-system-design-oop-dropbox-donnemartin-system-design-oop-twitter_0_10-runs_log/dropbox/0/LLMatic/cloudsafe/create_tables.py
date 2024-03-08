import sqlite3

# Connect to the database
conn = sqlite3.connect('cloudsafe.db')
c = conn.cursor()

# Create the 'users' table
c.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        profile_picture TEXT,
        storage_used INTEGER NOT NULL DEFAULT 0
    );
""")

# Commit the changes and close the connection
conn.commit()
conn.close()
