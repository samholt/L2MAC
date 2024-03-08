class Recipe:
	def __init__(self):
		self.recipes = {}

	def submit_recipe(self, recipe_id, recipe_data):
		self.recipes[recipe_id] = recipe_data

	def edit_recipe(self, recipe_id, recipe_data):
		if recipe_id in self.recipes:
			self.recipes[recipe_id] = recipe_data

	def delete_recipe(self, recipe_id):
		if recipe_id in self.recipes:
			del self.recipes[recipe_id]

	def get_recipe(self, recipe_id):
		return self.recipes.get(recipe_id, None)
