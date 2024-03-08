import sqlite3
import uuid

# Function to generate a shareable link for a file
def generate_shareable_link(file_id):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')
    cursor = conn.cursor()

    # Retrieve file information from files table
    cursor.execute('SELECT * FROM files WHERE id = ?', (file_id,))
    file = cursor.fetchone()
    if file is None:
        return 'File not found'

    # Generate unique link for the file
    link = str(uuid.uuid4())

    # Store link in the files table
    cursor.execute('UPDATE files SET link = ? WHERE id = ?', (link, file_id))
    conn.commit()
    conn.close()
    return link