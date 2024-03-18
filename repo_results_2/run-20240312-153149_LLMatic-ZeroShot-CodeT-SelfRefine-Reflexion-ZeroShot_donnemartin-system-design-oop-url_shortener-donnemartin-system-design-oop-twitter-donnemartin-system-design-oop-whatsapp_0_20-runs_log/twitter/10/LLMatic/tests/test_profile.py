import pytest
from models import User
from database import users


def test_get_profile():
	user = User('test@test.com', 'testuser', 'testpassword')
	users['test@test.com'] = user
	assert user.get_profile() == {
		'email': 'test@test.com',
		'username': 'testuser',
		'profile_picture': None,
		'bio': None,
		'website_link': None,
		'location': None
	}


def test_update_profile():
	user = User('test@test.com', 'testuser', 'testpassword')
	users['test@test.com'] = user
	user.update_profile('picture.jpg', 'This is a bio', 'http://website.com', 'Location', True)
	assert user.get_profile() == {'message': 'This profile is private'}
	user.is_private = False
	assert user.get_profile() == {
		'email': 'test@test.com',
		'username': 'testuser',
		'profile_picture': 'picture.jpg',
		'bio': 'This is a bio',
		'website_link': 'http://website.com',
		'location': 'Location'
	}
