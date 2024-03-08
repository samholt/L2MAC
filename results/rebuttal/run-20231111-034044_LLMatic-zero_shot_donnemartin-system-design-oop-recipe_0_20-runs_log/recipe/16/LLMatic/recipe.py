class Recipe:
	def __init__(self, name, ingredients, instructions, images, categories, user_ratings):
		self.name = name
		self.ingredients = ingredients
		self.instructions = instructions
		self.images = images
		self.categories = categories
		self.user_ratings = user_ratings

	def submit_recipe(self):
		# Mock database
		mock_db = {}
		mock_db[self.name] = self
		return mock_db

	def edit_recipe(self, new_recipe):
		self.name = new_recipe.name
		self.ingredients = new_recipe.ingredients
		self.instructions = new_recipe.instructions
		self.images = new_recipe.images
		self.categories = new_recipe.categories
		self.user_ratings = new_recipe.user_ratings

	def delete_recipe(self, mock_db):
		if self.name in mock_db:
			del mock_db[self.name]

	def rate_recipe(self, user, rating):
		if user not in self.user_ratings:
			self.user_ratings[user] = []
		self.user_ratings[user].append(rating)
