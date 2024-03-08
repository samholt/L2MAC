class Recipe:
	def __init__(self, name, category, instructions, submitted_by):
		self.name = name
		self.category = category
		self.instructions = instructions
		self.submitted_by = submitted_by
		self.reviews = []

	def add_review(self, review):
		self.reviews.append(review)

	def get_average_rating(self):
		if not self.reviews:
			return None
		return sum([review.rating for review in self.reviews]) / len(self.reviews)
