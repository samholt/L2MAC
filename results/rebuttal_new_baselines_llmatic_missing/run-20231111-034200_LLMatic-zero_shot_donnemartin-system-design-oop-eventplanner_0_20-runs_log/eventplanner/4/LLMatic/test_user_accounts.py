import pytest
import user_accounts

def test_import():
	assert user_accounts is not None

def test_user_creation():
	user = user_accounts.User('John Doe', 'Rock', 'Concert')
	assert user.name == 'John Doe'
	assert user.preferences == 'Rock'
	assert user.events == 'Concert'

def test_user_update():
	user = user_accounts.User('John Doe', 'Rock', 'Concert')
	user.update_profile(name='Jane Doe', preferences='Pop', events='Festival')
	assert user.name == 'Jane Doe'
	assert user.preferences == 'Pop'
	assert user.events == 'Festival'

