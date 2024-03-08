import app

def test_database():
	# Test that the database is set up correctly
	assert 'users' in app.DATABASE
	assert 'book_clubs' in app.DATABASE
	assert 'meetings' in app.DATABASE
	assert 'discussions' in app.DATABASE
	assert 'books' in app.DATABASE
	assert 'notifications' in app.DATABASE

	# Test that data can be added, retrieved, updated, and deleted correctly
	app.DATABASE['users']['test_user'] = {'name': 'Test User'}
	assert 'test_user' in app.DATABASE['users']
	assert app.DATABASE['users']['test_user']['name'] == 'Test User'
	app.DATABASE['users']['test_user']['name'] = 'Updated Test User'
	assert app.DATABASE['users']['test_user']['name'] == 'Updated Test User'
	del app.DATABASE['users']['test_user']
	assert 'test_user' not in app.DATABASE['users']
