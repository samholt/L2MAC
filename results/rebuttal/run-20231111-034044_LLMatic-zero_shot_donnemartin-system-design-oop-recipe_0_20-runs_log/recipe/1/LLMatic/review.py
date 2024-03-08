class Review:
	def __init__(self, user, recipe, rating, review_text):
		self.user = user
		self.recipe = recipe
		self.rating = rating
		self.review_text = review_text

	# Mock database
	review_db = {}

	def submit_review(self):
		if self.validate_review():
			self.review_db[(self.user, self.recipe)] = self
			return 'Review submitted successfully'
		else:
			return 'Invalid review'

	def validate_review(self):
		if not self.user or not self.recipe or not self.rating or not self.review_text:
			return False
		if self.rating < 1 or self.rating > 5:
			return False
		return True

	@classmethod
	def get_reviews_for_recipe(cls, recipe):
		results = [review for review in cls.review_db.values() if review.recipe == recipe]
		return results
