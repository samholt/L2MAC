class User:
	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email
		self.submitted_recipes = []
		self.favorite_recipes = []

	def submit_recipe(self, recipe_id):
		self.submitted_recipes.append(recipe_id)

	def favorite_recipe(self, recipe_id):
		self.favorite_recipes.append(recipe_id)

	def remove_favorite_recipe(self, recipe_id):
		if recipe_id in self.favorite_recipes:
			self.favorite_recipes.remove(recipe_id)
