class UserService:
	def __init__(self):
		self.users = {}

	def get_users(self):
		return self.users

	def register_user(self, name, email, password):
		user_id = len(self.users) + 1
		new_user = {'id': user_id, 'name': name, 'email': email, 'password': password}
		self.users[user_id] = new_user
		return new_user

	def authenticate_user(self, email, password):
		for user in self.users.values():
			if user['email'] == email and user['password'] == password:
				return user
		return None

	def get_profile(self, user_id):
		return self.users.get(user_id, None)
