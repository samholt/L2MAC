import hashlib

# Mock database
users_db = {}


def hash_password(password):
	return hashlib.sha256(password.encode()).hexdigest()


def login(username, password):
	if username in users_db and users_db[username]['password'] == hash_password(password):
		users_db[username]['logged_in'] = True
		return True
	return False


def logout(username):
	if username in users_db:
		users_db[username]['logged_in'] = False
		return True
	return False


def is_authenticated(username):
	return users_db.get(username, {}).get('logged_in', False)
