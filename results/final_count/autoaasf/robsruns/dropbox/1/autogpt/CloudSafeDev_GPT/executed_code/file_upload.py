import sqlite3
import os
import datetime

# Function to upload a file
def upload_file(user_id, filename, file):
    # Check file size
    if os.path.getsize(file) > 1000000:  # 1MB limit
        return 'File size exceeds limit'

    # Check file type
    if not filename.endswith(('.txt', '.pdf', '.jpg', '.png', '.docx')):
        return 'Invalid file type'

    # Store file in designated directory
    os.makedirs('uploads', exist_ok=True)
    with open(f'uploads/{filename}', 'wb') as f:
        f.write(file.read())

    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')
    cursor = conn.cursor()

    # Insert file information into files table
    cursor.execute('INSERT INTO files (user_id, filename, size, upload_date) VALUES (?, ?, ?, ?)', (user_id, filename, os.path.getsize(file), datetime.datetime.now()))
    conn.commit()
    conn.close()
    return 'File uploaded successfully'