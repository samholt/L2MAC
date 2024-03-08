import sqlite3

# Function to add expiry_date column to links table
def add_expiry_date_column():
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Add expiry_date column to links table
    cursor.execute("""ALTER TABLE links ADD COLUMN expiry_date TEXT""")

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Return success message
    return 'Expiry date column added to links table successfully'

# Test function
print(add_expiry_date_column())