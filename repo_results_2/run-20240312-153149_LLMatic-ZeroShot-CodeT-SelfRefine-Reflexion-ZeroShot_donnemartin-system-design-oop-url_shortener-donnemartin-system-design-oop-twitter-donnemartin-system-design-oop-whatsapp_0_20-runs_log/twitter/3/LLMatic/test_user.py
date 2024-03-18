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
	assert isinstance(user.authenticate('testpassword', users_db), str)
	assert user.authenticate('wrongpassword', users_db) == 'Invalid credentials'


def test_user_password_reset():
	users_db = {}
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.register(users_db)
	assert user.reset_password('newpassword', users_db) == 'Password reset successful'
	assert isinstance(user.authenticate('newpassword', users_db), str)


def test_user_profile_edit():
	users_db = {}
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.register(users_db)
	assert user.edit_profile(profile_picture='newpic.jpg', bio='new bio', website_link='newwebsite.com', location='new location') == 'Profile updated successfully'
	assert user.profile_picture == 'newpic.jpg'
	assert user.bio == 'new bio'
	assert user.website_link == 'newwebsite.com'
	assert user.location == 'new location'


def test_user_privacy_toggle():
	users_db = {}
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.register(users_db)
	assert user.toggle_privacy() == 'Privacy setting updated'
	assert user.is_private == True


def test_user_follow_unfollow():
	users_db = {}
	user1 = User('test1@test.com', 'testuser1', 'testpassword', False)
	user2 = User('test2@test.com', 'testuser2', 'testpassword', False)
	user1.register(users_db)
	user2.register(users_db)
	assert user1.follow_user(user2) == 'Followed user successfully'
	assert user1.unfollow_user(user2) == 'Unfollowed user successfully'


def test_user_notifications():
	users_db = {}
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.register(users_db)
	assert user.notify('You have a new follower') == 'Notification added successfully'
	assert 'You have a new follower' in user.notifications


def test_user_recommendations():
	users_db = {}
	user1 = User('test1@test.com', 'testuser1', 'testpassword', False)
	user2 = User('test2@test.com', 'testuser2', 'testpassword', False)
	user3 = User('test3@test.com', 'testuser3', 'testpassword', False)
	user1.register(users_db)
	user2.register(users_db)
	user3.register(users_db)
	user1.follow_user(user2)
	user3.follow_user(user2)
	user2.follow_user(user1)
	user2.follow_user(user3)
	recommended_users = user1.recommend_users(users_db)
	assert len(recommended_users) > 0
	assert user3 in recommended_users

