class Rating:
	def __init__(self, user_id, recipe_id, rating):
		self.user_id = user_id
		self.recipe_id = recipe_id
		self.rating = rating

	def rate_recipe(self):
		# Mock database
		mock_db = {}
		mock_db[(self.user_id, self.recipe_id)] = self.rating
		return mock_db[(self.user_id, self.recipe_id)]
