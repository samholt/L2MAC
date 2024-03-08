import pytest
from status import Status
from database import Database


def test_post():
	status = Status('user1', 'Hello, world!', 'public')
	status.post()
	assert status in Database.statuses
