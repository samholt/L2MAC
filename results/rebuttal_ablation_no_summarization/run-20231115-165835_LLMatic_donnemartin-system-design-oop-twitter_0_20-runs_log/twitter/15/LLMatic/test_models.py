from models import User, Post
from datetime import datetime


def test_user_model():
	user = User(1, 'test@test.com', 'testuser', 'testpassword', 'test.jpg', 'test bio', 'www.test.com', 'test location')
	assert user.id == 1
	assert user.email == 'test@test.com'
	assert user.username == 'testuser'
	assert user.profile_picture == 'test.jpg'
	assert user.bio == 'test bio'
	assert user.website_link == 'www.test.com'
	assert user.location == 'test location'
	assert user.check_password('testpassword')
	assert not user.check_password('wrongpassword')

	user2 = User(2, 'test2@test.com', 'testuser2', 'testpassword2', 'test2.jpg', 'test bio2', 'www.test2.com', 'test location2')
	user.follow(user2)
	assert user2 in user.following
	assert user in user2.followers
	user.unfollow(user2)
	assert user2 not in user.following
	assert user not in user2.followers


def test_post_model():
	post = Post(1, 1, 'test text', 'test.jpg')
	assert post.id == 1
	assert post.user_id == 1
	assert post.text == 'test text'
	assert post.image == 'test.jpg'
	assert isinstance(post.timestamp, datetime)
	post.delete()
	assert post.id is None
	assert post.user_id is None
	assert post.text is None
	assert post.image is None
	assert post.timestamp is None
