import pytest
from mock_db import MockDB


def test_mock_db():
	db = MockDB()
	db.add('key', 'value')
	assert db.retrieve('key') == 'value'
	db.update('key', 'new value')
	assert db.retrieve('key') == 'new value'
	db.delete('key')
	assert db.retrieve('key') is None
