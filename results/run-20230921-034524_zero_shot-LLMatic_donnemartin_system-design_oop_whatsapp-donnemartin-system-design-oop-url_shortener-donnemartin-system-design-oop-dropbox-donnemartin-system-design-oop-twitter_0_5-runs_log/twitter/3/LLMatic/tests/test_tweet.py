import pytest
from models.user import User
from models.tweet import Tweet


def test_set_privacy():
	user = User('test_user', 'password')
	tweet = Tweet('Hello, world!', user)
	tweet.set_privacy('private')
	assert tweet.privacy == 'private'
	with pytest.raises(ValueError):
		tweet.set_privacy('invalid')

