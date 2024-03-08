from werkzeug.security import generate_password_hash, check_password_hash


class UserService:
	def __init__(self):
		self.users = {}

	def create_user(self, username, password):
		if username in self.users:
			return 'Username already exists'
		self.users[username] = {'password': generate_password_hash(password), 'urls': []}
		return {'username': username}

	def get_user_urls(self, username):
		user = self.users.get(username)
		if user:
			return user['urls']
		return 'User not found'
