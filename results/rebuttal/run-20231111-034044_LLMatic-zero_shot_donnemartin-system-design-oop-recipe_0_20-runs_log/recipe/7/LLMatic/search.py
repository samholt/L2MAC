class Search:
	def __init__(self, recipes):
		self.recipes = recipes

	def search_by_name(self, name):
		return [recipe for recipe in self.recipes if name.lower() in recipe.name.lower()]

	def search_by_category(self, category):
		return [recipe for recipe in self.recipes if category.lower() in recipe.category.lower()]
