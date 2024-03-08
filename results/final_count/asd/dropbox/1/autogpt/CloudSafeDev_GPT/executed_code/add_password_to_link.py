import sqlite3

# Function to add password to shareable link
def add_password_to_link(link, password):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Add password to link in links table
    cursor.execute("""UPDATE links SET password = ? WHERE link = ?""", (password, link))

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Return success message
    return 'Password added to link successfully'

# Test function with dummy link and password
print(add_password_to_link('dc937b59892604f5a86ac96936cd7ff09e25f18ae6b758e8014a24c7fa039e91', 'password'))