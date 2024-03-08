import pytest
from datetime import datetime, timedelta
from status import Status
from user import User


def test_status():
	user = User('test@test.com', 'password')
	status = Status(user, 'image.jpg')
	status.post()
	assert status.view() == {'image': 'image.jpg', 'visibility': 'public', 'expiry_time': status.expiry_time}
	status.set_visibility('private')
	assert status.view() == {'image': 'image.jpg', 'visibility': 'private', 'expiry_time': status.expiry_time}

