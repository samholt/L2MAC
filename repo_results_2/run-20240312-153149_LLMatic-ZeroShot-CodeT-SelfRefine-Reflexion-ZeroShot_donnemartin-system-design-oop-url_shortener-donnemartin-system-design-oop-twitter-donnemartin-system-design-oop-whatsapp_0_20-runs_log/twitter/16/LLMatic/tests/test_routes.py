import pytest
import jwt
from models import User, users_db, posts_db
from app import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}


def test_authenticate(client):
	response = client.post('/authenticate', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert 'token' in response.get_json()


def test_profile(client):
	user = users_db['test@test.com']
	token = jwt.encode({'email': user.email}, 'secret', algorithm='HS256')
	response = client.get('/profile', headers={'Authorization': token})
	assert response.status_code == 200
	assert response.get_json() == {
		'email': user.email,
		'username': user.username,
		'profile_picture': user.profile_picture,
		'bio': user.bio,
		'website_link': user.website_link,
		'location': user.location
	}


def test_create_post(client):
	user = users_db['test@test.com']
	token = jwt.encode({'email': user.email}, 'secret', algorithm='HS256')
	response = client.post('/post', headers={'Authorization': token}, json={'text': 'Hello, world!', 'images': []})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post created successfully'}


def test_like_post(client):
	user = users_db['test@test.com']
	token = jwt.encode({'email': user.email}, 'secret', algorithm='HS256')
	response = client.post('/like', headers={'Authorization': token}, json={'post_id': 0})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post liked successfully'}


def test_retweet_post(client):
	user = users_db['test@test.com']
	token = jwt.encode({'email': user.email}, 'secret', algorithm='HS256')
	response = client.post('/retweet', headers={'Authorization': token}, json={'post_id': 0})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post retweeted successfully'}


def test_reply_to_post(client):
	user = users_db['test@test.com']
	token = jwt.encode({'email': user.email}, 'secret', algorithm='HS256')
	response = client.post('/reply', headers={'Authorization': token}, json={'post_id': 0, 'reply_text': 'Hello, world!'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Reply posted successfully'}


def test_search(client):
	response = client.get('/search', query_string={'keyword': 'Hello'})
	assert response.status_code == 200
	assert 'results' in response.get_json()


def test_filter(client):
	response = client.get('/filter', query_string={'element': 'Hello'})
	assert response.status_code == 200
	assert 'results' in response.get_json()


def test_follow(client):
	user = users_db['test@test.com']
	token = jwt.encode({'email': user.email}, 'secret', algorithm='HS256')
	response = client.post('/follow', headers={'Authorization': token}, json={'target_username': 'test2'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Followed user successfully'}


def test_unfollow(client):
	user = users_db['test@test.com']
	token = jwt.encode({'email': user.email}, 'secret', algorithm='HS256')
	response = client.post('/unfollow', headers={'Authorization': token}, json={'target_username': 'test2'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Unfollowed user successfully'}


def test_send_message(client):
	user = users_db['test@test.com']
	token = jwt.encode({'email': user.email}, 'secret', algorithm='HS256')
	response = client.post('/message', headers={'Authorization': token}, json={'recipient_username': 'test2', 'text': 'Hello, world!'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Message sent successfully'}


def test_get_notifications(client):
	user = users_db['test@test.com']
	token = jwt.encode({'email': user.email}, 'secret', algorithm='HS256')
	response = client.get('/notifications', headers={'Authorization': token})
	assert response.status_code == 200
	assert 'notifications' in response.get_json()


def test_trending_topics(client):
	response = client.get('/trending')
	assert response.status_code == 200
	assert 'trending' in response.get_json()


def test_user_recommendations(client):
	response = client.get('/recommendations')
	assert response.status_code == 200
	assert 'recommendations' in response.get_json()
