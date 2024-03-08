import sqlite3

# Function to retrieve all URLs
def get_all_urls():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("SELECT * FROM urls")
    urls = c.fetchall()
    conn.close()
    return urls

# Function to delete a URL
def delete_url(short_url):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("DELETE FROM urls WHERE short_url = ?", (short_url,))
    conn.commit()
    conn.close()