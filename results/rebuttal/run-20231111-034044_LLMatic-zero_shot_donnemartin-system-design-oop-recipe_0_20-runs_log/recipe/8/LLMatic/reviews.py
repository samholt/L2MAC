class Review:
	def __init__(self, username, recipe, rating, review_text):
		self.username = username
		self.recipe = recipe
		self.rating = rating
		self.review_text = review_text


mock_db = {}


def submit_review(username, recipe, rating, review_text):
	review = Review(username, recipe, rating, review_text)
	mock_db[username] = review
	return review


def get_review(username):
	return mock_db.get(username, None)

