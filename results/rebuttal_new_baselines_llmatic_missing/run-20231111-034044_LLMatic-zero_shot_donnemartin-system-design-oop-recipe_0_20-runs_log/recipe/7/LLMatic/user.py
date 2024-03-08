class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.submitted_recipes = []
		self.favorite_recipes = []
		self.preferences = []

	def create_account(self, username, password):
		self.username = username
		self.password = password

	def manage_account(self, new_username, new_password):
		self.username = new_username
		self.password = new_password

	def save_favorite_recipe(self, recipe):
		self.favorite_recipes.append(recipe)

	def set_preferences(self, preferences):
		self.preferences = preferences

	def get_preferences(self):
		return self.preferences
