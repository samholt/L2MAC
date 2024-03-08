import pytest
from datetime import timedelta
from status import Status
from user import User


def test_status():
	user = User('test@test.com', 'password')
	status = Status(user, 'Hello, world!', 'public', 24)
	db = {}
	status.post(db)
	assert status.view(db) == status
	status.expiry = status.expiry - timedelta(hours=25)
	assert status.view(db) == None
