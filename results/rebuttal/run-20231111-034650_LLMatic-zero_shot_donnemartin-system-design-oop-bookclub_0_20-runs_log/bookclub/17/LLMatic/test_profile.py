import pytest
from database import Database
from user import User
from profile import Profile

def test_profile():
	db = Database()
	user = User(db)
	profile = Profile(db)

	# Test get and update profile
	user.create_user('1', {'name': 'John', 'profile': {}})
	assert profile.get_profile('1') == {'name': 'John', 'profile': {}}
	profile.update_profile('1', {'bio': 'I love reading.'})
	assert profile.get_profile('1') == {'name': 'John', 'profile': {'bio': 'I love reading.'}}

	# Test list books
	user.update_user('1', {'name': 'John', 'profile': {'bio': 'I love reading.'}, 'books': ['book1', 'book2']})
	assert profile.list_books('1') == ['book1', 'book2']
