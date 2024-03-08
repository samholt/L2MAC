class User:
	def __init__(self, username):
		self.username = username
		self.profile = {}
		self.following = []
		self.reading_list = []
		self.recommendations = []

	def create_profile(self, name, email):
		self.profile['name'] = name
		self.profile['email'] = email

	def follow_user(self, user):
		self.following.append(user)

	def add_to_reading_list(self, book):
		self.reading_list.append(book)

	def recommend_book(self, book):
		self.recommendations.append(book)
