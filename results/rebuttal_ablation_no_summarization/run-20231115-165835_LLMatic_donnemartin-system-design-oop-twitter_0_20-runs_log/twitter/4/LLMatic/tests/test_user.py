import pytest
from user import User
from post import Post
import time


def test_user_registration():
	user = User('test@example.com', 'testuser', 'password')
	user.register()
	assert user.email == 'test@example.com'
	assert user.username == 'testuser'
	assert user.password == 'password'


def test_user_authentication():
	user = User('test@example.com', 'testuser', 'password')
	assert user.authenticate('password') is not None
	assert user.authenticate('wrongpassword') == 'Invalid password'


def test_reset_password():
	user = User('test@example.com', 'testuser', 'password')
	user.reset_password('newpassword')
	assert user.password == 'newpassword'


def test_edit_profile():
	user = User('test@example.com', 'testuser', 'password')
	user.edit_profile(profile_picture='newpic.jpg', bio='new bio', website_link='newwebsite.com', location='new location')
	assert user.profile_picture == 'newpic.jpg'
	assert user.bio == 'new bio'
	assert user.website_link == 'newwebsite.com'
	assert user.location == 'new location'


def test_toggle_privacy():
	user = User('test@example.com', 'testuser', 'password')
	user.toggle_privacy()
	assert user.is_private == True
	user.toggle_privacy()
	assert user.is_private == False


def test_follow_unfollow():
	user1 = User('test1@example.com', 'testuser1', 'password')
	user2 = User('test2@example.com', 'testuser2', 'password')
	user1.follow(user2)
	assert user2 in user1.following
	assert user1 in user2.followers
	assert f'{user1.username} started following you.' in user2.notifications
	user1.unfollow(user2)
	assert user2 not in user1.following
	assert user1 not in user2.followers


def test_view_timeline():
	user1 = User('test1@example.com', 'testuser1', 'password')
	user2 = User('test2@example.com', 'testuser2', 'password')
	user3 = User('test3@example.com', 'testuser3', 'password')
	user1.follow(user2)
	user1.follow(user3)
	user2.posts = [Post('post1', [], user2), Post('post2', [], user2)]
	time.sleep(1)
	user3.posts = [Post('post3', [], user3), Post('post4', [], user3)]
	assert sorted(user1.view_timeline(), key=lambda post: post.timestamp, reverse=True) == sorted([user3.posts[1], user3.posts[0], user2.posts[1], user2.posts[0]], key=lambda post: post.timestamp, reverse=True)


def test_view_notifications():
	user1 = User('test1@example.com', 'testuser1', 'password')
	user2 = User('test2@example.com', 'testuser2', 'password')
	user1.follow(user2)
	assert user2.view_notifications() == [f'{user1.username} started following you.']

