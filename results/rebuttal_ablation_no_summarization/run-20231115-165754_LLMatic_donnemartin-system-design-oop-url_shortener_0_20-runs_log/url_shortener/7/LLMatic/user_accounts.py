import hashlib

# Mock database for user accounts
USER_DB = {}


def create_account(username, password):
	if username in USER_DB:
		return {'result': False}
	USER_DB[username] = {
		'password': hashlib.md5(password.encode()).hexdigest(),
		'urls': []
	}
	return {'result': True}


def add_url_to_account(username, short_url):
	if username not in USER_DB:
		return {'result': False}
	USER_DB[username]['urls'].append(short_url)
	return {'result': True}


def remove_url_from_account(username, short_url):
	if username not in USER_DB or short_url not in USER_DB[username]['urls']:
		return {'result': False}
	USER_DB[username]['urls'].remove(short_url)
	return {'result': True}


def get_user_urls(username):
	if username not in USER_DB:
		return {'result': False}
	return {'result': USER_DB[username]['urls']}


def authenticate_user(username, password):
	if username not in USER_DB or USER_DB[username]['password'] != hashlib.md5(password.encode()).hexdigest():
		return {'result': False}
	return {'result': True}
