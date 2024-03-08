class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.submitted_recipes = []
		self.favorite_recipes = []
		self.followed_users = []
		self.activity_feed = []

	def follow_user(self, user):
		if user not in self.followed_users:
			self.followed_users.append(user)
			return 'User followed successfully'
		return 'User already followed'

	def get_feed(self):
		feed = []
		for user in self.followed_users:
			feed.extend(user.activity_feed)
		return sorted(feed, key=lambda x: x['timestamp'], reverse=True)


class UserManager:
	def __init__(self):
		self.users = {}

	def create_user(self, username, password):
		if username in self.users:
			return 'Username already exists'
		self.users[username] = User(username, password)
		return 'User created successfully'

	def get_user(self, username):
		return self.users.get(username, 'User not found')

	def update_user(self, username, password=None, submitted_recipes=None, favorite_recipes=None, followed_users=None):
		user = self.get_user(username)
		if user == 'User not found':
			return user
		if password:
			user.password = password
		if submitted_recipes:
			user.submitted_recipes = submitted_recipes
		if favorite_recipes:
			user.favorite_recipes = favorite_recipes
		if followed_users:
			user.followed_users = followed_users
		return 'User updated successfully'

	def delete_user(self, username):
		if username in self.users:
			del self.users[username]
			return 'User deleted successfully'
		return 'User not found'

	def follow_user(self, follower_username, followee_username):
		follower = self.get_user(follower_username)
		followee = self.get_user(followee_username)
		if follower == 'User not found' or followee == 'User not found':
			return 'User not found'
		return follower.follow_user(followee)

	def get_feed(self, username):
		user = self.get_user(username)
		if user == 'User not found':
			return user
		return user.get_feed()
