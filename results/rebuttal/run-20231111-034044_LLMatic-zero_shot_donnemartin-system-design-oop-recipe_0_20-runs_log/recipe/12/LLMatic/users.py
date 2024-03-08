class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.favorite_recipes = []
		self.followed_users = []

	def add_favorite_recipe(self, recipe):
		self.favorite_recipes.append(recipe)

	def remove_favorite_recipe(self, recipe):
		self.favorite_recipes.remove(recipe)

	def follow_user(self, user):
		self.followed_users.append(user)

	def unfollow_user(self, user):
		self.followed_users.remove(user)

mock_db = {}

def create_user(username, password):
	user = User(username, password)
	mock_db[username] = user

	return user

def get_user(username):
	return mock_db.get(username, None)

def delete_user(username):
	if username in mock_db:
		del mock_db[username]
