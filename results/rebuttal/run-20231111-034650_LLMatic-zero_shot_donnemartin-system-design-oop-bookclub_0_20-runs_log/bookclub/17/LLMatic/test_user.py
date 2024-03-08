import pytest
from database import Database
from user import User

def test_user():
	db = Database()
	user = User(db)

	# Test create and get user
	user.create_user('1', {'name': 'John'})
	assert user.get_user('1') == {'name': 'John'}

	# Test update user
	user.update_user('1', {'name': 'John Doe'})
	assert user.get_user('1') == {'name': 'John Doe'}

	# Test delete user
	user.delete_user('1')
	assert user.get_user('1') == None
