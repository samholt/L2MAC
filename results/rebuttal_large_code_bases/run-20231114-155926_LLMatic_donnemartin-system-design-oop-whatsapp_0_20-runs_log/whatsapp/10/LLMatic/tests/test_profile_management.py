import pytest
from app.models import User

def test_profile_management():
	user = User.create(id=1, email='test@example.com', password='test', profile_picture='test.jpg', status_message='Hello, world!', privacy_settings='Public', last_seen='2022-01-01 00:00:00', contacts=[], blocked_contacts=[])
	assert user.email == 'test@example.com'
	assert user.profile_picture == 'test.jpg'
	assert user.status_message == 'Hello, world!'
	assert user.privacy_settings == 'Public'
	assert user.last_seen == '2022-01-01 00:00:00'
	assert user.contacts == []
	assert user.blocked_contacts == []
