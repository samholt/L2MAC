import pytest
import mock_db

def test_mock_db():
	db = mock_db.MockDB()

	# Test add
	db.add('key', 'value')
	assert db.retrieve('key') == 'value'

	# Test update
	db.update('key', 'new value')
	assert db.retrieve('key') == 'new value'

	# Test delete
	db.delete('key')
	assert db.retrieve('key') is None
