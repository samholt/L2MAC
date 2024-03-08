import sqlite3
import hashlib

# Function to set a password for a shareable link
def set_link_password(file_id, password):
    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')
    cursor = conn.cursor()

    # Store hashed password in the files table
    cursor.execute('UPDATE files SET password = ? WHERE id = ?', (hashed_password, file_id))
    conn.commit()
    conn.close()
    return 'Password set successfully'