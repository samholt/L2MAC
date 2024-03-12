import pytest
from user import User
from post import Post


def test_user_registration():
	users_db = {}
	user = User('test@test.com', 'testuser', 'testpassword', False)
	assert user.register(users_db) == 'User registered successfully'
	assert user.register(users_db) == 'User already exists'


def test_user_authentication():
	users_db = {}
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.register(users_db)
	assert 'Authentication failed' == user.authenticate('wrongpassword', users_db)
	assert isinstance(user.authenticate('testpassword', users_db), str)


def test_user_password_reset():
	users_db = {}
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.register(users_db)
	assert 'Password reset successful' == user.reset_password('newpassword', users_db)
	assert 'Authentication failed' == user.authenticate('testpassword', users_db)
	assert isinstance(user.authenticate('newpassword', users_db), str)


def test_user_profile_management():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	assert 'Profile picture updated successfully' == user.update_profile_picture('new_picture.jpg')
	assert 'Bio updated successfully' == user.update_bio('This is a test bio')
	assert 'Website link updated successfully' == user.update_website_link('https://test.com')
	assert 'Location updated successfully' == user.update_location('Test City, Test Country')
	assert 'Privacy setting updated successfully' == user.toggle_privacy()
	assert user.is_private == True


def test_user_follow_unfollow():
	user1 = User('test1@test.com', 'testuser1', 'testpassword', False)
	user2 = User('test2@test.com', 'testuser2', 'testpassword', False)
	assert 'Followed successfully' == user1.follow(user2.username)
	assert user2.username in user1.following
	assert 'Already following' == user1.follow(user2.username)
	assert 'Unfollowed successfully' == user1.unfollow(user2.username)
	assert user2.username not in user1.following
	assert 'Not following' == user1.unfollow(user2.username)


def test_user_view_timeline():
	users_db = {}
	user1 = User('test1@test.com', 'testuser1', 'testpassword', False)
	user2 = User('test2@test.com', 'testuser2', 'testpassword', False)
	user1.register(users_db)
	user2.register(users_db)
	user1.follow(user2.username)
	posts_db = {}
	post1 = Post(user2.username, 'Hello world!')
	assert 'Post published successfully' == post1.publish(posts_db)
	assert post1 in user1.view_timeline(posts_db)


def test_user_receive_notification():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	assert 'Notification received successfully' == user.receive_notification('Test notification')
	assert 'Test notification' in user.notifications


def test_user_recommend_users():
	users_db = {}
	user1 = User('test1@test.com', 'testuser1', 'testpassword', False)
	user2 = User('test2@test.com', 'testuser2', 'testpassword', False)
	user3 = User('test3@test.com', 'testuser3', 'testpassword', False)
	user1.register(users_db)
	user2.register(users_db)
	user3.register(users_db)
	user1.follow(user2.username)
	user2.follow(user3.username)
	user3.follow(user1.username)
	assert user3.username in user1.recommend_users(users_db)
	assert user1.username in user2.recommend_users(users_db)

