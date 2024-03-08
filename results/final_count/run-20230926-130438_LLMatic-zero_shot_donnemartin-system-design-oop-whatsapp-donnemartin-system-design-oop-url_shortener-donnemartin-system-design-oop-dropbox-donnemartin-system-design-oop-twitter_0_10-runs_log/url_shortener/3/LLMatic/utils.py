import models
import string
import random

users = {}

admins = ['admin']

def save_user(user):
	users[user.username] = user

def get_user_by_username(username):
	return users.get(username)

def get_all_users():
	return users.values()

def delete_user(user):
	del users[user.username]

def is_admin(username):
	return username in admins

def generate_short_url(custom_short_url=None, expiration_date=None):
	if custom_short_url:
		return custom_short_url
	else:
		return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
