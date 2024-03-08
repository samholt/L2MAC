import sqlite3
from datetime import datetime

# Function to check if shareable link is valid
def is_link_valid(link, password):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Get link from links table
    cursor.execute("""SELECT * FROM links WHERE link = ?""", (link,))
    link_data = cursor.fetchone()

    # Close connection
    conn.close()

    # Check if link exists
    if link_data is None:
        return 'Link does not exist'

    # Check if password is correct
    if link_data[2] != password:
        return 'Incorrect password'

    # Check if link has expired
    if datetime.strptime(link_data[3], '%Y-%m-%d') < datetime.now():
        return 'Link has expired'

    # If all checks pass, return success message
    return 'Link is valid'

# Test function with dummy link and password
print(is_link_valid('dc937b59892604f5a86ac96936cd7ff09e25f18ae6b758e8014a24c7fa039e91', 'password'))