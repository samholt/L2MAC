from models import User, URL
from datetime import datetime
import string
import random

users = {}
urls = {}

# existing functions...

def generate_random_short_link():
	return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

def generate_short_url(url, user, custom_short_link, expiration_date=None):
	short_url = custom_short_link if custom_short_link else generate_random_short_link()
	new_url = URL(original_url=url, short_url=short_url, user=user, clicks=0, click_data=[], expiration_date=expiration_date)
	urls[short_url] = new_url
	return short_url

def get_original_url(short_url):
	url = urls.get(short_url)
	if url and (not url.expiration_date or url.expiration_date > datetime.now()):
		return url.original_url
	return None

def record_click(short_url, ip):
	url = urls.get(short_url)
	if url:
		url.clicks += 1
		url.click_data.append({'ip': ip, 'time': datetime.now()})

def get_analytics(short_url):
	url = urls.get(short_url)
	if url:
		return {'clicks': url.clicks, 'click_data': url.click_data}
	return None

def get_all_urls():
	return [url.to_dict() for url in urls.values()]

def get_all_users():
	return [user.to_dict() for user in users.values()]

def delete_url(short_url):
	if short_url in urls:
		del urls[short_url]
		return True
	return False

def get_system_performance():
	total_clicks = sum(url.clicks for url in urls.values())
	return {'total_urls': len(urls), 'total_users': len(users), 'total_clicks': total_clicks}

def create_user(username, password):
	if username in users:
		return 'User already exists'
	new_user = User(username=username, password=password)
	users[username] = new_user
	return 'User created successfully'

def edit_user(username, new_password):
	user = users.get(username)
	if not user:
		return 'User not found'
	user.password = new_password
	return 'User updated successfully'

def delete_user(username):
	if username in users:
		del users[username]
		return 'User deleted successfully'
	return 'User not found'

