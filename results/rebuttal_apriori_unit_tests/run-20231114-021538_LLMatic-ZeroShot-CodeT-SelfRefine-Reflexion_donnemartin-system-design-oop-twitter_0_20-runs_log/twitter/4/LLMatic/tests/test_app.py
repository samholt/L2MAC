import pytest
import random
import string
from models import register_user, authenticate_user, edit_user_profile, create_post, delete_post, like_post, retweet_post, create_reply, users_db
from utils import search_users, search_posts

# ... existing tests ...

def random_string(length=10):
	"""Generates a random string of specified length."""
	return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def test_user_search():
	username = random_string()
	register_user(username, f'{username}@example.com', 'password')
	assert len(search_users(username)) > 0

def test_post_search():
	username = random_string()
	email = f'{username}@example.com'
	password = 'password'
	register_user(username, email, password)
	user_id = [user.id for user in users_db.values() if user.username == username][0]
	content = random_string()
	create_post(user_id, content)
	assert len(search_posts(content)) > 0
