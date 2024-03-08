import pytest
from app import app, User, Post, Message, Notification, mock_db, post_db, message_db, notification_db
import jwt

def test_register():
	with app.test_client() as c:
		resp = c.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
		assert resp.status_code == 201
		assert 'User registered successfully' in resp.get_json()['message']
		assert isinstance(mock_db.get('test'), User)

def test_login():
	with app.test_client() as c:
		resp = c.post('/login', json={'username': 'test', 'password': 'test'})
		assert resp.status_code == 200
		assert 'token' in resp.get_json()
		decoded = jwt.decode(resp.get_json()['token'], 'secret', algorithms=['HS256'])
		assert decoded['username'] == 'test'

def test_profile():
	with app.test_client() as c:
		resp = c.post('/login', json={'username': 'test', 'password': 'test'})
		token = resp.get_json()['token']
		resp = c.get('/profile', headers={'Authorization': token})
		assert resp.status_code == 200
		assert resp.get_json()['username'] == 'test'
		resp = c.put('/profile', headers={'Authorization': token}, json={'bio': 'This is a test bio'})
		assert resp.status_code == 200
		assert resp.get_json()['bio'] == 'This is a test bio'

def test_follow():
	with app.test_client() as c:
		resp = c.post('/register', json={'email': 'test2@test.com', 'username': 'test2', 'password': 'test2'})
		assert resp.status_code == 201
		resp = c.post('/login', json={'username': 'test', 'password': 'test'})
		token = resp.get_json()['token']
		resp = c.post('/follow', headers={'Authorization': token}, json={'to_follow': 'test2'})
		assert resp.status_code == 200
		assert 'Followed user' in resp.get_json()['message']
		user = mock_db.get('test')
		assert 'test2' in user.following
		user2 = mock_db.get('test2')
		assert 'test' in user2.followers
		assert isinstance(notification_db.get(0), Notification)
		resp = c.delete('/follow', headers={'Authorization': token}, json={'to_follow': 'test2'})
		assert resp.status_code == 200
		assert 'Unfollowed user' in resp.get_json()['message']
		assert 'test2' not in user.following
		assert 'test' not in user2.followers

def test_posts():
	with app.test_client() as c:
		resp = c.post('/login', json={'username': 'test', 'password': 'test'})
		token = resp.get_json()['token']
		resp = c.post('/posts', headers={'Authorization': token}, json={'text': 'This is a test post', 'images': []})
		assert resp.status_code == 201
		assert 'Post created' in resp.get_json()['message']
		assert isinstance(post_db.get(resp.get_json()['post_id']), Post)
		assert isinstance(notification_db.get(1), Notification)
		resp = c.get('/posts', headers={'Authorization': token})
		assert resp.status_code == 200
		assert isinstance(resp.get_json(), dict)

def test_notifications():
	with app.test_client() as c:
		resp = c.post('/login', json={'username': 'test', 'password': 'test'})
		token = resp.get_json()['token']
		resp = c.get('/notifications', headers={'Authorization': token})
		assert resp.status_code == 200
		assert isinstance(resp.get_json(), dict)

def test_messages():
	with app.test_client() as c:
		resp = c.post('/login', json={'username': 'test', 'password': 'test'})
		token = resp.get_json()['token']
		resp = c.post('/messages', headers={'Authorization': token}, json={'receiver': 'test2', 'text': 'Hello, test2'})
		assert resp.status_code == 201
		assert 'Message sent' in resp.get_json()['message']
		assert isinstance(message_db.get(resp.get_json()['message_id']), Message)
		resp = c.get('/messages', headers={'Authorization': token})
		assert resp.status_code == 200
		assert isinstance(resp.get_json(), dict)

def test_search():
	with app.test_client() as c:
		resp = c.get('/search?q=test')
		assert resp.status_code == 200
		assert 'users' in resp.get_json()
		assert 'posts' in resp.get_json()

def test_trending():
	with app.test_client() as c:
		resp = c.get('/trending')
		assert resp.status_code == 200
		assert 'trending' in resp.get_json()

def test_recommendations():
	with app.test_client() as c:
		resp = c.post('/login', json={'username': 'test', 'password': 'test'})
		token = resp.get_json()['token']
		resp = c.get('/recommendations', headers={'Authorization': token})
		assert resp.status_code == 200
		assert 'recommendations' in resp.get_json()

def test_home():
	with app.test_client() as c:
		resp = c.get('/')
		assert resp.data == b'Hello, World!'

