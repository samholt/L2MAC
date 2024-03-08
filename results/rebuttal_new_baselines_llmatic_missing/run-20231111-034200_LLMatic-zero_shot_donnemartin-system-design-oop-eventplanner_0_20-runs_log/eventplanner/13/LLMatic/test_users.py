import pytest
from users import User

def test_user():
	user_manager = User()
	user_manager.create_user('1', 'John Doe', 'john@example.com')
	assert user_manager.get_user('1') == {'name': 'John Doe', 'email': 'john@example.com', 'events': []}
	user_manager.update_user('1', name='Jane Doe')
	assert user_manager.get_user('1')['name'] == 'Jane Doe'
	user_manager.save_event('1', 'event1')
	assert 'event1' in user_manager.get_user('1')['events']
