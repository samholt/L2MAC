import app

def test_database():
	# Test users
	app.DATABASE['users']['user1'] = 'User 1'
	assert app.DATABASE['users']['user1'] == 'User 1'

	# Test book_clubs
	app.DATABASE['book_clubs']['club1'] = 'Club 1'
	assert app.DATABASE['book_clubs']['club1'] == 'Club 1'

	# Test meetings
	app.DATABASE['meetings']['meeting1'] = 'Meeting 1'
	assert app.DATABASE['meetings']['meeting1'] == 'Meeting 1'

	# Test discussions
	app.DATABASE['discussions']['discussion1'] = 'Discussion 1'
	assert app.DATABASE['discussions']['discussion1'] == 'Discussion 1'

	# Test books
	app.DATABASE['books']['book1'] = 'Book 1'
	assert app.DATABASE['books']['book1'] == 'Book 1'
