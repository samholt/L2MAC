class Recipe:
	def __init__(self, id, name, category, ingredients, instructions, ratings, reviews):
		self.id = id
		self.name = name
		self.category = category
		self.ingredients = ingredients
		self.instructions = instructions
		self.ratings = ratings
		self.reviews = reviews

	@staticmethod
	def create_recipe(id, name, category, ingredients, instructions):
		return Recipe(id, name, category, ingredients, instructions, [], [])

	@staticmethod
	def get_all_recipes():
		# This method should return all recipes. As we are mocking a database with an in memory dictionary, let's return an empty list for now.
		return []
