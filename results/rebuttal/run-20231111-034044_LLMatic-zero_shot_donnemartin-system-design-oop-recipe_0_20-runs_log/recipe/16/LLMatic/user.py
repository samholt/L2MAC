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

	def manage_account(self, username=None, password=None):
		if username:
			self.username = username
		if password:
			self.password = password

	def save_recipe(self, recipe):
		self.favorite_recipes.append(recipe)

	def submit_recipe(self, recipe):
		self.submitted_recipes.append(recipe)

	def follow_user(self, user):
		self.followed_users.append(user)
