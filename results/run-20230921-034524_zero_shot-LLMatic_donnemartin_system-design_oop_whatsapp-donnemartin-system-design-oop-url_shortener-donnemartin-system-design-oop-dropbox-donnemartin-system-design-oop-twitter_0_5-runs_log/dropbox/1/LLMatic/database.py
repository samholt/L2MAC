import sqlite3

class Database:
	def __init__(self, db_name):
		self.conn = sqlite3.connect(db_name)
		self.cursor = self.conn.cursor()
		self.create_tables()

	def create_tables(self):
		self.cursor.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)')
		self.cursor.execute('CREATE TABLE IF NOT EXISTS files (file_name TEXT, file_size INTEGER, file_type TEXT, file_content BLOB)')
		self.cursor.execute('CREATE TABLE IF NOT EXISTS sharing (file TEXT, shared_by TEXT, shared_with TEXT)')

	def begin_transaction(self):
		self.cursor.execute('BEGIN TRANSACTION')

	def commit_transaction(self):
		self.conn.commit()

	def rollback_transaction(self):
		self.conn.rollback()

	def execute_query(self, query, params):
		self.cursor.execute(query, params)

	def fetch_all(self):
		return self.cursor.fetchall()

	def close(self):
		self.conn.close()

