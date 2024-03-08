import pytest
from database import Database

def test_database():
	db = Database()

	# Test insert and get
	db.insert(db.users, '1', {'name': 'John'})
	assert db.get(db.users, '1') == {'name': 'John'}

	# Test delete
	db.delete(db.users, '1')
	assert db.get(db.users, '1') == None
