import pytest
from status import Status


def test_post_status():
	status = Status('user1')
	status.post_status('Hello, world!')
	assert status.view_status() == {
		'user_id': 'user1',
		'status_content': 'Hello, world!',
		'created_at': status.created_at
	}


def test_view_status():
	status = Status('user1', 'Hello, world!')
	assert status.view_status() == {
		'user_id': 'user1',
		'status_content': 'Hello, world!',
		'created_at': status.created_at
	}
