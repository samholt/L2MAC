from database import Database

db = Database()

def create_event(data):
	db.insert('events', data)

def update_event(event_id, data):
	event = db.get('events', event_id)
	if event is not None:
		event.update(data)
		db.update('events', event_id, event)

def get_events():
	return db.get_all('events')

def create_user(username, password_hash):
	return db.insert('users', {'username': username, 'password_hash': password_hash})

def get_user(username):
	users = db.get_all('users')
	for user in users:
		if user['username'] == username:
			return user
	return None
