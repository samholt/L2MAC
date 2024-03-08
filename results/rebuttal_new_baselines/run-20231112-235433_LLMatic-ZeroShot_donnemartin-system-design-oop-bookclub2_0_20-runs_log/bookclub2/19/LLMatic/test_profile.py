import pytest
from profile import Profile

def test_create_profile():
	profile = Profile('1', 'User1')
	assert profile.id == '1'
	assert profile.user == 'User1'

def test_add_followed_user():
	profile = Profile('1', 'User1')
	profile.add_followed_user('User2')
	assert 'User2' in profile.followed_users

def test_update_profile():
	profile = Profile('1', 'User1')
	profile.update_profile('User3')
	assert profile.user == 'User3'
