class User:
	def __init__(self, name, email, preferences):
		self.name = name
		self.email = email
		self.preferences = preferences
		self.past_events = []
		self.upcoming_events = []

	def create_profile(self):
		return {'name': self.name, 'email': self.email, 'preferences': self.preferences}

	def update_profile(self, name, email, preferences):
		self.name = name
		self.email = email
		self.preferences = preferences
		return {'name': self.name, 'email': self.email, 'preferences': self.preferences}

	def view_profile(self):
		return {'name': self.name, 'email': self.email, 'preferences': self.preferences, 'past_events': self.past_events, 'upcoming_events': self.upcoming_events}

	def save_event(self, event, event_type):
		if event_type == 'past':
			self.past_events.append(event)
		elif event_type == 'upcoming':
			self.upcoming_events.append(event)

	def get_events(self, event_type):
		if event_type == 'past':
			return self.past_events
		elif event_type == 'upcoming':
			return self.upcoming_events

mock_db = {}

def create_user(name, email, preferences):
	user = User(name, email, preferences)
	mock_db[email] = user
	return user.create_profile()

def update_user(email, name, preferences):
	user = mock_db.get(email)
	if user:
		return user.update_profile(name, email, preferences)

def view_user(email):
	user = mock_db.get(email)
	if user:
		return user.view_profile()

def save_user_event(email, event, event_type):
	user = mock_db.get(email)
	if user:
		user.save_event(event, event_type)

def get_user_events(email, event_type):
	user = mock_db.get(email)
	if user:
		return user.get_events(event_type)
