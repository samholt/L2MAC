import sqlite3

# Function to retrieve original URL from database using short URL
def redirect_to_original_url(short_url):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("SELECT original_url FROM urls WHERE short_url = ?", (short_url,))
    original_url = c.fetchone()
    conn.close()
    return original_url