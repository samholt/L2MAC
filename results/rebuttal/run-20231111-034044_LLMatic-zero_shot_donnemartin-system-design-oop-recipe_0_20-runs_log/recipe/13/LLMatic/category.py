class Category:
	def __init__(self, database):
		self.database = database

	def categorize_by_type(self, type):
		return [recipe for recipe in self.database if type in recipe.categories]

	def categorize_by_cuisine(self, cuisine):
		return [recipe for recipe in self.database if cuisine in recipe.categories]

	def categorize_by_dietary_needs(self, dietary_needs):
		return [recipe for recipe in self.database if dietary_needs in recipe.categories]
