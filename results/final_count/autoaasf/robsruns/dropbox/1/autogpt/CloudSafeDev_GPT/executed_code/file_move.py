import sqlite3
import os
import shutil

# Function to move a file to a different folder
def move_file(file_id, new_folder):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')
    cursor = conn.cursor()

    # Retrieve file information from files table
    cursor.execute('SELECT * FROM files WHERE id = ?', (file_id,))
    file = cursor.fetchone()
    if file is None:
        return 'File not found'

    # Update file's folder in the files table
    cursor.execute('UPDATE files SET folder = ? WHERE id = ?', (new_folder, file_id))
    conn.commit()
    conn.close()

    # Move file in the file system
    os.makedirs(f'uploads/{new_folder}', exist_ok=True)
    shutil.move(f'uploads/{file[2]}', f'uploads/{new_folder}/{file[2]}')
    return 'File moved successfully'