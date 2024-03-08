class Review:
	def __init__(self, user, recipe, rating, text):
		self.user = user
		self.recipe = recipe
		self.rating = rating
		self.text = text

	def write_review(self):
		return {'user': self.user, 'recipe': self.recipe, 'rating': self.rating, 'text': self.text}
