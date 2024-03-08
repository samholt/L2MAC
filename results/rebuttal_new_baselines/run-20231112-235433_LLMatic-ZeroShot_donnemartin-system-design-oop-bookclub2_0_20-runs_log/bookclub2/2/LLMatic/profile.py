class Profile:
	def __init__(self, profile_id, user_id):
		self.profile_id = profile_id
		self.user_id = user_id
		self.reading_list = []
		self.recommendations = []

	def add_book_to_reading_list(self, book_id):
		self.reading_list.append(book_id)

	def remove_book_from_reading_list(self, book_id):
		self.reading_list.remove(book_id)

	def add_recommendation(self, book_id):
		self.recommendations.append(book_id)

	def remove_recommendation(self, book_id):
		self.recommendations.remove(book_id)

	def get_profile_info(self):
		return {
			'profile_id': self.profile_id,
			'user_id': self.user_id,
			'reading_list': self.reading_list,
			'recommendations': self.recommendations
		}
