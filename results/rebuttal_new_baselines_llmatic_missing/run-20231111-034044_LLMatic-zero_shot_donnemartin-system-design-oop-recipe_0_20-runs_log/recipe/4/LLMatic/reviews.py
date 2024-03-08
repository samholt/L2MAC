class Review:
	def __init__(self):
		self.reviews = {}

	def add_review(self, user_id, recipe_id, rating, review):
		if recipe_id not in self.reviews:
			self.reviews[recipe_id] = []
		self.reviews[recipe_id].append({'user_id': user_id, 'rating': rating, 'review': review})

	def get_reviews(self, recipe_id):
		return self.reviews.get(recipe_id, [])

	def get_average_rating(self, recipe_id):
		reviews = self.get_reviews(recipe_id)
		if not reviews:
			return 0
		return sum([review['rating'] for review in reviews]) / len(reviews)
