import sqlite3

# Function to create links table
def create_links_table():
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Create links table
    cursor.execute("""CREATE TABLE links (
        id INTEGER PRIMARY KEY,
        link TEXT,
        password TEXT
    )""")

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Return success message
    return 'Links table created successfully'

# Test function
print(create_links_table())