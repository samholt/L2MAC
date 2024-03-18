import pytest
from user import register, users_db, User
from post import create_post, post_db
from recommend import recommend


def setup_module(module):
	# Create users
	for i in range(10):
		register(f'user{i}@test.com', f'user{i}', 'password', False)
	
	# Create posts
	for i in range(10):
		create_post(users_db[f'user{i}'], f'post{i}')
	
	# Follow users
	for i in range(5):
		users_db['user0'].follow(users_db[f'user{i}'])
		users_db['user1'].follow(users_db[f'user{i}'])
	
	# Make sure user0 and user1 have mutual followers
	users_db['user2'].follow(users_db['user0'])
	users_db['user2'].follow(users_db['user1'])
	users_db['user3'].follow(users_db['user0'])
	users_db['user3'].follow(users_db['user1'])
	users_db['user4'].follow(users_db['user0'])
	users_db['user4'].follow(users_db['user1'])


def test_recommend():
	recommendations = recommend(users_db['user0'])
	assert len(recommendations) > 0
	assert all([isinstance(user, User) for user in recommendations])

