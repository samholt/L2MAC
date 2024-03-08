import pytest
from mock_db import MockDB


def test_mock_db():
	mock_db = MockDB()

	# Test add
	mock_db.add(mock_db.users, 'user1', 'User 1')
	assert mock_db.get(mock_db.users, 'user1') == 'User 1'

	# Test update
	mock_db.update(mock_db.users, 'user1', 'Updated User 1')
	assert mock_db.get(mock_db.users, 'user1') == 'Updated User 1'

	# Test delete
	mock_db.delete(mock_db.users, 'user1')
	assert mock_db.get(mock_db.users, 'user1') is None
