class Review:
	def __init__(self, user, recipe, rating, review_text):
		self.user = user
		self.recipe = recipe
		self.rating = rating
		self.review_text = review_text
		# Mock database
		self.review_db = {}

	def submit_review(self):
		if self.user and self.recipe and self.rating and self.review_text:
			self.review_db[self.user] = {'user': self.user, 'recipe': self.recipe, 'rating': self.rating, 'review_text': self.review_text}
			return 'Review submitted successfully'
		else:
			return 'Review submission failed'

	def to_dict(self):
		return {
			'user': self.user,
			'recipe': self.recipe,
			'rating': self.rating,
			'review_text': self.review_text
		}
