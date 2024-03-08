import pytest
from user import User


def test_register():
	user = User('user@example.com', 'username', 'password')
	assert user.register() == {'username': {'email': 'user@example.com', 'password': 'password', 'profile_picture': None, 'bio': None, 'website_link': None, 'location': None, 'private': False, 'following': [], 'followers': [], 'notifications': [], 'messages': [], 'blocked_users': [], 'posts': [], 'username': 'username'}}


def test_authenticate():
	user = User('user@example.com', 'username', 'password')
	user.register()
	assert 'Invalid username or password' in user.authenticate('username', 'wrong_password')
	assert 'Invalid username or password' in user.authenticate('wrong_username', 'password')
	assert isinstance(user.authenticate('username', 'password'), str)


def test_reset_password():
	user = User('user@example.com', 'username', 'password')
	user.register()
	assert user.reset_password('username', 'new_password') == 'Password reset successful'
	assert 'Invalid username or password' in user.authenticate('username', 'password')
	assert isinstance(user.authenticate('username', 'new_password'), str)


def test_edit_profile():
	user = User('user@example.com', 'username', 'password')
	assert user.edit_profile(profile_picture='new_picture.jpg', bio='new_bio', website_link='new_website.com', location='new_location') == 'Profile updated successfully'
	assert user.profile_picture == 'new_picture.jpg'
	assert user.bio == 'new_bio'
	assert user.website_link == 'new_website.com'
	assert user.location == 'new_location'


def test_toggle_privacy():
	user = User('user@example.com', 'username', 'password')
	assert user.toggle_privacy() == 'Privacy setting updated successfully'
	assert user.private == True
	assert user.toggle_privacy() == 'Privacy setting updated successfully'
	assert user.private == False


def test_follow():
	user1 = User('user1@example.com', 'user1', 'password1')
	user2 = User('user2@example.com', 'user2', 'password2')
	assert user1.follow(user2) == 'Followed successfully'
	assert user2 in user1.following
	assert user1 in user2.followers
	assert f'{user1.username} started following you.' in user2.notifications


def test_unfollow():
	user1 = User('user1@example.com', 'user1', 'password1')
	user2 = User('user2@example.com', 'user2', 'password2')
	user1.follow(user2)
	assert user1.unfollow(user2) == 'Unfollowed successfully'
	assert user2 not in user1.following
	assert user1 not in user2.followers


def test_view_timeline():
	user1 = User('user1@example.com', 'user1', 'password1')
	user2 = User('user2@example.com', 'user2', 'password2')
	user1.follow(user2)
	user2.posts.append({'content': 'Hello, world!', 'timestamp': '2022-01-01T00:00:00Z'})
	assert user1.view_timeline() == [{'content': 'Hello, world!', 'timestamp': '2022-01-01T00:00:00Z'}]


def test_view_notifications():
	user1 = User('user1@example.com', 'user1', 'password1')
	user2 = User('user2@example.com', 'user2', 'password2')
	user1.follow(user2)
	assert user2.view_notifications() == [f'{user1.username} started following you.']


def test_recommend_users():
	user1 = User('user1@example.com', 'user1', 'password1', bio='music sports')
	user2 = User('user2@example.com', 'user2', 'password2', bio='music movies')
	user3 = User('user3@example.com', 'user3', 'password3', bio='sports movies')
	user4 = User('user4@example.com', 'user4', 'password4', bio='music sports movies')
	user1.register()
	user2.register()
	user3.register()
	user4.register()
	user1.follow(user2)
	user2.follow(user3)
	user3.follow(user4)
	user4.follow(user1)
	recommendations = user1.recommend_users()
	assert len(recommendations) > 0
	assert all(user['username'] not in user1.following and user['username'] not in user1.blocked_users for user in recommendations)
