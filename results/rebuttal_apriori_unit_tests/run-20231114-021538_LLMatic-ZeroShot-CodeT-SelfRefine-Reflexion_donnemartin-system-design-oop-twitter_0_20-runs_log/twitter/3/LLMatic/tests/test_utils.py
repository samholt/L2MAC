import pytest
import random
import string
from utils import register_user, authenticate_user, edit_profile, users_db


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
	assert isinstance(authenticate_user(email, password), str)


def test_profile_editing():
	username = random_string()
	email = f'{random_string()}@example.com'
	password = random_string()
	register_user(username, email, password)
	user_id = len(users_db)
	new_bio = random_string(50)
	new_website = f'https://{random_string()}.com'
	new_location = random_string(15)
	assert edit_profile(user_id, new_bio, new_website, new_location) == True
