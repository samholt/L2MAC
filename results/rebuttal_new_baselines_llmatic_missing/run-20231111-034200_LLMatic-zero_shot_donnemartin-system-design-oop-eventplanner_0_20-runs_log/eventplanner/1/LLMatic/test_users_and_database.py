import pytest
from users import User
from database import Database

def test_user_creation():
	user = User('1', 'John Doe', 'johndoe@example.com', 'likes outdoor events')
	assert user.user_id == '1'
	assert user.name == 'John Doe'
	assert user.contact_info == 'johndoe@example.com'
	assert user.preferences == 'likes outdoor events'


def test_user_profile_update():
	user = User('1', 'John Doe', 'johndoe@example.com', 'likes outdoor events')
	user.update_profile(name='Jane Doe', contact_info='janedoe@example.com', preferences='likes indoor events')
	assert user.name == 'Jane Doe'
	assert user.contact_info == 'janedoe@example.com'
	assert user.preferences == 'likes indoor events'


def test_user_profile_view():
	user = User('1', 'John Doe', 'johndoe@example.com', 'likes outdoor events')
	profile = user.view_profile()
	assert profile['user_id'] == '1'
	assert profile['name'] == 'John Doe'
	assert profile['contact_info'] == 'johndoe@example.com'
	assert profile['preferences'] == 'likes outdoor events'


def test_user_event_save_and_access():
	user = User('1', 'John Doe', 'johndoe@example.com', 'likes outdoor events')
	user.save_event('event1', is_upcoming=True)
	user.save_event('event2', is_upcoming=False)
	assert user.get_upcoming_events() == ['event1']
	assert user.get_past_events() == ['event2']


def test_user_storage():
	db = Database()
	user = User('1', 'John Doe', 'johndoe@example.com', 'likes outdoor events')
	db.add_user('1', user)
	retrieved_user = db.get_user('1')
	assert retrieved_user.user_id == '1'
	assert retrieved_user.name == 'John Doe'
	assert retrieved_user.contact_info == 'johndoe@example.com'
	assert retrieved_user.preferences == 'likes outdoor events'
