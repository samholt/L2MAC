class Admin:
	def __init__(self):
		self.managed_recipes = []

	def manage_recipe(self, recipe):
		self.managed_recipes.append(recipe)

	def remove_recipe(self, recipe):
		if recipe in self.managed_recipes:
			self.managed_recipes.remove(recipe)
			recipe.delete_recipe()

	def get_managed_recipes(self):
		return self.managed_recipes
