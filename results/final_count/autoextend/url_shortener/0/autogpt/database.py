import sqlite3


class Database:
    def __init__(self, db_name: str = 'url_shortener.db'):
        self.conn = sqlite3.connect(db_name)
        self._create_table()

    def _create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS url_mapping
                     (original_url TEXT PRIMARY KEY, shortened_url TEXT UNIQUE)''')
        self.conn.commit()

    def store_url_mapping(self, original_url: str, shortened_url: str):
        cursor = self.conn.cursor()
        cursor.execute('INSERT OR IGNORE INTO url_mapping (original_url, shortened_url) VALUES (?, ?)', (original_url, shortened_url))
        self.conn.commit()

    def get_original_url(self, shortened_url: str) -> str:
        cursor = self.conn.cursor()
        cursor.execute('SELECT original_url FROM url_mapping WHERE shortened_url = ?', (shortened_url,))
        result = cursor.fetchone()
        return result[0] if result else None

    def get_shortened_url(self, original_url: str) -> str:
        cursor = self.conn.cursor()
        cursor.execute('SELECT shortened_url FROM url_mapping WHERE original_url = ?', (original_url,))
        result = cursor.fetchone()
        return result[0] if result else None