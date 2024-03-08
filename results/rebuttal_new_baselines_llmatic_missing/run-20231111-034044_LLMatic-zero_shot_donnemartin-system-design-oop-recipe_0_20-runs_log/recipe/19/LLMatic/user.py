class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.submitted_recipes = []
		self.favorite_recipes = []
		self.followed_users = []

	def create_account(self, username, password):
		self.username = username
		self.password = password

	def manage_account(self, username, password):
		self.username = username
		self.password = password

	def save_favorite_recipe(self, recipe):
		self.favorite_recipes.append(recipe)

	def follow_user(self, user):
		self.followed_users.append(user)
