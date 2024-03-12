import pytest
from user import User


def test_user_registration():
	db = {}
	user = User('test@test.com', 'testuser', 'testpassword', False)
	assert user.register(db) == 'User registered successfully'
	assert user.register(db) == 'User already exists'


def test_user_authentication():
	db = {}
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.register(db)
	assert isinstance(user.authenticate('testpassword', db), str)
	assert user.authenticate('wrongpassword', db) == 'Invalid credentials'


def test_user_password_reset():
	db = {}
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.register(db)
	assert user.reset_password('newpassword', db) == 'Password reset successful'
	assert user.authenticate('newpassword', db) != 'Invalid credentials'


def test_user_profile_management():
	db = {}
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.register(db)
	assert user.update_profile_picture('new_picture.jpg') == 'Profile picture updated successfully'
	assert user.update_bio('This is a test bio') == 'Bio updated successfully'
	assert user.update_website_link('https://test.com') == 'Website link updated successfully'
	assert user.update_location('Test City, Test Country') == 'Location updated successfully'
	assert user.toggle_privacy() == 'Privacy setting updated successfully'


def test_user_following_and_followers():
	db = {}
	user1 = User('test1@test.com', 'testuser1', 'testpassword', False)
	user2 = User('test2@test.com', 'testuser2', 'testpassword', False)
	user1.register(db)
	user2.register(db)
	assert user1.follow(user2) == 'Followed successfully'
	assert user1.unfollow(user2) == 'Unfollowed successfully'
	assert user1.follow(user2) == 'Followed successfully'
	assert user1.unfollow(user2) == 'Unfollowed successfully'


def test_user_receive_notification():
	db = {}
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.register(db)
	assert user.receive_notification('Test notification') == 'Notification received'
	assert len(user.notifications) == 1
	assert user.notifications[0] == 'Test notification'


def test_user_recommendations():
	db = {}
	user1 = User('test1@test.com', 'testuser1', 'testpassword', False)
	user2 = User('test2@test.com', 'testuser2', 'testpassword', False)
	user3 = User('test3@test.com', 'testuser3', 'testpassword', False)
	user1.register(db)
	user2.register(db)
	user3.register(db)
	user1.follow(user2)
	user3.follow(user2)
	recommended_users = user1.recommend_users(db)
	assert len(recommended_users) == 1
	assert user3 in recommended_users
