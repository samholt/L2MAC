import pytest
from app import app, users


def test_hello_world():
	with app.test_client() as client:
		response = client.get('/')
		assert response.status_code == 200

def test_users_dict():
	assert isinstance(users, dict)

def test_signup():
	with app.test_client() as client:
		response = client.post('/signup', json={'username': 'test', 'password': 'test'})
		assert response.status_code == 201
		user_id = response.get_json()['user_id']
		assert users[user_id] == {'username': 'test', 'password': 'test', 'blocked_contacts': [], 'groups': {}, 'messages': [], 'statuses': [], 'online': False}

def test_post_status():
	with app.test_client() as client:
		response = client.post('/signup', json={'username': 'test', 'password': 'test'})
		user_id = response.get_json()['user_id']
		response = client.post('/post_status', json={'user_id': user_id, 'status': 'Hello, world!'})
		assert response.status_code == 201
		status_id = response.get_json()['status_id']
		assert users[user_id]['statuses'][-1] == {'status_id': status_id, 'status': 'Hello, world!', 'timestamp': users[user_id]['statuses'][-1]['timestamp']}

def test_view_status():
	with app.test_client() as client:
		response = client.post('/signup', json={'username': 'test', 'password': 'test'})
		user_id = response.get_json()['user_id']
		response = client.post('/post_status', json={'user_id': user_id, 'status': 'Hello, world!'})
		status_id = response.get_json()['status_id']
		response = client.post('/view_status', json={'user_id': user_id, 'status_id': status_id})
		assert response.status_code == 200
		assert response.get_json() == {'status': 'Hello, world!'}

def test_update_status():
	with app.test_client() as client:
		response = client.post('/signup', json={'username': 'test', 'password': 'test'})
		user_id = response.get_json()['user_id']
		response = client.post('/update_status', json={'user_id': user_id, 'status': True})
		assert response.status_code == 200
		assert users[user_id]['online'] == True
		response = client.post('/update_status', json={'user_id': user_id, 'status': False})
		assert response.status_code == 200
		assert users[user_id]['online'] == False
