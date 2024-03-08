import hashlib

# Mock database
users_db = {}


def hash_password(password):
	return hashlib.sha256(password.encode()).hexdigest()


def create_user(username, password, email):
	if username in users_db:
		return 'Username already exists'
	else:
		users_db[username] = {'password': hash_password(password), 'email': email, 'logged_in': False}
		return 'User created successfully'


def login(username, password):
	if username in users_db and users_db[username]['password'] == hash_password(password):
		users_db[username]['logged_in'] = True
		return 'Logged in successfully'
	else:
		return 'Invalid username or password'


def logout(username):
	if username in users_db:
		users_db[username]['logged_in'] = False
		return 'Logged out successfully'
	else:
		return 'Invalid username'


def recover_password(username):
	if username in users_db:
		return 'Password recovery email has been sent to ' + users_db[username]['email']
	else:
		return 'Invalid username'
