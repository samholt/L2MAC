class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.submitted_recipes = []
		self.favorite_recipes = []
		self.preferences = []
		self.interest_areas = []

	def create_account(self, username, password):
		self.username = username
		self.password = password

	def manage_account(self, username, password):
		self.username = username
		self.password = password

	def save_favorite_recipe(self, recipe):
		self.favorite_recipes.append(recipe)

	def set_preferences(self, preferences):
		self.preferences = preferences

	def set_interest_areas(self, interest_areas):
		self.interest_areas = interest_areas
