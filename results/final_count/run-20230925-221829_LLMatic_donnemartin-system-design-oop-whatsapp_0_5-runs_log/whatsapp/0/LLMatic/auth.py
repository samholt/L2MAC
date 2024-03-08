import random
import string

# Mock database
users_db = {}


def register_user(email, password):
	"""Register a new user."""
	if email in users_db:
		return 'Email already registered.'
	users_db[email] = password
	return 'User registered successfully.'


def generate_recovery_token(email):
	"""Generate a recovery token for a user."""
	if email not in users_db:
		return 'Email not registered.'
	token = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
	return token
