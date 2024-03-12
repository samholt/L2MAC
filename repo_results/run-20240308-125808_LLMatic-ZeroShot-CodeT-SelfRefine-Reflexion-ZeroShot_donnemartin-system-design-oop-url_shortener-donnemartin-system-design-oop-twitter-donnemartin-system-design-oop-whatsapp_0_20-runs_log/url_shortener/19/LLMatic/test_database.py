from database import Database

def test_database_operations():
	# Initialize the database
	db = Database()

	# Test insert operation
	db.insert('users', 'user1', {'name': 'John', 'email': 'john@example.com'})
	assert db.get('users', 'user1') == {'name': 'John', 'email': 'john@example.com'}

	# Test update operation
	db.update('users', 'user1', {'name': 'John Doe', 'email': 'johndoe@example.com'})
	assert db.get('users', 'user1') == {'name': 'John Doe', 'email': 'johndoe@example.com'}

	# Test delete operation
	db.delete('users', 'user1')
	assert db.get('users', 'user1') is None
