class Category:
	def __init__(self, name):
		self.name = name
		self.recipes = []

	def add_recipe(self, recipe):
		self.recipes.append(recipe)

	def remove_recipe(self, recipe):
		if recipe in self.recipes:
			self.recipes.remove(recipe)
