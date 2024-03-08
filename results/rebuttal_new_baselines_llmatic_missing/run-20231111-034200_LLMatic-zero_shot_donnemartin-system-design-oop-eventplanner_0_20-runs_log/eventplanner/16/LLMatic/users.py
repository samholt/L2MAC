class User:
	def __init__(self, name):
		self.name = name
		self.preferences = {}
		self.events = {'past': [], 'upcoming': []}

	def create_profile(self, preferences):
		self.preferences = preferences

	def update_profile(self, preferences):
		self.preferences.update(preferences)

	def save_event(self, event, event_type):
		self.events[event_type].append(event)

	def get_events(self, event_type):
		return self.events[event_type]

users_db = {}

def create_user(name):
	user = User(name)
	users_db[name] = user
	return user

def get_user(name):
	return users_db.get(name, None)

def update_user(name, preferences):
	user = get_user(name)
	if user:
		user.update_profile(preferences)
	return user

def save_user_event(name, event, event_type):
	user = get_user(name)
	if user:
		user.save_event(event, event_type)
	return user

def get_user_events(name, event_type):
	user = get_user(name)
	if user:
		return user.get_events(event_type)
	return None
