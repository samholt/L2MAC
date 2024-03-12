import pytest
from user import User, UserDatabase
from post import Post
from datetime import datetime


def test_user_registration():
	user_db = UserDatabase()
	assert user_db.register('1', 'test@email.com', 'testuser', 'password', False) == True
	assert user_db.register('2', 'test@email.com', 'testuser', 'password', False) == False


def test_user_authentication():
	user_db = UserDatabase()
	user_db.register('1', 'test@email.com', 'testuser', 'password', False)
	assert user_db.authenticate('testuser', 'password') == True
	assert user_db.authenticate('testuser', 'wrongpassword') == False
	assert user_db.authenticate('wronguser', 'password') == False


def test_password_reset():
	user_db = UserDatabase()
	user_db.register('1', 'test@email.com', 'testuser', 'password', False)
	user = user_db.users['testuser']
	old_password_hash = user.password
	user.reset_password('newpassword')
	assert old_password_hash != user.password
	assert user_db.authenticate('testuser', 'newpassword') == True


def test_profile_management():
	user_db = UserDatabase()
	user_db.register('1', 'test@email.com', 'testuser', 'password', False)
	user = user_db.users['testuser']
	user.update_profile_picture('new_picture.jpg')
	assert user.profile_picture == 'new_picture.jpg'
	user.update_bio('This is a new bio')
	assert user.bio == 'This is a new bio'
	user.update_website_link('https://newwebsite.com')
	assert user.website_link == 'https://newwebsite.com'
	user.update_location('New Location')
	assert user.location == 'New Location'
	user.toggle_privacy()
	assert user.is_private == True
	user.toggle_privacy()
	assert user.is_private == False


def test_follow_unfollow():
	user_db = UserDatabase()
	user_db.register('1', 'test1@email.com', 'testuser1', 'password', False)
	user_db.register('2', 'test2@email.com', 'testuser2', 'password', False)
	user1 = user_db.users['testuser1']
	user2 = user_db.users['testuser2']
	user1.follow(user2)
	assert 'testuser2' in user1.following
	assert 'testuser1' in user2.followers
	assert 'testuser1 started following you.' in user2.notifications
	user1.unfollow(user2)
	assert 'testuser2' not in user1.following
	assert 'testuser1' not in user2.followers


def test_view_timeline():
	user_db = UserDatabase()
	user_db.register('1', 'test1@email.com', 'testuser1', 'password', False)
	user_db.register('2', 'test2@email.com', 'testuser2', 'password', False)
	user1 = user_db.users['testuser1']
	user2 = user_db.users['testuser2']
	user1.follow(user2)
	post = Post('1', 'Hello, world!', [], 'testuser2', datetime.now())
	user2.posts.append(post)
	assert post in user1.view_timeline(user_db)


def test_notifications():
	user_db = UserDatabase()
	user_db.register('1', 'test1@email.com', 'testuser1', 'password', False)
	user_db.register('2', 'test2@email.com', 'testuser2', 'password', False)
	user1 = user_db.users['testuser1']
	user2 = user_db.users['testuser2']
	user1.notify('You have a new follower.')
	assert 'You have a new follower.' in user1.notifications


def test_recommend_users():
	user_db = UserDatabase()
	user_db.register('1', 'test1@email.com', 'testuser1', 'password', False)
	user_db.register('2', 'test2@email.com', 'testuser2', 'password', False)
	user_db.register('3', 'test3@email.com', 'testuser3', 'password', False)
	user1 = user_db.users['testuser1']
	user2 = user_db.users['testuser2']
	user3 = user_db.users['testuser3']
	user1.follow(user2)
	user3.follow(user2)
	user2.follow(user1)
	user2.follow(user3)
	assert 'testuser3' in user1.recommend_users(user_db)

