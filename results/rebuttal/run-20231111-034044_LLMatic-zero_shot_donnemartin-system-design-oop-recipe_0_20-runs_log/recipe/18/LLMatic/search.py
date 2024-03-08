class Search:
	def __init__(self, recipe_db):
		self.recipe_db = recipe_db

	def search_by_name(self, name):
		return [recipe for recipe in self.recipe_db if recipe['name'] == name]

	def search_by_ingredient(self, ingredient):
		return [recipe for recipe in self.recipe_db if ingredient in recipe['ingredients']]

	def search_by_category(self, category):
		return [recipe for recipe in self.recipe_db if category in recipe['categories']]

	def categorize_by_type(self, type):
		return [recipe for recipe in self.recipe_db if type in recipe['categories']]

	def categorize_by_cuisine(self, cuisine):
		return [recipe for recipe in self.recipe_db if cuisine in recipe['categories']]

	def categorize_by_diet(self, diet):
		return [recipe for recipe in self.recipe_db if diet in recipe['categories']]
