from database import Database

class Sharing:
	def __init__(self, file, shared_by, shared_with):
		self.file = file
		self.shared_by = shared_by
		self.shared_with = shared_with
		self.db = Database('file_storage.db')

	def share(self):
		query = 'INSERT INTO sharing (file, shared_by, shared_with) VALUES (?, ?, ?)'
		params = (self.file.file_name, self.shared_by.username, self.shared_with.username)
		self.db.execute_query(query, params)
		self.db.commit_transaction()

	def unshare(self):
		# Unshare logic goes here
		pass

	def get_shared_files(self):
		# Logic to get shared files goes here
		return self.shared_with

