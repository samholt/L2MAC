import sqlite3

# Function to delete shareable link from links table
def delete_link_from_table(link):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Delete shareable link from links table
    cursor.execute("""DELETE FROM links WHERE link = ?""", (link,))

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Return success message
    return 'Link deleted from table successfully'

# Test function with dummy link
print(delete_link_from_table('dc937b59892604f5a86ac96936cd7ff09e25f18ae6b758e8014a24c7fa039e91'))