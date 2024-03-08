class Review:
	def __init__(self, user, recipe, review):
		self.user = user
		self.recipe = recipe
		self.review = review

	def write_review(self, review):
		self.review = review
		return 'Review updated successfully.'
