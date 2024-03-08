import sqlite3

# Function to fetch user details
def fetch_user_details(username):
    # Connect to SQLite database
    conn = sqlite3.connect('cloudsafe.db')

    # Create cursor object
    cursor = conn.cursor()

    # Fetch user details from database
    cursor.execute("""SELECT * FROM users WHERE username = ?""", (username,))
    result = cursor.fetchone()

    # Close connection
    conn.close()

    # Return user details
    return result

# Test function with dummy user details
print(fetch_user_details('testuser'))