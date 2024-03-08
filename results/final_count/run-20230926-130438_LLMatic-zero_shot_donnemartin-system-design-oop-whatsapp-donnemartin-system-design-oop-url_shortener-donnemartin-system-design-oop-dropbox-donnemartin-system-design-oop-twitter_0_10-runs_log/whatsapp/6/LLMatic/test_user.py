import pytest
from user import User

def test_set_online_status():
	user = User()
	user.set_online_status('user1', 'online')
	assert user.get_online_status('user1') == 'online'

	user.set_online_status('user1', 'offline')
	assert user.get_online_status('user1') == 'offline'

	assert user.get_online_status('user2') == 'offline'

