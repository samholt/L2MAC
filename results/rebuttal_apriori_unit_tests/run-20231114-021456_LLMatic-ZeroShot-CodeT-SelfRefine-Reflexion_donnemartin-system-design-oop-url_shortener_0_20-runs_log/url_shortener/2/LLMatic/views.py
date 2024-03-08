from database import DATABASE, add_user, authenticate_user, deauthenticate_user
from models import User
from datetime import datetime

def register(data):
	"""Registers a new user."""
	username = data.get('username')
	password = data.get('password')
	if username and password:
		user = User(username, password)
		add_user(user)
		return 'User registered successfully'
	else:
		return 'Invalid data'

def login(data):
	"""Logs in a user."""
	username = data.get('username')
	password = data.get('password')
	if authenticate_user(username, password):
		return 'User logged in successfully'
	else:
		return 'Invalid username or password'

def logout(data):
	"""Logs out a user."""
	username = data.get('username')
	if deauthenticate_user(username):
		return 'User logged out successfully'
	else:
		return 'Invalid username'

def redirect(short_url):
	"""Redirects to the original URL associated with the given shortened URL."""
	if short_url in DATABASE:
		url = DATABASE[short_url]
		if url.expiration_date and url.expiration_date < datetime.now():
			return 'URL expired'
		else:
			return url.original_url
	else:
		return 'URL not found'

def get_all_urls(data):
	"""Returns all the URLs shortened by the user."""
	username = data.get('username')
	if username in DATABASE:
		return DATABASE[username].get_shortened_urls()
	else:
		return 'User not found'

def delete_url(data):
	"""Deletes a specified URL."""
	username = data.get('username')
	short_url = data.get('short_url')
	if username in DATABASE:
		DATABASE[username].delete_url(short_url)
		return 'URL deleted successfully'
	else:
		return 'User not found'

def delete_user(data):
	"""Deletes a specified user account."""
	username = data.get('username')
	if username in DATABASE:
		del DATABASE[username]
		return 'User deleted successfully'
	else:
		return 'User not found'

