import pytest
from user_accounts import User

def test_user_creation():
	user = User('John Doe', 'Music', [])
	assert user.name == 'John Doe'
	assert user.preferences == 'Music'
	assert user.event_history == []

def test_profile_update():
	user = User('John Doe', 'Music', [])
	user.update_profile(name='Jane Doe', preferences='Art')
	assert user.name == 'Jane Doe'
	assert user.preferences == 'Art'

def test_event_history():
	user = User('John Doe', 'Music', [])
	user.add_event_to_history('Concert')
	assert user.event_history == ['Concert']
