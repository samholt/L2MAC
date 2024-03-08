class Recipe:
	def __init__(self, name, ingredients, instructions, images, categories):
		self.name = name
		self.ingredients = ingredients
		self.instructions = instructions
		self.images = images
		self.categories = categories
		self.ratings = []

	def submit_recipe(self):
		# Mock database
		db = {}
		db[self.name] = self
		return db[self.name]

	def edit_recipe(self, name, ingredients, instructions, images, categories):
		self.name = name
		self.ingredients = ingredients
		self.instructions = instructions
		self.images = images
		self.categories = categories
		return self

	def delete_recipe(self):
		# Mock database
		db = {}
		if self.name in db:
			del db[self.name]
		return db

	def rate_recipe(self, rating):
		self.ratings.append(rating)
		return sum(self.ratings) / len(self.ratings)
