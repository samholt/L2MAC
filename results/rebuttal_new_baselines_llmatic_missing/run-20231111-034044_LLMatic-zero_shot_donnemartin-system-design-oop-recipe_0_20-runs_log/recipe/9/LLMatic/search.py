class Search:
	def __init__(self, database):
		self.database = database

	@classmethod
	def query(cls, query):
		# Here should be the logic to perform the search in the database using the query
		pass

	def search_by_ingredient(self, ingredient):
		results = []
		for recipe in self.database.values():
			if ingredient in recipe['ingredients']:
				results.append(recipe)
		return results

	def search_by_name(self, name):
		results = []
		for recipe in self.database.values():
			if name.lower() in recipe['name'].lower():
				results.append(recipe)
		return results

	def search_by_category(self, category):
		results = []
		for recipe in self.database.values():
			if category.lower() in recipe['category'].lower():
				results.append(recipe)
		return results
