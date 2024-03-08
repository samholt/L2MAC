class Search:
	def __init__(self, database):
		self.database = database

	def search_by_name(self, name):
		return [recipe for recipe in self.database if recipe.name == name]

	def search_by_ingredient(self, ingredient):
		return [recipe for recipe in self.database if ingredient in recipe.ingredients]

	def search_by_category(self, category):
		return [recipe for recipe in self.database if category in recipe.categories]
