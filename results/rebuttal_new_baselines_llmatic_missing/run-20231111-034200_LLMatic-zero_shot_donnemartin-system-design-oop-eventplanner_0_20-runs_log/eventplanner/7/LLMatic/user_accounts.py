class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.profile = {}
		self.events = []

	def create_profile(self, profile):
		self.profile = profile

	def customize_profile(self, profile):
		self.profile.update(profile)

	def save_event(self, event):
		self.events.append(event)

	def get_events(self):
		return self.events

users = {}

def create_user(username, password):
	users[username] = User(username, password)

def get_user(username):
	return users.get(username, None)

