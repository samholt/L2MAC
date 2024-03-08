import sqlite3
import time

# Function to set expiration for a URL
def set_expiration(short_url, expiration_time):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("UPDATE urls SET expiration_time = ? WHERE short_url = ?", (expiration_time, short_url))
    conn.commit()
    conn.close()

# Function to check and update the status of expired URLs
def check_expired_urls():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("SELECT * FROM urls WHERE expiration_time <= ?", (time.time(),))
    expired_urls = c.fetchall()
    for url in expired_urls:
        c.execute("DELETE FROM urls WHERE short_url = ?", (url[1],))
    conn.commit()
    conn.close()