import random
import string
import sqlite3

# Function to generate short URL
def generate_short_url():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

# Function to store URL in database
def store_url(original_url, short_url):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("INSERT INTO urls (original_url, short_url) VALUES (?, ?)", (original_url, short_url))
    conn.commit()
    conn.close()