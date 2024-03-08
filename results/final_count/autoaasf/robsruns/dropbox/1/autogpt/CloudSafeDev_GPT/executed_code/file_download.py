import sqlite3

# Function to download a file
def download_file(file_id):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')
    cursor = conn.cursor()

    # Retrieve file information from files table
    cursor.execute('SELECT * FROM files WHERE id = ?', (file_id,))
    file = cursor.fetchone()
    if file is None:
        return 'File not found'

    conn.close()

    # Return file from designated directory
    with open(f'uploads/{file[2]}', 'rb') as f:
        return f.read()