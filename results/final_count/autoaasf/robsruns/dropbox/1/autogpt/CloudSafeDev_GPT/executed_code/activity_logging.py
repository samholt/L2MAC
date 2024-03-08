import sqlite3
import datetime

# Function to log a user's action
def log_action(username, action):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')
    cursor = conn.cursor()

    # Insert record into activity_log table
    cursor.execute('INSERT INTO activity_log (username, action, timestamp) VALUES (?, ?, ?)', (username, action, datetime.datetime.now()))
    conn.commit()
    conn.close()
    return 'Action logged successfully'