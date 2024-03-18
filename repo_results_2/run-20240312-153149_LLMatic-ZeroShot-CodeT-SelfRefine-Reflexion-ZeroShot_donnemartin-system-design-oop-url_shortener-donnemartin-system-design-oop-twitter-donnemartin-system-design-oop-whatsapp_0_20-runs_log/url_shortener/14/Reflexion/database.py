from models import User, URL


users = {}
urls = {}


def get_user(user_id):
	return users.get(user_id)


def get_url(url_id):
	return urls.get(url_id)


def add_user(user):
	users[user.id] = user


def add_url(url):
	urls[url.id] = url


def delete_user(user_id):
	del users[user_id]


def delete_url(url_id):
	del urls[url_id]

