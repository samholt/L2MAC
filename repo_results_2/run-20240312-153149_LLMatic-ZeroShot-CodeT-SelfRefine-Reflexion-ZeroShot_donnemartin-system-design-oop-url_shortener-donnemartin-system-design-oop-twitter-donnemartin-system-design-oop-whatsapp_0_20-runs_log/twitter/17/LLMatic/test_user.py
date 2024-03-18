import pytest
from user import User
from post import Post


def test_user_registration():
	user = User('test@example.com', 'testuser', 'password', False)
	user.register()


def test_user_authentication():
	user = User('test@example.com', 'testuser', 'password', False)
	assert user.authenticate('password')


def test_user_password_reset():
	user = User('test@example.com', 'testuser', 'password', False)
	user.reset_password('newpassword')
	assert user.authenticate('newpassword')


def test_user_edit_profile():
	user = User('test@example.com', 'testuser', 'password', False)
	user.edit_profile(profile_picture='newpic.jpg', bio='New bio', website_link='www.newwebsite.com', location='New location')
	assert user.profile_picture == 'newpic.jpg'
	assert user.bio == 'New bio'
	assert user.website_link == 'www.newwebsite.com'
	assert user.location == 'New location'


def test_user_toggle_privacy():
	user = User('test@example.com', 'testuser', 'password', False)
	user.toggle_privacy()
	assert user.is_private


def test_user_follow_unfollow():
	user1 = User('test1@example.com', 'testuser1', 'password', False)
	user2 = User('test2@example.com', 'testuser2', 'password', False)
	user1.follow(user2)
	assert user2 in user1.following
	user1.unfollow(user2)
	assert user2 not in user1.following


def test_user_get_timeline():
	user1 = User('test1@example.com', 'testuser1', 'password', False)
	user2 = User('test2@example.com', 'testuser2', 'password', False)
	user3 = User('test3@example.com', 'testuser3', 'password', False)
	post1 = Post(user2, 'Hello world')
	post2 = Post(user3, 'Hello again')
	user2.posts.append(post1)
	user3.posts.append(post2)
	user1.follow(user2)
	user1.follow(user3)
	assert len(user1.get_timeline()) == len(user2.posts) + len(user3.posts)


def test_user_notify_new_follower():
	user1 = User('test1@example.com', 'testuser1', 'password', False)
	user2 = User('test2@example.com', 'testuser2', 'password', False)
	user1.follow(user2)
	assert user2 in user1.following
	assert f'User {user1.username} started following you.' in user2.notifications


def test_user_notify():
	user = User('test@example.com', 'testuser', 'password', False)
	user.notify('Test notification')
	assert 'Test notification' in user.notifications

