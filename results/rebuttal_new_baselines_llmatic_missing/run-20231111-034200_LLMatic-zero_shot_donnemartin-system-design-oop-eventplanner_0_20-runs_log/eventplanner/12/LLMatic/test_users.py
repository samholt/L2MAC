import pytest
from users import User, create_user, get_user

def test_user_creation():
	user = create_user('John Doe')
	assert user.name == 'John Doe'
	assert get_user('John Doe') == user

def test_profile_customization():
	user = create_user('Jane Doe', {'likes': 'music'})
	user.customize_profile({'dislikes': 'noise'})
	assert user.preferences == {'likes': 'music', 'dislikes': 'noise'}

def test_event_saving_and_accessing():
	user = create_user('John Doe')
	user.save_event('Wedding')
	assert user.get_events() == ['Wedding']
