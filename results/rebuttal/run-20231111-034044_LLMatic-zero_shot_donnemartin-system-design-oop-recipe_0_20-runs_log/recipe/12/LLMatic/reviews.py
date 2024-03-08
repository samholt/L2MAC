class Review:
	def __init__(self):
		self.reviews = {}

	def add_review(self, user_id, recipe_id, rating, review):
		if recipe_id not in self.reviews:
			self.reviews[recipe_id] = []
		self.reviews[recipe_id].append({'user_id': user_id, 'rating': rating, 'review': review})

	def edit_review(self, user_id, recipe_id, rating, review):
		for r in self.reviews[recipe_id]:
			if r['user_id'] == user_id:
				r['rating'] = rating
				r['review'] = review

	def get_average_rating(self, recipe_id):
		total_rating = 0
		for r in self.reviews[recipe_id]:
			total_rating += r['rating']
		return total_rating / len(self.reviews[recipe_id]) if self.reviews[recipe_id] else 0
