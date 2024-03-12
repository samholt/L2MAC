import pytest
import routes
from models import db, User, Post, Comment, Like, Follow, Message, Notification

@pytest.fixture
def client():
	with routes.app.test_client() as client:
		yield client

@pytest.fixture
def init_database():
	db.create_all()
	yield
	db.drop_all()

@pytest.fixture
def new_user():
	user = User(email='test@test.com', username='test', password='test')
	return user

@pytest.fixture
def new_post():
	post = Post(content='This is a test post', user_id=1)
	return post

@pytest.fixture
def new_comment():
	comment = Comment(content='This is a test comment', post_id=1, user_id=1)
	return comment

@pytest.fixture
def new_like():
	like = Like(post_id=1, user_id=1)
	return like

@pytest.fixture
def new_follow():
	follow = Follow(follower_id=1, followed_id=2)
	return follow

@pytest.fixture
def new_message():
	message = Message(content='This is a test message', sender_id=1, receiver_id=2)
	return message

@pytest.fixture
def new_notification():
	notification = Notification(content='This is a test notification', user_id=1)
	return notification

def test_register(client, init_database, new_user):
	response = client.post('/register', json={'email': new_user.email, 'username': new_user.username, 'password': new_user.password})
	assert response.status_code == 201

def test_login(client, init_database, new_user):
	response = client.post('/login', json={'email': new_user.email, 'password': new_user.password})
	assert response.status_code == 200

def test_create_post(client, init_database, new_post):
	response = client.post('/post', json={'content': new_post.content, 'user_id': new_post.user_id})
	assert response.status_code == 201

def test_create_comment(client, init_database, new_comment):
	response = client.post('/comment', json={'content': new_comment.content, 'post_id': new_comment.post_id, 'user_id': new_comment.user_id})
	assert response.status_code == 201

def test_create_like(client, init_database, new_like):
	response = client.post('/like', json={'post_id': new_like.post_id, 'user_id': new_like.user_id})
	assert response.status_code == 201

def test_create_follow(client, init_database, new_follow):
	response = client.post('/follow', json={'follower_id': new_follow.follower_id, 'followed_id': new_follow.followed_id})
	assert response.status_code == 201

def test_create_message(client, init_database, new_message):
	response = client.post('/message', json={'content': new_message.content, 'sender_id': new_message.sender_id, 'receiver_id': new_message.receiver_id})
	assert response.status_code == 201

def test_create_notification(client, init_database, new_notification):
	response = client.post('/notification', json={'content': new_notification.content, 'user_id': new_notification.user_id})
	assert response.status_code == 201
