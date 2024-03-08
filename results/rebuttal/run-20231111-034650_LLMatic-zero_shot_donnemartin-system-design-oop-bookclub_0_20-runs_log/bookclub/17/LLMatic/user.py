class User:
	def __init__(self, database):
		self.database = database

	def create_user(self, id, user_data):
		self.database.insert(self.database.users, id, user_data)

	def get_user(self, id):
		return self.database.get(self.database.users, id)

	def update_user(self, id, user_data):
		if self.get_user(id):
			self.database.insert(self.database.users, id, user_data)

	def delete_user(self, id):
		self.database.delete(self.database.users, id)
