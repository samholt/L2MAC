import pytest
from user_profile import UserProfile

def test_create_profile():
	user_profile = UserProfile()
	user_profile.create_profile('1', 'John Doe')
	assert user_profile.profiles['1']['name'] == 'John Doe'

def test_list_books():
	user_profile = UserProfile()
	user_profile.create_profile('1', 'John Doe')
	user_profile.profiles['1']['books'].append('Book1')
	assert user_profile.list_books('1') == ['Book1']

def test_follow():
	user_profile = UserProfile()
	user_profile.create_profile('1', 'John Doe')
	user_profile.create_profile('2', 'Jane Doe')
	user_profile.follow('1', '2')
	assert '2' in user_profile.profiles['1']['following']
