from database import Database

class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.files = []
		self.db = Database('file_storage.db')

	def register(self):
		query = 'INSERT INTO users (username, password) VALUES (?, ?)'
		params = (self.username, self.password)
		self.db.execute_query(query, params)
		self.db.commit_transaction()

	def login(self):
		# Login logic goes here
		pass

	def logout(self):
		# Logout logic goes here
		pass

	def get_files(self):
		# Logic to get user's files goes here
		return self.files
