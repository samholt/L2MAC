import sqlite3

class Database:
	def __init__(self, db_name):
		self.connection = sqlite3.connect(db_name)
		self.cursor = self.connection.cursor()

	def execute(self, query, params=None):
		if params is None:
			self.cursor.execute(query)
		else:
			self.cursor.execute(query, params)

	def commit(self):
		self.connection.commit()

	def fetchall(self):
		return self.cursor.fetchall()

	def close(self):
		self.connection.close()
