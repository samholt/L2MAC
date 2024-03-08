class Review:
	def __init__(self, user, recipe, rating, text):
		self.user = user
		self.recipe = recipe
		self.rating = rating
		self.text = text
		self.id = None

	def write_review(self, db):
		if self.id is None:
			self.id = len(db) + 1
				
		db[self.id] = self

	def delete_review(self, db):
		if self.id in db:
			del db[self.id]
