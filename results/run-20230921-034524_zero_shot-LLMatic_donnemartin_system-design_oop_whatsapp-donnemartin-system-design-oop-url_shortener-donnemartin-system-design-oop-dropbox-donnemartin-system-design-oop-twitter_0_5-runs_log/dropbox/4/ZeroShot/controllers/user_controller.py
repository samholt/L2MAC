from models.user import User

class UserController:
	def __init__(self):
		self.users = []

	def create_user(self, id, name, email):
		user = User(id, name, email)
		self.users.append(user)
		return user

	def get_user(self, id):
		for user in self.users:
			if user.id == id:
				return user
		return None

	def update_user(self, id, name, email):
		user = self.get_user(id)
		if user:
			user.name = name
			user.email = email
			return user
		return None
