class Review:
	def __init__(self, user, recipe, rating=0, review_text=''):
		self.user = user
		self.recipe = recipe
		self.rating = rating
		self.review_text = review_text

	def rate_recipe(self, rating):
		self.rating = rating

	def review_recipe(self, review_text):
		self.review_text = review_text

	@staticmethod
	def calculate_average_rating(reviews):
		if not reviews:
			return 0
		return sum([review.rating for review in reviews]) / len(reviews)
