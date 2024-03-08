class Category:
	def __init__(self, name):
		self.name = name
		self.recipes = []

	def add_recipe(self, recipe):
		self.recipes.append(recipe)

	def search_recipes(self, recipe_name):
		return [recipe for recipe in self.recipes if recipe.name == recipe_name]
