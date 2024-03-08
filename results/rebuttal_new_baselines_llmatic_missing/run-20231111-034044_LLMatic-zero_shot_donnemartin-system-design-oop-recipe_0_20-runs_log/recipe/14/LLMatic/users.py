class User:
	def __init__(self, id, name, email):
		self.id = id
		self.name = name
		self.email = email
		self.following = []
		self.feed = []
		self.liked_recipes = []

	def follow(self, user_to_follow):
		self.following.append(user_to_follow)
		user_to_follow.feed.append(f'{self.name} started following you.')

	def unfollow(self, user_to_unfollow):
		if user_to_unfollow in self.following:
			self.following.remove(user_to_unfollow)
			user_to_unfollow.feed.append(f'{self.name} stopped following you.')

	def get_feed(self):
		return self.feed


class UserManager:
	def __init__(self):
		self.users = {}

	def create_user(self, id, name, email):
		if id in self.users:
			return 'User already exists'
		self.users[id] = User(id, name, email)
		return 'User created successfully'

	def get_user(self, id):
		if id not in self.users:
			return None
		return self.users[id]

	def update_user(self, id, name=None, email=None):
		if id not in self.users:
			return 'User not found'
		if name:
			self.users[id].name = name
		if email:
			self.users[id].email = email
		return 'User updated successfully'

	def delete_user(self, id):
		if id not in self.users:
			return 'User not found'
		del self.users[id]
		return 'User deleted successfully'

	def get_user_feed(self, id):
		if id not in self.users:
			return 'User not found'
		return self.users[id].get_feed()
