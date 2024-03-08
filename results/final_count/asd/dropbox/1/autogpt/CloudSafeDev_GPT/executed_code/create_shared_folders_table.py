import sqlite3

# Function to create shared_folders table
def create_shared_folders_table():
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Create shared_folders table
    cursor.execute("""CREATE TABLE shared_folders (user TEXT, folder TEXT)""")

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Return success message
    return 'Shared folders table created successfully'

# Test function
print(create_shared_folders_table())