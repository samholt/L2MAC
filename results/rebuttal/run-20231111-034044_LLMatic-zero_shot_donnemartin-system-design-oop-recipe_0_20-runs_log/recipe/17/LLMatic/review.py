class Review:
	def __init__(self, user_id, recipe_id, review):
		self.user_id = user_id
		self.recipe_id = recipe_id
		self.review = review

	def write_review(self):
		# Mock database
		mock_db = {}
		mock_db[(self.user_id, self.recipe_id)] = self.review
		return mock_db[(self.user_id, self.recipe_id)]
