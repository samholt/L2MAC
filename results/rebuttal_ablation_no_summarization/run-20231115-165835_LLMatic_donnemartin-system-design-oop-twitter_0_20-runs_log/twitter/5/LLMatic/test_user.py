import pytest
from user import User
from post import Post


def test_user_registration():
	user = User('test@test.com', 'testuser', 'testpassword')
	assert user.email == 'test@test.com'
	assert user.username == 'testuser'
	assert user.password != 'testpassword'


def test_user_authentication():
	user = User('test@test.com', 'testuser', 'testpassword')
	assert user.authenticate('testuser', 'testpassword') is not None
	assert user.authenticate('testuser', 'wrongpassword') is None


def test_user_password_reset():
	user = User('test@test.com', 'testuser', 'testpassword')
	user.reset_password('newpassword')
	assert user.authenticate('testuser', 'newpassword') is not None
	assert user.authenticate('testuser', 'testpassword') is None


def test_user_profile_update():
	user = User('test@test.com', 'testuser', 'testpassword')
	user.update_profile(profile_picture='newpic.jpg', bio='new bio', website='newwebsite.com', location='new location')
	assert user.profile_picture == 'newpic.jpg'
	assert user.bio == 'new bio'
	assert user.website == 'newwebsite.com'
	assert user.location == 'new location'


def test_user_privacy_toggle():
	user = User('test@test.com', 'testuser', 'testpassword')
	user.toggle_privacy()
	assert user.is_private == True
	user.toggle_privacy()
	assert user.is_private == False


def test_user_follow_unfollow():
	user1 = User('test1@test.com', 'testuser1', 'testpassword1')
	user2 = User('test2@test.com', 'testuser2', 'testpassword2')
	user1.follow(user2)
	assert user2 in user1.following
	assert user1 in user2.followers
	user1.unfollow(user2)
	assert user2 not in user1.following
	assert user1 not in user2.followers


def test_user_timeline():
	user1 = User('test1@test.com', 'testuser1', 'testpassword1')
	user2 = User('test2@test.com', 'testuser2', 'testpassword2')
	user1.follow(user2)
	post = Post(user2, 'Hello, world!')
	user2.posts.append(post)
	assert post in user1.view_timeline()


def test_user_notifications():
	user = User('test@test.com', 'testuser', 'testpassword')
	user.add_notification('User X liked your post')
	assert 'User X liked your post' in user.view_notifications()


def test_user_recommendations():
	user1 = User('test1@test.com', 'testuser1', 'testpassword1')
	user2 = User('test2@test.com', 'testuser2', 'testpassword2')
	user3 = User('test3@test.com', 'testuser3', 'testpassword3')
	user1.follow(user2)
	user2.follow(user3)
	assert user3 in user1.recommend_users([user2, user3])
	assert user2 not in user1.recommend_users([user2, user3])

