class Rating:
	def __init__(self, user, recipe, rating, review):
		self.user = user
		self.recipe = recipe
		self.rating = rating
		self.review = review

	def rate_recipe(self, new_rating):
		self.rating = new_rating

	def write_review(self, new_review):
		self.review = new_review

	@staticmethod
	def calculate_average_rating(ratings):
		return sum(ratings) / len(ratings) if ratings else 0
