class Search:
	def __init__(self, database):
		self.database = database

	def search_by_ingredients(self, ingredients):
		results = []
		for recipe in self.database['recipes'].values():
			if all(ingredient in recipe['ingredients'] for ingredient in ingredients):
				results.append(recipe)
		return results

	def search_by_name(self, name):
		results = []
		for recipe in self.database['recipes'].values():
			if name.lower() in recipe['name'].lower():
				results.append(recipe)
		return results

	def search_by_category(self, category):
		results = []
		for recipe in self.database['recipes'].values():
			if category.lower() in recipe['category'].lower():
				results.append(recipe)
		return results
