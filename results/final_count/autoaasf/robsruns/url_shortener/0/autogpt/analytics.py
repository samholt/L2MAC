import sqlite3
import time

# Function to record usage of short URL
def record_usage(short_url):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("INSERT INTO usage (short_url, timestamp) VALUES (?, ?)", (short_url, time.time()))
    conn.commit()
    conn.close()

# Function to retrieve usage statistics
def get_usage_statistics(short_url):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM usage WHERE short_url = ?", (short_url,))
    usage_count = c.fetchone()
    conn.close()
    return usage_count