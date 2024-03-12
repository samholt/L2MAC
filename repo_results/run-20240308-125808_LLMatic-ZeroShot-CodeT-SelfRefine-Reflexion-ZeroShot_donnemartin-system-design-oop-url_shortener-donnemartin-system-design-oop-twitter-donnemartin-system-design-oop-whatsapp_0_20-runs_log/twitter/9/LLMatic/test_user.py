import pytest
from user import User, register, authenticate
from post import Post


def test_register():
	assert register('test3@test.com', 'testuser', 'testpassword', False) == True


def test_authenticate():
	assert authenticate('test3@test.com', 'testpassword') != False


def test_reset_password():
	user = authenticate('test3@test.com', 'testpassword')
	user.reset_password('newpassword')
	assert user.verify_password('newpassword') == True


def test_edit_profile():
	user = authenticate('test3@test.com', 'newpassword')
	user.edit_profile(profile_picture='newpic.jpg', bio='new bio', website='newwebsite.com', location='new location')
	assert user.profile_picture == 'newpic.jpg'
	assert user.bio == 'new bio'
	assert user.website == 'newwebsite.com'
	assert user.location == 'new location'


def test_toggle_privacy():
	user = authenticate('test3@test.com', 'newpassword')
	user.toggle_privacy()
	assert user.is_private == True
	user.toggle_privacy()
	assert user.is_private == False


def test_follow_user():
	register('test4@test.com', 'testuser2', 'password', False)
	user1 = authenticate('test3@test.com', 'newpassword')
	user2 = authenticate('test4@test.com', 'password')
	assert user1.follow_user(user2) == True


def test_unfollow_user():
	user1 = authenticate('test3@test.com', 'newpassword')
	user2 = authenticate('test4@test.com', 'password')
	assert user1.unfollow_user(user2) == True


def test_view_timeline():
	user1 = authenticate('test3@test.com', 'newpassword')
	user2 = authenticate('test4@test.com', 'password')
	user1.follow_user(user2)
	new_post = Post.create_post(user2.email, 'new post')
	user2.posts.append(new_post)
	assert user1.view_timeline() == [new_post]


def test_recommend_users():
	register('test5@test.com', 'testuser3', 'password', False)
	user1 = authenticate('test3@test.com', 'newpassword')
	user3 = authenticate('test5@test.com', 'password')
	recommended_users = user1.recommend_users()
	assert user3 in recommended_users
