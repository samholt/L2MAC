class Admin:
	def __init__(self):
		self.recipes = {}
		self.reviews = {}

	@classmethod
	def perform_action(cls, data):
		# Here should be the logic to perform the admin action using the data
		pass

	def manage_recipes(self, recipe_id, action):
		if action == 'delete':
			if recipe_id in self.recipes:
				del self.recipes[recipe_id]
				return 'Recipe deleted successfully'
			else:
				return 'Recipe not found'
		elif action == 'view':
			if recipe_id in self.recipes:
				return self.recipes[recipe_id]
			else:
				return 'Recipe not found'

	def manage_reviews(self, review_id, action):
		if action == 'delete':
			if review_id in self.reviews:
				del self.reviews[review_id]
				return 'Review deleted successfully'
			else:
				return 'Review not found'
		elif action == 'view':
			if review_id in self.reviews:
				return self.reviews[review_id]
			else:
				return 'Review not found'
