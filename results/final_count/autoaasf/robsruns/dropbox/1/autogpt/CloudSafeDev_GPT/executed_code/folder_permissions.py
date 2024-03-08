import sqlite3

# Function to set permissions for a user in a shared folder
def set_folder_permissions(folder_id, username, permissions):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')
    cursor = conn.cursor()

    # Update permissions in the shared_folders table
    cursor.execute('UPDATE shared_folders SET permissions = ? WHERE folder_id = ? AND username = ?', (permissions, folder_id, username))
    conn.commit()
    conn.close()
    return 'Permissions set successfully'