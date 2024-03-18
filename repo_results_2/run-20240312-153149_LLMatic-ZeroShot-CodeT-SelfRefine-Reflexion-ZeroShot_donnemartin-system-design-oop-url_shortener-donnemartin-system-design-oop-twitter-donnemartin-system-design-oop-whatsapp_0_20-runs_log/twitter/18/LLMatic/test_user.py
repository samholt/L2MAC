import pytest
from user import User


def test_register():
	user = User('test@test.com', 'testuser', 'testpass', False)
	assert user.register() == {'email': 'test@test.com', 'username': 'testuser', 'password': 'testpass', 'is_private': False}


def test_authenticate():
	user = User('test@test.com', 'testuser', 'testpass', False)
	assert 'Invalid credentials' == user.authenticate('wrong@test.com', 'wrongpass')
	assert isinstance(user.authenticate('test@test.com', 'testpass'), str)


def test_reset_password():
	user = User('test@test.com', 'testuser', 'testpass', False)
	user.reset_password('newpass')
	assert 'Invalid credentials' == user.authenticate('test@test.com', 'testpass')
	assert isinstance(user.authenticate('test@test.com', 'newpass'), str)


def test_set_profile_picture():
	user = User('test@test.com', 'testuser', 'testpass', False)
	assert user.set_profile_picture('new_picture.jpg') == 'Profile picture updated'


def test_set_bio():
	user = User('test@test.com', 'testuser', 'testpass', False)
	assert user.set_bio('This is a test bio') == 'Bio updated'


def test_set_website_link():
	user = User('test@test.com', 'testuser', 'testpass', False)
	assert user.set_website_link('https://test.com') == 'Website link updated'


def test_set_location():
	user = User('test@test.com', 'testuser', 'testpass', False)
	assert user.set_location('Test City, Test Country') == 'Location updated'


def test_toggle_privacy():
	user = User('test@test.com', 'testuser', 'testpass', False)
	user.toggle_privacy()
	assert user.is_private == True


def test_follow():
	user1 = User('test1@test.com', 'testuser1', 'testpass1', False)
	user2 = User('test2@test.com', 'testuser2', 'testpass2', False)
	assert user1.follow(user2) == 'Followed successfully'
	assert user2 in user1.following
	assert user1 in user2.followers
	assert f'{user1.username} started following you.' in user2.notifications


def test_unfollow():
	user1 = User('test1@test.com', 'testuser1', 'testpass1', False)
	user2 = User('test2@test.com', 'testuser2', 'testpass2', False)
	user1.follow(user2)
	assert user1.unfollow(user2) == 'Unfollowed successfully'
	assert user2 not in user1.following
	assert user1 not in user2.followers


def test_view_timeline():
	user1 = User('test1@test.com', 'testuser1', 'testpass1', False)
	user2 = User('test2@test.com', 'testuser2', 'testpass2', False)
	user1.follow(user2)
	user2.posts = [{'content': 'Hello, world!', 'timestamp': '2022-01-01T00:00:00Z'}]
	assert user1.view_timeline() == user2.posts

