import sqlite3

# Function to add expiry date to shareable link
def add_expiry_date_to_link(link, expiry_date):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Add expiry date to link in links table
    cursor.execute("""UPDATE links SET expiry_date = ? WHERE link = ?""", (expiry_date, link))

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Return success message
    return 'Expiry date added to link successfully'

# Test function with dummy link and expiry date
print(add_expiry_date_to_link('dc937b59892604f5a86ac96936cd7ff09e25f18ae6b758e8014a24c7fa039e91', '2023-10-01'))