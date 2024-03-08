class Search:
	def __init__(self):
		# Mock database
		self.db = {}

	def search_by_name(self, name):
		results = [recipe for recipe in self.db.values() if recipe.name == name]
		return results

	def search_by_ingredients(self, ingredients):
		results = [recipe for recipe in self.db.values() if set(ingredients).issubset(set(recipe.ingredients))]
		return results

	def search_by_category(self, category):
		results = [recipe for recipe in self.db.values() if category in recipe.categories]
		return results
