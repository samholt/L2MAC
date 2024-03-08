class Categories:
	def __init__(self):
		self.recipes = {}

	def search_by_ingredient(self, ingredient):
		return [recipe for recipe in self.recipes.values() if ingredient in recipe['ingredients']]

	def search_by_name(self, name):
		return [recipe for recipe in self.recipes.values() if name in recipe['name']]

	def search_by_category(self, category):
		return [recipe for recipe in self.recipes.values() if category in recipe['categories']]

	def categorize_by_type(self, type):
		return [recipe for recipe in self.recipes.values() if type == recipe['type']]

	def categorize_by_cuisine(self, cuisine):
		return [recipe for recipe in self.recipes.values() if cuisine in recipe['cuisine']]

	def categorize_by_diet(self, diet):
		return [recipe for recipe in self.recipes.values() if diet == recipe['diet']]
