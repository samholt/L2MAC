class Review:
	def __init__(self, user, recipe, rating, text):
		self.user = user
		self.recipe = recipe
		self.rating = rating
		self.text = text
		self.deleted = False

	def write_review(self):
		if not self.deleted:
			return {'user': self.user, 'recipe': self.recipe, 'rating': self.rating, 'text': self.text}
		else:
			return 'Review has been deleted'

	def delete_review(self):
		self.deleted = True
		return 'Review has been deleted'
