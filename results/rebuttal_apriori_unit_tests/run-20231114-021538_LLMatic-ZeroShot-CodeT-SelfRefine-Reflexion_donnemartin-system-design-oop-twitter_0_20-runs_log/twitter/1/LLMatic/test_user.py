import pytest
import random
import string
from user import register_user, authenticate_user, edit_profile, toggle_privacy, follow_user, unfollow_user

def random_string(length=10):
	return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def test_user_registration():
	username = random_string()
	email = f'{random_string()}@example.com'
	password = random_string()
	assert register_user(username, email, password) == True

def test_user_authentication():
	username = random_string()
	email = f'{random_string()}@example.com'
	password = random_string()
	register_user(username, email, password)
	assert authenticate_user(email, password) == True

def test_edit_profile():
	username = random_string()
	email = f'{random_string()}@example.com'
	password = random_string()
	register_user(username, email, password)
	bio = random_string(50)
	website_link = f'https://{random_string()}.com'
	location = random_string(15)
	assert edit_profile(email, bio, website_link, location) == True

def test_toggle_privacy():
	username = random_string()
	email = f'{random_string()}@example.com'
	password = random_string()
	register_user(username, email, password)
	assert toggle_privacy(email) == True

def test_follow_unfollow():
	username1 = random_string()
	email1 = f'{random_string()}@example.com'
	password1 = random_string()
	register_user(username1, email1, password1)
	username2 = random_string()
	email2 = f'{random_string()}@example.com'
	password2 = random_string()
	register_user(username2, email2, password2)
	assert follow_user(email1, 2) == True
	assert unfollow_user(email1, 2) == True
