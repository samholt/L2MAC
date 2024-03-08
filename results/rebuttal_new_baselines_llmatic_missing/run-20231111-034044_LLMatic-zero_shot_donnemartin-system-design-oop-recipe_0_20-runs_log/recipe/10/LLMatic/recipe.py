import datetime
class Recipe:
	def __init__(self, name, ingredients, instructions, images, categories):
		self.name = name
		self.ingredients = ingredients
		self.instructions = instructions
		self.images = images
		self.categories = categories
		self.reviews = []
		self.timestamp = datetime.datetime.now()

	def edit_recipe(self, name, ingredients, instructions, images, categories):
		self.name = name
		self.ingredients = ingredients
		self.instructions = instructions
		self.images = images
		self.categories = categories

	def validate_recipe(self):
		if not self.name or not self.ingredients or not self.instructions or not self.categories:
			return False
		return True

	def add_review(self, review):
		self.reviews.append(review)

	def average_rating(self):
		return sum([review.rating for review in self.reviews]) / len(self.reviews) if self.reviews else 0

	@staticmethod
	def search_recipes(recipes, search_term):
		return [recipe for recipe in recipes if search_term in recipe.name or search_term in recipe.ingredients or any(search_term in category for category in recipe.categories)]

	@staticmethod
	def categorize_recipes(recipes, category):
		return [recipe for recipe in recipes if category in recipe.categories]

