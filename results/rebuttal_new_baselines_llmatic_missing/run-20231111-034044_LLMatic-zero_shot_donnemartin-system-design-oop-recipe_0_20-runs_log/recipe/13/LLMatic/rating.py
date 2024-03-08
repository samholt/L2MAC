class Rating:
	def __init__(self, user, recipe, rating):
		self.user = user
		self.recipe = recipe
		self.rating = rating

	def rate_recipe(self, rating):
		if rating < 1 or rating > 5:
			return 'Invalid rating. Please rate between 1 and 5.'
		self.rating = rating
		return 'Rating updated successfully.'
