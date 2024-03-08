class Review:
	def __init__(self, user, recipe, rating, review_text):
		self.user = user
		self.recipe = recipe
		self.rating = rating
		self.review_text = review_text

	@classmethod
	def post(cls, data):
		user = data['user']
		recipe = data['recipe']
		rating = data['rating']
		review_text = data['review_text']
		return cls(user, recipe, rating, review_text)

	def write_review(self, review_text):
		self.review_text = review_text

	def rate_recipe(self, rating):
		self.rating = rating

	def to_dict(self):
		return {
			'user': self.user,
			'recipe': self.recipe,
			'rating': self.rating,
			'review_text': self.review_text
		}
