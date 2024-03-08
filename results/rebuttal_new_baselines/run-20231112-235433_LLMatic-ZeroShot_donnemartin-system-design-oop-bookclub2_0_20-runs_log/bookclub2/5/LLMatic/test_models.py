import models

def test_user():
	user = models.User(1, 'Test User', 'testuser@example.com', 'password123')
	assert user.id == 1
	assert user.username == 'Test User'
	assert user.email == 'testuser@example.com'
	assert user.password == 'password123'

def test_profile():
	profile = models.Profile(1, 1, 'This is a test bio.', 'Test City, Test Country')
	assert profile.id == 1
	assert profile.user_id == 1
	assert profile.bio == 'This is a test bio.'
	assert profile.location == 'Test City, Test Country'

def test_book_club():
	book_club = models.BookClub(1, 'Test Book Club', 'This is a test book club.', 'Public')
	assert book_club.id == 1
	assert book_club.name == 'Test Book Club'
	assert book_club.description == 'This is a test book club.'
	assert book_club.privacy_settings == 'Public'

def test_meeting():
	meeting = models.Meeting(1, 1, '2022-12-31', '12:00', 'Test Location')
	assert meeting.id == 1
	assert meeting.bookclub_id == 1
	assert meeting.date == '2022-12-31'
	assert meeting.time == '12:00'
	assert meeting.location == 'Test Location'

def test_discussion():
	discussion = models.Discussion(1, 1, 'Test Discussion', 'This is a test discussion.')
	assert discussion.id == 1
	assert discussion.bookclub_id == 1
	assert discussion.title == 'Test Discussion'
	assert discussion.content == 'This is a test discussion.'

def test_comment():
	comment = models.Comment(1, 1, 1, 'This is a test comment.')
	assert comment.id == 1
	assert comment.discussion_id == 1
	assert comment.user_id == 1
	assert comment.content == 'This is a test comment.'

def test_vote():
	vote = models.Vote(1, 1, 1)
	assert vote.id == 1
	assert vote.book_id == 1
	assert vote.user_id == 1

def test_follow():
	follow = models.Follow(1, 1, 2)
	assert follow.id == 1
	assert follow.follower_id == 1
	assert follow.followee_id == 2

def test_reading_list():
	reading_list = models.ReadingList(1, 1, 1)
	assert reading_list.id == 1
	assert reading_list.user_id == 1
	assert reading_list.book_id == 1

def test_recommendation():
	recommendation = models.Recommendation(1, 1, 1)
	assert recommendation.id == 1
	assert recommendation.user_id == 1
	assert recommendation.book_id == 1

def test_dashboard():
	dashboard = models.Dashboard(1, 1, 'This is a test dashboard.')
	assert dashboard.id == 1
	assert dashboard.admin_id == 1
	assert dashboard.content == 'This is a test dashboard.'

def test_moderation():
	moderation = models.Moderation(1, 1, 'Test Action')
	assert moderation.id == 1
	assert moderation.admin_id == 1
	assert moderation.action == 'Test Action'

def test_analytics():
	analytics = models.Analytics(1, 100, ['Book1', 'Book2', 'Book3'])
	assert analytics.id == 1
	assert analytics.user_engagement == 100
	assert analytics.popular_books == ['Book1', 'Book2', 'Book3']
