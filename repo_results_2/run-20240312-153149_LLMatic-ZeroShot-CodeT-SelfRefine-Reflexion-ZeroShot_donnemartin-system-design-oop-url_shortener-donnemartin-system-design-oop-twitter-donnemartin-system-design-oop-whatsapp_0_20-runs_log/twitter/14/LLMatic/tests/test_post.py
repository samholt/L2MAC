import pytest
from flask import Flask
from models import User, Post, users_db, posts_db
from views import views

app = Flask(__name__)
app.register_blueprint(views)

def setup_function():
	users_db.clear()
	posts_db.clear()
	test_user = User('test@test.com', 'testuser', 'testpass')
	users_db['testuser'] = test_user
	test_post = Post('Test post', ['image1.jpg', 'image2.jpg'], 'testuser')
	posts_db[0] = test_post


def test_create_post():
	with app.test_request_context('/post', method='POST', json={'username': 'testuser', 'password': 'testpass', 'text': 'Test post', 'images': ['image1.jpg', 'image2.jpg']}):
		response = app.test_client().post('/post', json={'username': 'testuser', 'password': 'testpass', 'text': 'Test post', 'images': ['image1.jpg', 'image2.jpg']})
		assert response.status_code == 201
		assert len(posts_db) == 2


def test_view_post():
	with app.test_request_context('/post/0', method='GET'):
		response = app.test_client().get('/post/0')
		assert response.status_code == 200
		data = response.get_json()
		assert data['text'] == 'Test post'
		assert data['images'] == ['image1.jpg', 'image2.jpg']
		assert data['user'] == 'testuser'
		assert data['likes'] == 0
		assert data['retweets'] == 0
		assert data['replies'] == []


def test_delete_post():
	with app.test_request_context('/post/0', method='DELETE', json={'username': 'testuser', 'password': 'testpass'}):
		response = app.test_client().delete('/post/0', json={'username': 'testuser', 'password': 'testpass'})
		assert response.status_code == 200
		assert len(posts_db) == 0


def test_like_post():
	with app.test_request_context('/post/0/like', method='POST', json={'username': 'testuser', 'password': 'testpass'}):
		response = app.test_client().post('/post/0/like', json={'username': 'testuser', 'password': 'testpass'})
		assert response.status_code == 200
		assert posts_db[0].likes == 1


def test_retweet_post():
	with app.test_request_context('/post/0/retweet', method='POST', json={'username': 'testuser', 'password': 'testpass'}):
		response = app.test_client().post('/post/0/retweet', json={'username': 'testuser', 'password': 'testpass'})
		assert response.status_code == 200
		assert posts_db[0].retweets == 1


def test_reply_post():
	with app.test_request_context('/post/0/reply', method='POST', json={'username': 'testuser', 'password': 'testpass', 'reply': 'Test reply'}):
		response = app.test_client().post('/post/0/reply', json={'username': 'testuser', 'password': 'testpass', 'reply': 'Test reply'})
		assert response.status_code == 200
		assert posts_db[0].replies == ['Test reply']
