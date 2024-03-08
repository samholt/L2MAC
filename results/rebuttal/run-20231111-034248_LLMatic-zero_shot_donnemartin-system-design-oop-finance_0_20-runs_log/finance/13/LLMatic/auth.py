from werkzeug.security import generate_password_hash, check_password_hash
from models import User

# Mock database
users_db = {}


def register_user(username, password, email):
	"""Register a new user."""
	if username in users_db:
		return False
	
	hashed_password = generate_password_hash(password)
	users_db[username] = {'password': hashed_password, 'email': email}
	return True


def login_user(username, password):
	"""Log in an existing user."""
	if username not in users_db:
		return False
	
	user = users_db[username]
	return check_password_hash(user['password'], password)


def logout_user(username):
	"""Log out a user."""
	# In a real application, this would involve removing the user's session.
	# Here, we'll just return a message.
	if username in users_db:
		return f'{username} logged out.'
	else:
		return 'User not found.'
