class UserAccounts:
	def __init__(self):
		self.users = {}

	def create_account(self, username, password):
		if username in self.users:
			return 'Username already exists'
		self.users[username] = {'password': password, 'profile': {}, 'events': {'past': [], 'upcoming': []}}
		return 'Account created successfully'

	def customize_profile(self, username, profile):
		if username not in self.users:
			return 'User not found'
		self.users[username]['profile'] = profile
		return 'Profile updated successfully'

	def save_event(self, username, event, event_type):
		if username not in self.users:
			return 'User not found'
		if event_type not in ['past', 'upcoming']:
			return 'Invalid event type'
		self.users[username]['events'][event_type].append(event)
		return 'Event saved successfully'

	def get_events(self, username, event_type):
		if username not in self.users:
			return 'User not found'
		if event_type not in ['past', 'upcoming']:
			return 'Invalid event type'
		return self.users[username]['events'][event_type]
