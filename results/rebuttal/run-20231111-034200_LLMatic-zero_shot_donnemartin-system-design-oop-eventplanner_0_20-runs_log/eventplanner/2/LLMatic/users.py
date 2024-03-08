class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.profile = {}
		self.events = {'past': [], 'upcoming': []}

	def customize_profile(self, profile_data):
		self.profile.update(profile_data)

	def save_event(self, event, event_type):
		self.events[event_type].append(event)

	def get_events(self, event_type):
		return self.events[event_type]

users_db = {}

def create_user(username, password):
	if username in users_db:
		return 'User already exists'
	else:
		users_db[username] = User(username, password)
		return 'User created successfully'

def get_user(username):
	return users_db.get(username, 'User not found')

def update_user_profile(username, profile_data):
	user = get_user(username)
	if isinstance(user, User):
		user.customize_profile(profile_data)
		return 'Profile updated successfully'
	return user

def save_user_event(username, event, event_type):
	user = get_user(username)
	if isinstance(user, User):
		user.save_event(event, event_type)
		return 'Event saved successfully'
	return user

def get_user_events(username, event_type):
	user = get_user(username)
	if isinstance(user, User):
		return user.get_events(event_type)
	return user
