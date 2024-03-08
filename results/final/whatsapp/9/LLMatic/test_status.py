import pytest
from status import Status
from user import User

def test_post_status():
	user = User('test_email', 'test_password')
	status = Status(user, 'test_image', 'public', '24h')
	status.post_status()
	assert status.status_db[user.email]['image'] == 'test_image'
	assert status.status_db[user.email]['visibility'] == 'public'
	assert status.status_db[user.email]['expiry_time'] == '24h'
