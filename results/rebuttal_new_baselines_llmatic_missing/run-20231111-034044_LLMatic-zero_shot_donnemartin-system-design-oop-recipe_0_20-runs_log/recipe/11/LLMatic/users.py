from database import MockDatabase

class User:
	def __init__(self, id, name, email, following=[]):
		self.id = id
		self.name = name
		self.email = email
		self.following = following

	def follow(self, user):
		if user.id not in self.following:
			self.following.append(user.id)

	def unfollow(self, user):
		if user.id in self.following:
			self.following.remove(user.id)

class UserManager:
	def __init__(self, db):
		self.db = db

	def create_user(self, id, name, email):
		if id in self.db.users:
			return 'User already exists'
		user = User(id, name, email)
		self.db.add_user(user)
		return user

	def get_user(self, id):
		return self.db.users.get(id, 'User not found')

	def delete_user(self, id):
		if id not in self.db.users:
			return 'User not found'
		del self.db.users[id]
		return 'User deleted successfully'
