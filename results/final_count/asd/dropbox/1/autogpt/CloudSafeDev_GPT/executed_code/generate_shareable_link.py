import sqlite3
import hashlib

# Function to generate shareable link
def generate_shareable_link(file_id):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Get file from files table
    cursor.execute("""SELECT * FROM files WHERE id = ?""", (file_id,))
    file = cursor.fetchone()

    # Close connection
    conn.close()

    # Generate shareable link
    link = hashlib.sha256(str(file).encode()).hexdigest()

    # Return shareable link
    return link

# Test function with dummy file ID
print(generate_shareable_link(1))