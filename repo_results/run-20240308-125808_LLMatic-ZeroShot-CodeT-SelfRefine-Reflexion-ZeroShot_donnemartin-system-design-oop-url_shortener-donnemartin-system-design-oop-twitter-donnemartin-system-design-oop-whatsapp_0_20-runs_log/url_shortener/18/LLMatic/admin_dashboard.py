url_db = {}
user_db = {}


def view_all_urls():
	return url_db


def delete_url(url):
	if url in url_db:
		del url_db[url]
		return 'URL deleted successfully'
	else:
		return 'URL does not exist'


def delete_user(username):
	if username in user_db:
		del user_db[username]
		return 'User deleted successfully'
	else:
		return 'User does not exist'


def monitor_system():
	# For simplicity, we'll just return the number of URLs and users
	return {'total_urls': len(url_db), 'total_users': len(user_db)}
