from models import User, Post
from datetime import datetime


def test_user_model():
	user = User(1, 'testuser', 'testuser@example.com', 'password', 'profile_picture.jpg', 'This is a test user.', 'http://example.com', 'Test City')
	assert user.id == 1
	assert user.username == 'testuser'
	assert user.email == 'testuser@example.com'
	assert user.check_password('password')
	assert user.profile_picture == 'profile_picture.jpg'
	assert user.bio == 'This is a test user.'
	assert user.website_link == 'http://example.com'
	assert user.location == 'Test City'


def test_post_model():
	post = Post(1, 1, 'This is a test post.', 'image.jpg', datetime.utcnow())
	assert post.id == 1
	assert post.user_id == 1
	assert post.text == 'This is a test post.'
	assert post.image == 'image.jpg'
	assert isinstance(post.timestamp, datetime)
