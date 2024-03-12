import pytest
from models import User, Post, users_db, posts_db
from views import views
from flask import Flask

app = Flask(__name__)
app.register_blueprint(views)
client = app.test_client()


def test_create_post():
	user = User('test@test.com', 'testuser', 'testpass')
	users_db['test@test.com'] = user
	response = client.post('/create-post', json={'email': 'test@test.com', 'text': 'Test post', 'images': ['image1.jpg', 'image2.jpg']})
	assert response.status_code == 200
	assert 'Post created successfully' in response.get_json()['message']


def test_delete_post():
	user = User('test@test.com', 'testuser', 'testpass')
	users_db['test@test.com'] = user
	post = Post(user, 'Test post', ['image1.jpg', 'image2.jpg'])
	posts_db['testpost'] = post
	post_id = 'testpost'
	response = client.delete('/delete-post', json={'email': 'test@test.com', 'post_id': post_id})
	assert response.status_code == 200
	assert 'Post deleted successfully' in response.get_json()['message']
	assert post_id not in posts_db


def test_like_post():
	user = User('test@test.com', 'testuser', 'testpass')
	users_db['test@test.com'] = user
	post = Post(user, 'Test post', ['image1.jpg', 'image2.jpg'])
	posts_db['testpost'] = post
	post_id = 'testpost'
	response = client.post('/like-post', json={'email': 'test@test.com', 'post_id': post_id})
	assert response.status_code == 200
	assert 'Post liked successfully' in response.get_json()['message']
	assert user in post.likes


def test_retweet_post():
	user = User('test@test.com', 'testuser', 'testpass')
	users_db['test@test.com'] = user
	post = Post(user, 'Test post', ['image1.jpg', 'image2.jpg'])
	posts_db['testpost'] = post
	post_id = 'testpost'
	response = client.post('/retweet-post', json={'email': 'test@test.com', 'post_id': post_id})
	assert response.status_code == 200
	assert 'Post retweeted successfully' in response.get_json()['message']
	assert user in post.retweets


def test_reply_post():
	user = User('test@test.com', 'testuser', 'testpass')
	users_db['test@test.com'] = user
	post = Post(user, 'Test post', ['image1.jpg', 'image2.jpg'])
	posts_db['testpost'] = post
	post_id = 'testpost'
	response = client.post('/reply-post', json={'email': 'test@test.com', 'post_id': post_id, 'text': 'Test reply'})
	assert response.status_code == 200
	assert 'Reply posted successfully' in response.get_json()['message']
	assert {'user': user, 'text': 'Test reply'} in post.replies
