class Review:
	def __init__(self):
		self.reviews = {}

	def add_review(self, user_id, recipe_id, rating, review):
		if recipe_id not in self.reviews:
			self.reviews[recipe_id] = []
		self.reviews[recipe_id].append({'user_id': user_id, 'rating': rating, 'review': review})
		return {'status': 'success', 'message': 'Review added successfully'}

	def get_reviews(self, recipe_id):
		if recipe_id in self.reviews:
			return {'status': 'success', 'data': self.reviews[recipe_id]}
		else:
			return {'status': 'error', 'message': 'No reviews found for this recipe'}

	def delete_review(self, user_id, recipe_id):
		if recipe_id in self.reviews:
			for i in range(len(self.reviews[recipe_id])):
				if self.reviews[recipe_id][i]['user_id'] == user_id:
					self.reviews[recipe_id].pop(i)
					return {'status': 'success', 'message': 'Review deleted successfully'}
		return {'status': 'error', 'message': 'No review found for this user and recipe'}
