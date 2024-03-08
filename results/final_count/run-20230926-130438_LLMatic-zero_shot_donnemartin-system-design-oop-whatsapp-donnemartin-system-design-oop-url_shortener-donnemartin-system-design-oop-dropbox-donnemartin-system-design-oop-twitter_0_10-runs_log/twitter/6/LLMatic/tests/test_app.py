import pytest
import app
import jwt

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'token' in response.get_json()


def test_edit_profile(client):
	token = jwt.encode({'username': 'test'}, app.app.config['SECRET_KEY'], algorithm='HS256')
	response = client.post('/edit_profile', json={'token': token, 'bio': 'test bio'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Profile updated successfully'}


def test_follow(client):
	token = jwt.encode({'username': 'test'}, app.app.config['SECRET_KEY'], algorithm='HS256')
	response = client.post('/follow', json={'token': token, 'follow_username': 'test2'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User followed successfully'}


def test_unfollow(client):
	token = jwt.encode({'username': 'test'}, app.app.config['SECRET_KEY'], algorithm='HS256')
	response = client.post('/unfollow', json={'token': token, 'unfollow_username': 'test2'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User unfollowed successfully'}


def test_create_post(client):
	token = jwt.encode({'username': 'test'}, app.app.config['SECRET_KEY'], algorithm='HS256')
	response = client.post('/create_post', json={'token': token, 'text': 'test post'})
	assert response.status_code == 201
	assert 'post_id' in response.get_json()


def test_delete_post(client):
	token = jwt.encode({'username': 'test'}, app.app.config['SECRET_KEY'], algorithm='HS256')
	response = client.delete('/delete_post', json={'token': token, 'post_id': 0})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post deleted successfully'}


def test_like_post(client):
	token = jwt.encode({'username': 'test'}, app.app.config['SECRET_KEY'], algorithm='HS256')
	response = client.post('/like_post', json={'token': token, 'post_id': 0})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post liked successfully'}


def test_retweet_post(client):
	token = jwt.encode({'username': 'test'}, app.app.config['SECRET_KEY'], algorithm='HS256')
	response = client.post('/retweet_post', json={'token': token, 'post_id': 0})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post retweeted successfully'}


def test_reply_post(client):
	token = jwt.encode({'username': 'test'}, app.app.config['SECRET_KEY'], algorithm='HS256')
	response = client.post('/reply_post', json={'token': token, 'post_id': 0, 'comment_text': 'test comment'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Comment added successfully'}


def test_search(client):
	response = client.post('/search', json={'query': 'test'})
	assert response.status_code == 200
	assert 'users' in response.get_json()
	assert 'posts' in response.get_json()


def test_send_message(client):
	token = jwt.encode({'username': 'test'}, app.app.config['SECRET_KEY'], algorithm='HS256')
	response = client.post('/send_message', json={'token': token, 'recipient': 'test2', 'text': 'test message'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Message sent successfully'}


def test_get_messages(client):
	token = jwt.encode({'username': 'test2'}, app.app.config['SECRET_KEY'], algorithm='HS256')
	response = client.post('/get_messages', json={'token': token})
	assert response.status_code == 200
	assert 'messages' in response.get_json()


def test_get_notifications(client):
	token = jwt.encode({'username': 'test'}, app.app.config['SECRET_KEY'], algorithm='HS256')
	response = client.post('/get_notifications', json={'token': token})
	assert response.status_code == 200
	assert 'notifications' in response.get_json()

