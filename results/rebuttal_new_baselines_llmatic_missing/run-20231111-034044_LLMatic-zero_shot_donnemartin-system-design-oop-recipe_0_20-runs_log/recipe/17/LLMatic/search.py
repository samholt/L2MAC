class Search:
	def __init__(self, database):
		self.database = database

	def search_by_ingredient(self, ingredient):
		results = []
		for recipe in self.database.values():
			if ingredient in recipe.ingredients:
				results.append(recipe)
		return results

	def search_by_name(self, name):
		results = []
		for recipe in self.database.values():
			if name.lower() in recipe.name.lower():
				results.append(recipe)
		return results

	def search_by_category(self, category):
		results = []
		for recipe in self.database.values():
			if category.lower() in recipe.categories:
				results.append(recipe)
		return results

	def categorize_by_type(self, type):
		results = []
		for recipe in self.database.values():
			if type.lower() in recipe.categories:
				results.append(recipe)
		return results

	def categorize_by_cuisine(self, cuisine):
		results = []
		for recipe in self.database.values():
			if cuisine.lower() in recipe.categories:
				results.append(recipe)
		return results

	def categorize_by_diet(self, diet):
		results = []
		for recipe in self.database.values():
			if diet.lower() in recipe.categories:
				results.append(recipe)
		return results
