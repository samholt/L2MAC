class Profile:
	def __init__(self, database):
		self.database = database

	def get_profile(self, user_id):
		return self.database.get(self.database.users, user_id)

	def update_profile(self, user_id, profile_data):
		user = self.database.get(self.database.users, user_id)
		if user:
			user['profile'] = profile_data
			self.database.insert(self.database.users, user_id, user)

	def list_books(self, user_id):
		user = self.database.get(self.database.users, user_id)
		if user and 'books' in user:
			return user['books']
		return []
