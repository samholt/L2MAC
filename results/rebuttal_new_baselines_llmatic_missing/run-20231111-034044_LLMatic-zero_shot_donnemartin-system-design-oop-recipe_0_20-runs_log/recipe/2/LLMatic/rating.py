class Rating:
	def __init__(self, user, recipe, rating, review):
		self.user = user
		self.recipe = recipe
		self.rating = rating
		self.review = review

	@staticmethod
	def calculate_average_rating(ratings):
		return sum(rating.rating for rating in ratings) / len(ratings) if ratings else 0
