class User:
	users = {}

	def __init__(self, username, password):
		if not username or not password:
			raise ValueError('Missing required parameters')
		self.username = username
		self.password = password
		self.profile = {}
		self.following = []
		self.reading_list = []
		self.recommendations = []
		self.__class__.users[username] = self

	def create_profile(self, profile):
		if not profile:
			raise ValueError('Missing required parameters')
		self.profile = profile

	def update_profile(self, profile):
		if not profile:
			raise ValueError('Missing required parameters')
		self.profile.update(profile)

	def delete_profile(self):
		self.profile = {}

	def follow_user(self, user):
		if not user:
			raise ValueError('Missing required parameters')
		self.following.append(user)

	def display_reading_list(self):
		return self.reading_list

	def display_recommendations(self):
		return self.recommendations
