import pytest
from user import User

def test_user_registration():
	user = User('test@test.com', 'testuser', 'testpassword')
	assert user.register() == {
		'email': 'test@test.com',
		'username': 'testuser',
		'password': user.password,
		'profile_picture': None,
		'bio': None,
		'website_link': None,
		'location': None
	}
