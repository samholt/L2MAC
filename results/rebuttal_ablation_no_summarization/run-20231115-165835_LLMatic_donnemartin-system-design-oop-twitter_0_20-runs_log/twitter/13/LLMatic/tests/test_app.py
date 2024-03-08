import pytest
from app import app, User, Post, mock_db, post_db
import jwt

def test_home():
	with app.test_client() as c:
		resp = c.get('/')
		assert resp.status_code == 200
		assert resp.data == b'Hello, World!'

def test_register():
	with app.test_client() as c:
		resp = c.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
		assert resp.status_code == 201
		assert resp.get_json()['message'] == 'User registered successfully'
		assert isinstance(mock_db['test'], User)

def test_login():
	with app.test_client() as c:
		resp = c.post('/login', json={'username': 'test', 'password': 'test'})
		assert resp.status_code == 200
		token = resp.get_json()['token']
		assert jwt.decode(token, 'secret', algorithms=['HS256'])['username'] == 'test'
	resp = c.post('/login', json={'username': 'test', 'password': 'wrong'})
	assert resp.status_code == 401
	assert resp.get_json()['message'] == 'Invalid credentials'

def test_profile():
	with app.test_client() as c:
		resp = c.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
		assert resp.status_code == 201
		resp = c.post('/login', json={'username': 'test', 'password': 'test'})
		assert resp.status_code == 200
		token = resp.get_json()['token']
		resp = c.get('/profile', headers={'Authorization': token})
		assert resp.status_code == 200
		assert resp.get_json()['username'] == 'test'
		resp = c.put('/profile', headers={'Authorization': token}, json={'bio': 'This is a test bio'})
		assert resp.status_code == 200
		assert resp.get_json()['message'] == 'Profile updated successfully'
		resp = c.get('/profile', headers={'Authorization': token})
		assert resp.status_code == 200
		assert resp.get_json()['bio'] == 'This is a test bio'

def test_follow():
	with app.test_client() as c:
		resp = c.post('/register', json={'email': 'test1@test.com', 'username': 'test1', 'password': 'test'})
		assert resp.status_code == 201
		resp = c.post('/register', json={'email': 'test2@test.com', 'username': 'test2', 'password': 'test'})
		assert resp.status_code == 201
		resp = c.post('/login', json={'username': 'test1', 'password': 'test'})
		assert resp.status_code == 200
		token = resp.get_json()['token']
		resp = c.post('/follow', headers={'Authorization': token}, json={'follow': 'test2'})
		assert resp.status_code == 200
		assert resp.get_json()['message'] == 'Followed user successfully'
		assert 'test2' in mock_db['test1'].following
		assert 'test1' in mock_db['test2'].followers
		resp = c.delete('/follow', headers={'Authorization': token}, json={'unfollow': 'test2'})
		assert resp.status_code == 200
		assert resp.get_json()['message'] == 'Unfollowed user successfully'
		assert 'test2' not in mock_db['test1'].following
		assert 'test1' not in mock_db['test2'].followers

def test_timeline():
	with app.test_client() as c:
		resp = c.post('/register', json={'email': 'test1@test.com', 'username': 'test1', 'password': 'test'})
		assert resp.status_code == 201
		resp = c.post('/register', json={'email': 'test2@test.com', 'username': 'test2', 'password': 'test'})
		assert resp.status_code == 201
		resp = c.post('/login', json={'username': 'test1', 'password': 'test'})
		assert resp.status_code == 200
		token1 = resp.get_json()['token']
		resp = c.post('/login', json={'username': 'test2', 'password': 'test'})
		assert resp.status_code == 200
		token2 = resp.get_json()['token']
		resp = c.post('/post', headers={'Authorization': token2}, json={'content': 'This is a test post from test2', 'images': []})
		assert resp.status_code == 201
		resp = c.post('/follow', headers={'Authorization': token1}, json={'follow': 'test2'})
		assert resp.status_code == 200
		resp = c.get('/timeline', headers={'Authorization': token1})
		assert resp.status_code == 200
		timeline_posts = resp.get_json()
		assert 'This is a test post from test2' in [post['content'] for post in timeline_posts]

def test_post():
	with app.test_client() as c:
		resp = c.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
		assert resp.status_code == 201
		resp = c.post('/login', json={'username': 'test', 'password': 'test'})
		assert resp.status_code == 200
		token = resp.get_json()['token']
		resp = c.post('/post', headers={'Authorization': token}, json={'content': 'This is a test post', 'images': []})
		assert resp.status_code == 201
		assert resp.get_json()['message'] == 'Post created successfully'
		assert isinstance(post_db['This is a test post'], Post)
		resp = c.put('/post', headers={'Authorization': token}, json={'content': 'This is a test post', 'likes': 1})
		assert resp.status_code == 200
		assert resp.get_json()['message'] == 'Post updated successfully'
		assert post_db['This is a test post'].likes == 1
		resp = c.delete('/post', headers={'Authorization': token}, json={'content': 'This is a test post'})
		assert resp.status_code == 200
		assert resp.get_json()['message'] == 'Post deleted successfully'
		assert 'This is a test post' not in post_db

def test_search():
	with app.test_client() as c:
		resp = c.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
		assert resp.status_code == 201
		resp = c.post('/login', json={'username': 'test', 'password': 'test'})
		assert resp.status_code == 200
		token = resp.get_json()['token']
		resp = c.post('/post', headers={'Authorization': token}, json={'content': 'This is a test post', 'images': []})
		assert resp.status_code == 201
		resp = c.get('/search?keyword=test')
		assert resp.status_code == 200
		results = resp.get_json()
		assert 'test' in [user['username'] for user in results['users']]
		assert 'This is a test post' in [post['content'] for post in results['posts']]

def test_filter():
	with app.test_client() as c:
		resp = c.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
		assert resp.status_code == 201
		resp = c.post('/login', json={'username': 'test', 'password': 'test'})
		assert resp.status_code == 200
		token = resp.get_json()['token']
		resp = c.post('/post', headers={'Authorization': token}, json={'content': 'This is a test post', 'images': []})
		assert resp.status_code == 201
		resp = c.get('/filter?options=test')
		assert resp.status_code == 200
		results = resp.get_json()
		assert 'This is a test post' in [post['content'] for post in results['posts']]
