class User:
	def __init__(self, name, preferences=None, events=None):
		self.name = name
		self.preferences = preferences if preferences else {}
		self.events = events if events else []

	def create_profile(self, preferences):
		self.preferences = preferences

	def customize_profile(self, preferences):
		self.preferences.update(preferences)

	def save_event(self, event):
		self.events.append(event)

	def get_events(self):
		return self.events

# Mock database
users_db = {}

def create_user(name, preferences=None):
	user = User(name, preferences)
	users_db[name] = user
	return user

def get_user(name):
	return users_db.get(name, None)
