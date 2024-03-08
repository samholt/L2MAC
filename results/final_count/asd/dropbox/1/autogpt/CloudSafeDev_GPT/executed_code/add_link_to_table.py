import sqlite3

# Function to add shareable link to links table
def add_link_to_table(link, password, expiry_date):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Add shareable link to links table
    cursor.execute("""INSERT INTO links (link, password, expiry_date) VALUES (?, ?, ?)""", (link, password, expiry_date))

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Return success message
    return 'Link added to table successfully'

# Test function with dummy link, password, and expiry date
print(add_link_to_table('dc937b59892604f5a86ac96936cd7ff09e25f18ae6b758e8014a24c7fa039e91', 'password', '2023-10-01'))