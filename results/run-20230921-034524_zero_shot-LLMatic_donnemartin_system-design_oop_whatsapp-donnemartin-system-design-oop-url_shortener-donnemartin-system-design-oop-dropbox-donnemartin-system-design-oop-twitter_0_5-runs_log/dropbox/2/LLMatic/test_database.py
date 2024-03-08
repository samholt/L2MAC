import pytest
from database import Database


def test_database():
	# Initialize database
	db = Database(':memory:')

	# Start transaction
	db.start_transaction()

	# Execute query
	db.execute_query('CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)')
	db.execute_query('INSERT INTO test (name) VALUES (?)', ('test',))

	# Commit transaction
	db.commit_transaction()

	# Check data
	data = db.execute_query('SELECT * FROM test')
	assert data == [(1, 'test')]

	# Close database
	db.close()
