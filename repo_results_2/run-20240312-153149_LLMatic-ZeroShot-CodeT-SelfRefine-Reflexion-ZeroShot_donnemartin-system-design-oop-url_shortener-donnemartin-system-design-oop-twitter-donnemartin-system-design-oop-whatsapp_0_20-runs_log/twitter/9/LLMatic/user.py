class User:
	def __init__(self):
		self.users = {}

	def register(self, email, username, password):
		if username in self.users:
			return False
		self.users[username] = {'email': email, 'password': password, 'is_active': True, 'profile_picture': '', 'bio': '', 'website_link': '', 'location': '', 'is_private': False, 'following': [], 'followers': [], 'posts': []}
		return True

	def authenticate(self, username, password):
		if username in self.users and self.users[username]['password'] == password:
			return True
		return False

	def reset_password(self, username, old_password, new_password):
		if username in self.users and self.users[username]['password'] == old_password:
			self.users[username]['password'] = new_password
			return True
		return False

	def edit_profile(self, username, profile_picture, bio, website_link, location):
		if username in self.users:
			self.users[username]['profile_picture'] = profile_picture
			self.users[username]['bio'] = bio
			self.users[username]['website_link'] = website_link
			self.users[username]['location'] = location
			return True
		return False

	def toggle_privacy(self, username):
		if username in self.users:
			self.users[username]['is_private'] = not self.users[username]['is_private']
			return True
		return False

	def follow_user(self, user, other_user):
		if user in self.users and other_user in self.users:
			self.users[user]['following'].append(other_user)
			self.users[other_user]['followers'].append(user)
			return True
		return False

	def unfollow_user(self, user, other_user):
		if user in self.users and other_user in self.users:
			self.users[user]['following'].remove(other_user)
			self.users[other_user]['followers'].remove(user)
			return True
		return False

	def get_timeline(self, user):
		if user in self.users:
			timeline = []
			for following in self.users[user]['following']:
				timeline.extend(self.users[following]['posts'])
			return timeline
		return []
