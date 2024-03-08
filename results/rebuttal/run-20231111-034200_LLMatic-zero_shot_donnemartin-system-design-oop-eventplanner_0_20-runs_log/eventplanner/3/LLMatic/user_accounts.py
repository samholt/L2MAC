class User:
	def __init__(self, name, preferences, event_history):
		self.name = name
		self.preferences = preferences
		self.event_history = event_history

mock_database = {}

def create_account(name, preferences):
	user = User(name, preferences, [])
	mock_database[name] = user
	return user

def delete_account(name):
	if name in mock_database:
		del mock_database[name]

def update_account(name, preferences):
	if name in mock_database:
		mock_database[name].preferences = preferences

def get_account(name):
	return mock_database.get(name, None)
