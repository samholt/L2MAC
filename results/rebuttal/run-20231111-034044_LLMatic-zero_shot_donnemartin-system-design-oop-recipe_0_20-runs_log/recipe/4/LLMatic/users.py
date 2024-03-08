class User:
	def __init__(self, id, name, email):
		self.id = id
		self.name = name
		self.email = email
		self.following = []
		self.feed = []

	def follow(self, user):
		if user not in self.following:
			self.following.append(user)
			return 'User followed successfully'
		return 'User already followed'

	def view_feed(self):
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
			return 'User does not exist'
		return self.users[id]

	def update_user(self, id, name=None, email=None):
		if id not in self.users:
			return 'User does not exist'
		if name:
			self.users[id].name = name
		if email:
			self.users[id].email = email
		return 'User updated successfully'

	def delete_user(self, id):
		if id not in self.users:
			return 'User does not exist'
		del self.users[id]
		return 'User deleted successfully'

	def follow_user(self, follower_id, followee_id):
		if follower_id not in self.users or followee_id not in self.users:
			return 'User does not exist'
		return self.users[follower_id].follow(followee_id)

	def view_user_feed(self, id):
		if id not in self.users:
			return 'User does not exist'
		return self.users[id].view_feed()
