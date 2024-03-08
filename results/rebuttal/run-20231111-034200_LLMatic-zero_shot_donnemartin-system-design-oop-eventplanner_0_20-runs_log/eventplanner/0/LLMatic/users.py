class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.profile = {}
		self.events = {'past': [], 'upcoming': []}


def create_user(username, password):
	return User(username, password)


def customize_profile(user, profile):
	user.profile = profile


def save_event(user, event, event_type):
	user.events[event_type].append(event)


def get_events(user, event_type):
	return user.events[event_type]
