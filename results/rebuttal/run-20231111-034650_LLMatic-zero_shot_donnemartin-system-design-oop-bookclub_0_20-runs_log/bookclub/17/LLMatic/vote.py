class Vote:
	def __init__(self, id, book_id, user_id):
		self.id = id
		self.book_id = book_id
		self.user_id = user_id

	def cast(self, book_id, user_id):
		self.book_id = book_id
		self.user_id = user_id

	def get_data(self):
		return {'id': self.id, 'book_id': self.book_id, 'user_id': self.user_id}

	def update_data(self, book_id, user_id):
		self.book_id = book_id
		self.user_id = user_id

	def delete(self):
		self.id = None
		self.book_id = None
		self.user_id = None
