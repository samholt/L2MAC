class User:
	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email
		self.reading_list = []
		self.recommendations = []
		self.following = []

	def create_user(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email

	def update_user(self, username=None, password=None, email=None):
		if username:
			self.username = username
		if password:
			self.password = password
		if email:
			self.email = email

	def delete_user(self):
		self.username = None
		self.password = None
		self.email = None
		self.reading_list = None
		self.recommendations = None
		self.following = None

	def follow_user(self, user):
		self.following.append(user)

	def unfollow_user(self, user):
		self.following.remove(user)

	def view_followed_users_reading_lists(self):
		return {user.username: user.reading_list for user in self.following}

	def view_followed_users_recommendations(self):
		return {user.username: user.recommendations for user in self.following}

	def add_to_reading_list(self, book):
		self.reading_list.append(book)

	def remove_from_reading_list(self, book):
		self.reading_list.remove(book)

	def add_recommendation(self, book):
		self.recommendations.append(book)

	def remove_recommendation(self, book):
		self.recommendations.remove(book)
