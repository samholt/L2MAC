class Review:
	def __init__(self, id, user, rating, content):
		self.id = id
		self.user = user
		self.rating = rating
		self.content = content

	@staticmethod
	def create_review(id, user, rating, content):
		return Review(id, user, rating, content)

	@staticmethod
	def calculate_average_rating(reviews):
		return sum([review.rating for review in reviews]) / len(reviews) if reviews else 0
