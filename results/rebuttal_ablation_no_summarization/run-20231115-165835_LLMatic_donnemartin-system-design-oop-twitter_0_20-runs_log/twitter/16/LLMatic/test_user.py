import pytest
from user import User
from post import Post
import time


def test_register():
	db = {}
	user = User('test@test.com', 'testuser', 'testpassword', False)
	assert user.register(db) == True
	assert user.register(db) == False


def test_authenticate():
	db = {}
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.register(db)
	assert user.authenticate(db, 'testpassword') == True
	assert user.authenticate(db, 'wrongpassword') == False


def test_reset_password():
	db = {}
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.register(db)
	assert user.reset_password(db, 'newpassword') == True
	assert user.authenticate(db, 'newpassword') == True


def test_edit_profile():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.edit_profile(profile_picture='new_pic.jpg', bio='new bio', website_link='new_website.com', location='new location')
	assert user.profile_picture == 'new_pic.jpg'
	assert user.bio == 'new bio'
	assert user.website_link == 'new_website.com'
	assert user.location == 'new location'


def test_toggle_privacy():
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
	assert user2.notifications == [f'{user1.username} started following you.']
	user1.unfollow(user2)
	assert user2 not in user1.following
	assert user1 not in user2.followers


def test_view_timeline():
	user1 = User('test1@test.com', 'testuser1', 'testpassword', False)
	user2 = User('test2@test.com', 'testuser2', 'testpassword', False)
	user3 = User('test3@test.com', 'testuser3', 'testpassword', False)
	user1.follow(user2)
	user1.follow(user3)
	post1 = Post()
	post2 = Post()
	post3 = Post()
	post4 = Post()
	user2.posts = [post1.create(user2.username, 'post1', None), post2.create(user2.username, 'post2', None)]
	time.sleep(1)
	user3.posts = [post3.create(user3.username, 'post3', None), post4.create(user3.username, 'post4', None)]
	assert sorted(user1.view_timeline(), key=lambda post: post['timestamp'], reverse=True) == sorted([post4.database[list(post4.database.keys())[0]], post3.database[list(post3.database.keys())[0]], post2.database[list(post2.database.keys())[0]], post1.database[list(post1.database.keys())[0]]], key=lambda post: post['timestamp'], reverse=True)

