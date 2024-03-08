import pytest
from flask import Flask, json
from app import app, User, Post, Message, Notification, mock_db, posts_db, messages_db, notifications_db, trending_db

@pytest.fixture

def create_app():
	app = Flask(__name__)
	@app.route('/')
	def home():
		return 'Hello, World!', 200
	return app


def test_home(create_app):
	with create_app.test_client() as client:
		response = client.get('/')
		assert response.status_code == 200
		assert response.data == b'Hello, World!'


def test_register():
	with app.test_client() as client:
		response = client.post('/register', data=json.dumps({'email': 'test@test.com', 'username': 'test', 'password': 'test'}), content_type='application/json')
		assert response.status_code == 200
		assert 'User registered successfully' in response.get_data(as_text=True)
		assert isinstance(mock_db.get('test'), User)


def test_login():
	with app.test_client() as client:
		response = client.post('/login', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
		assert response.status_code == 200
		assert 'token' in response.get_data(as_text=True)
		response = client.post('/login', data=json.dumps({'username': 'test', 'password': 'wrong'}), content_type='application/json')
		assert response.status_code == 401
		assert 'Invalid username or password' in response.get_data(as_text=True)


def test_edit_profile():
	with app.test_client() as client:
		response = client.post('/edit_profile', data=json.dumps({'username': 'test', 'password': 'test', 'bio': 'This is a test bio'}), content_type='application/json')
		assert response.status_code == 200
		assert 'Profile updated successfully' in response.get_data(as_text=True)
		assert mock_db.get('test').bio == 'This is a test bio'


def test_toggle_privacy():
	with app.test_client() as client:
		response = client.post('/toggle_privacy', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
		assert response.status_code == 200
		assert 'Profile privacy toggled successfully' in response.get_data(as_text=True)
		assert mock_db.get('test').is_private == True


def test_follow():
	with app.test_client() as client:
		response = client.post('/register', data=json.dumps({'email': 'test2@test.com', 'username': 'test2', 'password': 'test2'}), content_type='application/json')
		response = client.post('/follow', data=json.dumps({'username': 'test', 'password': 'test', 'to_follow': 'test2'}), content_type='application/json')
		assert response.status_code == 200
		assert 'Followed successfully' in response.get_data(as_text=True)
		assert 'test2' in mock_db.get('test').following
		assert 'test' in mock_db.get('test2').followers


def test_unfollow():
	with app.test_client() as client:
		response = client.post('/unfollow', data=json.dumps({'username': 'test', 'password': 'test', 'to_unfollow': 'test2'}), content_type='application/json')
		assert response.status_code == 200
		assert 'Unfollowed successfully' in response.get_data(as_text=True)
		assert 'test2' not in mock_db.get('test').following
		assert 'test' not in mock_db.get('test2').followers


def test_block():
	with app.test_client() as client:
		response = client.post('/block', data=json.dumps({'username': 'test', 'password': 'test', 'to_block': 'test2'}), content_type='application/json')
		assert response.status_code == 200
		assert 'Blocked successfully' in response.get_data(as_text=True)
		assert 'test2' in mock_db.get('test').blocked


def test_unblock():
	with app.test_client() as client:
		response = client.post('/unblock', data=json.dumps({'username': 'test', 'password': 'test', 'to_unblock': 'test2'}), content_type='application/json')
		assert response.status_code == 200
		assert 'Unblocked successfully' in response.get_data(as_text=True)
		assert 'test2' not in mock_db.get('test').blocked


def test_send_message():
	with app.test_client() as client:
		response = client.post('/send_message', data=json.dumps({'sender': 'test', 'password': 'test', 'receiver': 'test2', 'text': 'Hello'}), content_type='application/json')
		assert response.status_code == 200
		assert 'Message sent successfully' in response.get_data(as_text=True)
		assert isinstance(messages_db.get(0), Message)


def test_timeline():
	with app.test_client() as client:
		response = client.post('/create_post', data=json.dumps({'username': 'test2', 'password': 'test2', 'text': 'This is a test post', 'images': ['image1.jpg', 'image2.jpg']}), content_type='application/json')
		response = client.post('/follow', data=json.dumps({'username': 'test', 'password': 'test', 'to_follow': 'test2'}), content_type='application/json')
		response = client.post('/timeline', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
		assert response.status_code == 200
		assert 'This is a test post' in response.get_data(as_text=True)


def test_create_post():
	with app.test_client() as client:
		response = client.post('/create_post', data=json.dumps({'username': 'test', 'password': 'test', 'text': 'This is a test post', 'images': ['image1.jpg', 'image2.jpg']}), content_type='application/json')
		assert response.status_code == 200
		assert 'Post created successfully' in response.get_data(as_text=True)
		assert isinstance(posts_db.get(0), Post)


def test_search():
	with app.test_client() as client:
		response = client.post('/search', data=json.dumps({'keyword': 'test'}), content_type='application/json')
		assert response.status_code == 200
		assert 'This is a test post' in response.get_data(as_text=True)


def test_create_notification():
	with app.test_client() as client:
		response = client.post('/create_notification', data=json.dumps({'username': 'test', 'password': 'test', 'text': 'This is a test notification'}), content_type='application/json')
		assert response.status_code == 200
		assert 'Notification created successfully' in response.get_data(as_text=True)
		assert isinstance(notifications_db.get(0), Notification)


def test_trending():
	with app.test_client() as client:
		response = client.post('/create_post', data=json.dumps({'username': 'test', 'password': 'test', 'text': '#test'}), content_type='application/json')
		response = client.get('/trending')
		assert response.status_code == 200
		assert '#test' in response.get_data(as_text=True)
		assert trending_db.get('#test') == 1


def test_recommendations():
	with app.test_client() as client:
		response = client.post('/register', data=json.dumps({'email': 'test3@test.com', 'username': 'test3', 'password': 'test3'}), content_type='application/json')
		response = client.post('/follow', data=json.dumps({'username': 'test2', 'password': 'test2', 'to_follow': 'test3'}), content_type='application/json')
		response = client.post('/recommendations', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
		assert response.status_code == 200
		assert 'test3' in response.get_data(as_text=True)

