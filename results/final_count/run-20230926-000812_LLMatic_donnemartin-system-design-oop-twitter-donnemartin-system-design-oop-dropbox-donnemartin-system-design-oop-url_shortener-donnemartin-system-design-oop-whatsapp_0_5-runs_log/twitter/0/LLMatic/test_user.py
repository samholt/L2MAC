import pytest
from user import User


def test_user_creation():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	assert user.email == 'test@test.com'
	assert user.username == 'testuser'
	assert user.is_private == False


def test_user_authentication():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	assert user.authenticate('testpassword') == True
	assert user.authenticate('wrongpassword') == False


def test_password_reset():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.reset_password('newpassword')
	assert user.authenticate('newpassword') == True


def test_auth_token():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	token = user.generate_auth_token()
	assert token is not None


def test_profile_management():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.edit_profile('newpic.jpg', 'This is a bio', 'www.test.com', 'Test City')
	assert user.profile_picture == 'newpic.jpg'
	assert user.bio == 'This is a bio'
	assert user.website_link == 'www.test.com'
	assert user.location == 'Test City'


def test_privacy_toggle():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.toggle_privacy()
	assert user.is_private == True
	user.toggle_privacy()
	assert user.is_private == False


def test_follow_unfollow():
	user1 = User('test1@test.com', 'testuser1', 'testpassword', False)
	user2 = User('test2@test.com', 'testuser2', 'testpassword', False)
	user1.follow(user2)
	assert user2 in user1.following
	assert user1 in user2.followers
	user1.unfollow(user2)
	assert user2 not in user1.following
	assert user1 not in user2.followers


def test_timeline():
	user1 = User('test1@test.com', 'testuser1', 'testpassword', False)
	user2 = User('test2@test.com', 'testuser2', 'testpassword', False)
	user1.follow(user2)
	user2.update_timeline('Hello world!')
	assert 'Hello world!' in user1.view_timeline()


def test_notifications():
	user1 = User('test1@test.com', 'testuser1', 'testpassword', False)
	user2 = User('test2@test.com', 'testuser2', 'testpassword', False)
	user1.follow(user2)
	assert f'testuser1 started following you.' in user2.notifications
	user2.notify_like('Hello world!')
	assert 'Your post Hello world! got a new like.' in user2.notifications
	user2.notify_retweet('Hello world!')
	assert 'Your post Hello world! was retweeted.' in user2.notifications
	user2.notify_reply('Hello world!')
	assert 'Your post Hello world! got a new reply.' in user2.notifications
	user2.notify_mention('Hello world!')
	assert 'You were mentioned in a post Hello world!.' in user2.notifications


def test_user_recommendations():
	user1 = User('test1@test.com', 'testuser1', 'testpassword', False)
	user2 = User('test2@test.com', 'testuser2', 'testpassword', False)
	user3 = User('test3@test.com', 'testuser3', 'testpassword', False)
	user4 = User('test4@test.com', 'testuser4', 'testpassword', False)
	user1.follow(user2)
	user2.follow(user3)
	user3.follow(user1)
	user4.update_timeline('Hello world!')
	recommendations = user1.recommend_users([user3, user4])
	assert user4 in recommendations

