import hashlib

# Mock database
users_db = {}


def hash_password(password):
	return hashlib.sha256(password.encode()).hexdigest()


def create_user(username, password, email):
	if username in users_db:
		return 'Username already exists'
	else:
		users_db[username] = {'password': hash_password(password), 'email': email}
		return 'User created successfully'


def login(username, password):
	if username in users_db and users_db[username]['password'] == hash_password(password):
		return 'Login successful'
	else:
		return 'Invalid username or password'


def recover_password(username):
	if username in users_db:
		return 'Password recovery email sent'
	else:
		return 'Username does not exist'
