from database import Database

class User:
	def __init__(self):
		self.db = Database()

	def create_account(self, username, password):
		# Check if user already exists
		if self.db.get('users', username) is not None:
			return 'User already exists'
		# Create new user
		self.db.insert('users', username, {'password': password, 'urls': []})
		return 'Account created successfully'

	def get_user_data(self, username):
		# Retrieve user data
		return self.db.get('users', username)

	def update_user_data(self, username, data):
		# Update user data
		self.db.update('users', username, data)
		return 'User data updated successfully'

	def delete_user(self, username):
		# Delete user
		self.db.delete('users', username)
		return 'User deleted successfully'
