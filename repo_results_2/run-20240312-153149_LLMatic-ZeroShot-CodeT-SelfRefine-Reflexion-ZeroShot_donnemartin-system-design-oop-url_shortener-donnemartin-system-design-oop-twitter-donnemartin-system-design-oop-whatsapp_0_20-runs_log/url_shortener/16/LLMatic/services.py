import string
import random
from urllib.parse import urlparse
from models import URL, Click, User
from datetime import datetime, timedelta

# Mock database
DATABASE = {}
CLICKS = {}
USERS = {}


def validate_url(url):
	try:
		result = urlparse(url)
		return all([result.scheme, result.netloc])
	except ValueError:
		return False


def generate_short_link(url, custom_short_link=None):
	if not validate_url(url):
		return 'Invalid URL'
	if not custom_short_link:
		custom_short_link = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
	shortened_url = URL(original_url=url, shortened_url=custom_short_link, user='user', creation_date=datetime.now(), expiration_date=datetime.now() + timedelta(days=30))
	DATABASE[custom_short_link] = shortened_url
	return shortened_url

def get_original_url(short_url):
	url = DATABASE.get(short_url)
	if url is None:
		return None
	return url.original_url

def record_click(url, location):
	click = Click(url=url, click_date=datetime.now(), location=location)
	if url in CLICKS:
		CLICKS[url].append(click)
	else:
		CLICKS[url] = [click]
	return click

def get_clicks(url):
	return CLICKS.get(url, [])

def create_user(username, password):
	if username in USERS:
		return 'Username already exists'
	user = User(username=username, password=password, urls=[])
	USERS[username] = user
	return user

def get_user(username):
	return USERS.get(username)

def edit_user(username, new_password):
	user = USERS.get(username)
	if user is None:
		return 'User not found'
	user.password = new_password
	return user

def delete_user(username):
	if username in USERS:
		del USERS[username]
		return 'User deleted'
	return 'User not found'

def get_all_urls():
	return list(DATABASE.values())

def delete_url(short_url):
	if short_url in DATABASE:
		del DATABASE[short_url]
		return 'URL deleted'
	return 'URL not found'

def get_all_users():
	return list(USERS.values())
