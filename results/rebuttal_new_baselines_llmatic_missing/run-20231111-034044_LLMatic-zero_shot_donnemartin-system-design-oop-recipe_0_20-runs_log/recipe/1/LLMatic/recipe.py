class Recipe:
	def __init__(self, ingredients, instructions, images, category, dietary_needs, timestamp):
		self.ingredients = ingredients
		self.instructions = instructions
		self.images = images
		self.category = category
		self.dietary_needs = dietary_needs
		self.reviews = []
		self.timestamp = timestamp

	# Mock database
	recipe_db = {}

	def submit_recipe(self):
		self.recipe_db[self.instructions] = self
		return 'Recipe submitted successfully'

	def edit_recipe(self, new_ingredients, new_instructions, new_images, new_category, new_dietary_needs):
		self.ingredients = new_ingredients
		self.instructions = new_instructions
		self.images = new_images
		self.category = new_category
		self.dietary_needs = new_dietary_needs
		return 'Recipe edited successfully'

	def delete_recipe(self):
		if self.instructions in self.recipe_db:
			del self.recipe_db[self.instructions]
			return 'Recipe deleted successfully'
		else:
			return 'Recipe not found'

	def validate_recipe(self):
		if not self.ingredients or not self.instructions or not self.images or not self.category or not self.dietary_needs:
			return False
		return True

	def add_review(self, review):
		self.reviews.append(review)

	def get_average_rating(self):
		if not self.reviews:
			return 'No reviews yet'
		total_rating = sum([review.rating for review in self.reviews])
		average_rating = total_rating / len(self.reviews)
		return average_rating

	@classmethod
	def search_by_ingredient(cls, ingredient):
		results = [recipe for recipe in cls.recipe_db.values() if ingredient in recipe.ingredients]
		return results

	@classmethod
	def search_by_name(cls, name):
		results = [recipe for recipe in cls.recipe_db.values() if name in recipe.instructions]
		return results

	@classmethod
	def search_by_category(cls, category):
		results = [recipe for recipe in cls.recipe_db.values() if category in recipe.category]
		return results

	@classmethod
	def categorize_by_type(cls, type):
		results = [recipe for recipe in cls.recipe_db.values() if type in recipe.category]
		return results

	@classmethod
	def categorize_by_cuisine(cls, cuisine):
		results = [recipe for recipe in cls.recipe_db.values() if cuisine in recipe.category]
		return results

	@classmethod
	def categorize_by_dietary_needs(cls, dietary_needs):
		results = [recipe for recipe in cls.recipe_db.values() if dietary_needs == recipe.dietary_needs]
		return results

	def share_on_social_media(self):
		return 'Shared on social media'
