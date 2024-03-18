import app

def test_database():
	# Test users table
	app.DATABASE['users'][1] = {'name': 'John', 'email': 'john@example.com'}
	assert app.DATABASE['users'][1] == {'name': 'John', 'email': 'john@example.com'}

	# Test messages table
	app.DATABASE['messages'][1] = {'user_id': 1, 'message': 'Hello, World!'}
	assert app.DATABASE['messages'][1] == {'user_id': 1, 'message': 'Hello, World!'}

	# Test groups table
	app.DATABASE['groups'][1] = {'name': 'Group 1', 'members': [1]}
	assert app.DATABASE['groups'][1] == {'name': 'Group 1', 'members': [1]}

	# Test statuses table
	app.DATABASE['statuses'][1] = {'user_id': 1, 'status': 'Online'}
	assert app.DATABASE['statuses'][1] == {'user_id': 1, 'status': 'Online'}
