import pytest
from database import MockDatabase

def test_mock_database():
	db = MockDatabase()

	# Test add
	assert db.add('users', '1', {'name': 'John'}) == 'Data added successfully'
	assert db.add('invalid_table', '1', {'name': 'John'}) == 'Invalid table'

	# Test get
	assert db.get('users', '1') == {'name': 'John'}
	assert db.get('users', '2') == 'Invalid table or id'

	# Test update
	assert db.update('users', '1', {'name': 'John Doe'}) == 'Data updated successfully'
	assert db.get('users', '1') == {'name': 'John Doe'}
	assert db.update('users', '2', {'name': 'John Doe'}) == 'Invalid table or id'

	# Test delete
	assert db.delete('users', '1') == 'Data deleted successfully'
	assert db.get('users', '1') == 'Invalid table or id'
