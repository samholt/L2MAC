class User:
	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email
		self.submitted_recipes = []
		self.favorite_recipes = []

	def submit_recipe(self, recipe):
		self.submitted_recipes.append(recipe)

	def favorite_recipe(self, recipe):
		self.favorite_recipes.append(recipe)

	def remove_favorite_recipe(self, recipe):
		if recipe in self.favorite_recipes:
			self.favorite_recipes.remove(recipe)

	def get_submitted_recipes(self):
		return self.submitted_recipes

	def get_favorite_recipes(self):
		return self.favorite_recipes


class Profile:
	def __init__(self, user):
		self.user = user

	def display_submitted_recipes(self):
		return self.user.get_submitted_recipes()

	def display_favorite_recipes(self):
		return self.user.get_favorite_recipes()
