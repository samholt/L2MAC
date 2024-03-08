import sqlite3
import os
import datetime

# Function to upload a new version of a file
def upload_new_version(file_id, new_file):
    # Check new file's size
    if os.path.getsize(new_file) > 1000000:  # 1MB limit
        return 'File size exceeds limit'

    # Check new file's type
    filename = os.path.basename(new_file)
    if not filename.endswith(('.txt', '.pdf', '.jpg', '.png', '.docx')):
        return 'Invalid file type'

    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')
    cursor = conn.cursor()

    # Retrieve file information from files table
    cursor.execute('SELECT * FROM files WHERE id = ?', (file_id,))
    file = cursor.fetchone()
    if file is None:
        return 'File not found'

    # Store new file in designated directory
    os.makedirs('uploads', exist_ok=True)
    with open(f'uploads/{filename}', 'wb') as f:
        f.write(new_file.read())

    # Update file's information in the files table
    cursor.execute('UPDATE files SET filename = ?, size = ?, upload_date = ?, version = version + 1 WHERE id = ?', (filename, os.path.getsize(new_file), datetime.datetime.now(), file_id))
    conn.commit()
    conn.close()
    return 'New version uploaded successfully'