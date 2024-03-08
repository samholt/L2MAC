import sqlite3

DB_NAME = 'chat.db'

class AuthService:
	@staticmethod
	def register(email, password):
		conn = sqlite3.connect(DB_NAME)
		c = conn.cursor()
		c.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, password))
		conn.commit()
		conn.close()

	@staticmethod
	def login(email, password):
		conn = sqlite3.connect(DB_NAME)
		c = conn.cursor()
		c.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
		user = c.fetchone()
		conn.close()
		return user
