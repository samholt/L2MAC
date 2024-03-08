import pytest
from user import User

def test_create_profile():
	user = User('testuser')
	user.create_profile('Test User', 'testuser@example.com')
	assert user.profile['name'] == 'Test User'
	assert user.profile['email'] == 'testuser@example.com'

def test_follow_user():
	user1 = User('user1')
	user2 = User('user2')
	user1.follow_user(user2)
	assert user2 in user1.following

def test_add_to_reading_list():
	user = User('testuser')
	user.add_to_reading_list('Test Book')
	assert 'Test Book' in user.reading_list

def test_recommend_book():
	user = User('testuser')
	user.recommend_book('Test Book')
	assert 'Test Book' in user.recommendations
