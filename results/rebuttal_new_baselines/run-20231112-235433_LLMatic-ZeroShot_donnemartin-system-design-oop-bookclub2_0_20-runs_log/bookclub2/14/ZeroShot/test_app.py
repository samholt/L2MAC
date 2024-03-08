import pytest
import app

# Test data
user = app.User(id='1', name='Test User')
club = app.Club(id='1', name='Test Club', privacy='public')
meeting = app.Meeting(id='1', club_id='1', schedule='2022-12-31 12:00:00')
forum = app.Forum(id='1', club_id='1')
comment = app.Comment(id='1', user_id='1', forum_id='1', content='Test comment')
vote = app.Vote(id='1', user_id='1', book='Test Book')
profile = app.Profile(id='1', user_id='1', bio='Test bio')
follow = app.Follow(id='1', follower_id='1', followee_id='2')
reading_list = app.ReadingList(id='1', user_id='1', books=['Test Book'])
recommendation = app.Recommendation(id='1', user_id='1', book='Test Book')
admin = app.Admin(id='1', user_id='1')
moderation = app.Moderation(id='1', admin_id='1', content_id='1', action='delete')
analytics = app.Analytics(id='1', metric='users', value=1)

def test_user():
	assert user.id == '1'
	assert user.name == 'Test User'

def test_club():
	assert club.id == '1'
	assert club.name == 'Test Club'
	assert club.privacy == 'public'

def test_meeting():
	assert meeting.id == '1'
	assert meeting.club_id == '1'
	assert meeting.schedule == '2022-12-31 12:00:00'

def test_forum():
	assert forum.id == '1'
	assert forum.club_id == '1'

def test_comment():
	assert comment.id == '1'
	assert comment.user_id == '1'
	assert comment.forum_id == '1'
	assert comment.content == 'Test comment'

def test_vote():
	assert vote.id == '1'
	assert vote.user_id == '1'
	assert vote.book == 'Test Book'

def test_profile():
	assert profile.id == '1'
	assert profile.user_id == '1'
	assert profile.bio == 'Test bio'

def test_follow():
	assert follow.id == '1'
	assert follow.follower_id == '1'
	assert follow.followee_id == '2'

def test_reading_list():
	assert reading_list.id == '1'
	assert reading_list.user_id == '1'
	assert reading_list.books == ['Test Book']

def test_recommendation():
	assert recommendation.id == '1'
	assert recommendation.user_id == '1'
	assert recommendation.book == 'Test Book'

def test_admin():
	assert admin.id == '1'
	assert admin.user_id == '1'

def test_moderation():
	assert moderation.id == '1'
	assert moderation.admin_id == '1'
	assert moderation.content_id == '1'
	assert moderation.action == 'delete'

def test_analytics():
	assert analytics.id == '1'
	assert analytics.metric == 'users'
	assert analytics.value == 1
