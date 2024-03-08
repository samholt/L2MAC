import sqlite3


class Database:
	def __init__(self, db_name):
		self.conn = sqlite3.connect(db_name)
		self.cursor = self.conn.cursor()

	def start_transaction(self):
		self.cursor.execute('BEGIN TRANSACTION')

	def commit_transaction(self):
		self.conn.commit()

	def execute_query(self, query, params=None):
		if params:
			self.cursor.execute(query, params)
		else:
			self.cursor.execute(query)
		return self.cursor.fetchall()

	def close(self):
		self.conn.close()
