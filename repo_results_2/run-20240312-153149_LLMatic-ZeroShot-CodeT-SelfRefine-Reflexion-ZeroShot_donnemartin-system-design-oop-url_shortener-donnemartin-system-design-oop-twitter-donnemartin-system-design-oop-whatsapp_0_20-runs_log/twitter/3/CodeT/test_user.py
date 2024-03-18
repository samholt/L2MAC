import pytest
from user import User

@pytest.fixture
def user():
	return User('test@test.com', 'test', 'password')

def test_check_password(user):
	assert user.check_password('password')
	assert not user.check_password('wrong_password')

def test_update(user):
	user.update(bio='New bio', website='newwebsite.com')
	assert user.bio == 'New bio'
	assert user.website == 'newwebsite.com'

def test_to_dict(user):
	user_dict = user.to_dict()
	assert 'password' not in user_dict
	assert user_dict['email'] == 'test@test.com'
	assert user_dict['username'] == 'test'
