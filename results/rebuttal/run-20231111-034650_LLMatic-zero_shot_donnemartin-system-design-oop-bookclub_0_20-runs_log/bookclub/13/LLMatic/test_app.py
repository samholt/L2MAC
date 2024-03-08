import app

def test_database():
	# Test that the database can store and retrieve data
	app.DATABASE['users']['test_user'] = 'test_data'
	assert app.DATABASE['users']['test_user'] == 'test_data'

def test_user_registration():
	# Test user registration
	user = app.User('test_user', 'test_password')
	user.create()
	assert app.DATABASE['users']['test_user'] == 'test_password'

def test_user_login():
	# Test user login
	user = app.User('test_user', 'test_password')
	assert user.authenticate('test_password') == True
	assert user.authenticate('wrong_password') == False

def test_book_club_creation():
	# Test book club creation
	club = app.BookClub('test_club', True)
	club.create()
	assert app.DATABASE['book_clubs']['test_club'] == {'is_private': True, 'members': []}

def test_set_privacy():
	# Test setting book club privacy
	club = app.BookClub('test_club')
	club.set_privacy(False)
	assert app.DATABASE['book_clubs']['test_club']['is_private'] == False

def test_manage_member():
	# Test managing book club members
	club = app.BookClub('test_club')
	club.manage_member('test_user', 'add')
	assert 'test_user' in app.DATABASE['book_clubs']['test_club']['members']
	club.manage_member('test_user', 'remove')
	assert 'test_user' not in app.DATABASE['book_clubs']['test_club']['members']

def test_schedule_meeting():
	# Test scheduling a meeting
	meeting = app.Meeting('test_meeting', 'test_club', '2022-12-31 12:00:00')
	meeting.schedule()
	assert app.DATABASE['meetings']['test_meeting'] == {'club_name': 'test_club', 'date_time': '2022-12-31 12:00:00'}

def test_create_discussion():
	# Test creating a discussion
	discussion = app.Discussion('test_discussion', 'test_club')
	discussion.create()
	assert app.DATABASE['discussions']['test_discussion'] == {'club_name': 'test_club', 'comments': []}

def test_post_comment():
	# Test posting a comment
	discussion = app.Discussion('test_discussion', 'test_club')
	discussion.post_comment('test_user', 'test_comment')
	assert {'username': 'test_user', 'comment': 'test_comment'} in app.DATABASE['discussions']['test_discussion']['comments']

def test_suggest_book():
	# Test suggesting a book
	book = app.Book('test_book', 'test_club')
	book.suggest()
	assert app.DATABASE['book_selections']['test_book'] == {'club_name': 'test_club', 'votes': 0}

def test_vote_book():
	# Test voting for a book
	book = app.Book('test_book', 'test_club')
	book.vote()
	assert app.DATABASE['book_selections']['test_book']['votes'] == 1

