class Admin:
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.recipes = {}

	def add_recipe(self, recipe):
		self.recipes[recipe.id] = recipe

	def remove_recipe(self, recipe_id):
		if recipe_id in self.recipes:
			del self.recipes[recipe_id]

	def manage_recipes(self):
		return self.recipes

	def remove_inappropriate_content(self, review):
		if review.rating < 3:
			review.content = 'This review has been removed due to inappropriate content.'
