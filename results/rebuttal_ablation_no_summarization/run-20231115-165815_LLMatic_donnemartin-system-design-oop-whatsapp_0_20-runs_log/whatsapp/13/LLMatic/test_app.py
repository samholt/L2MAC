import pytest
from app import app, users
from flask import json

def test_signup():
	with app.test_client() as client:
		response = client.post('/signup', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
		data = json.loads(response.data)
		assert response.status_code == 201
		assert data['user_id'] == 1
		assert data['message'] == 'User created successfully'
		assert users[1]['username'] == 'test'
		assert users[1]['password'] == 'test'
		assert users[1]['blocked_contacts'] == []
		assert users[1]['groups'] == []
		assert users[1]['messages'] == []
		assert users[1]['statuses'] == []
		assert users[1]['online'] == False

		# Test with missing data
		response = client.post('/signup', data=json.dumps({'username': 'test'}), content_type='application/json')
		data = json.loads(response.data)
		assert response.status_code == 400
		assert data['message'] == 'Invalid request data'

def test_post_status():
	with app.test_client() as client:
		response = client.post('/post_status/1', data=json.dumps({'id': 1, 'image': 'status.jpg', 'caption': 'Hello, world!', 'visibility': 'public'}), content_type='application/json')
		data = json.loads(response.data)
		assert response.status_code == 200
		assert data['message'] == 'Status posted successfully'
		assert {'id': 1, 'image': 'status.jpg', 'caption': 'Hello, world!', 'visibility': 'public'} in users[1]['statuses']

		# Test with missing data
		response = client.post('/post_status/1', data=json.dumps({'id': 1, 'image': 'status.jpg', 'caption': 'Hello, world!'}), content_type='application/json')
		data = json.loads(response.data)
		assert response.status_code == 400
		assert data['message'] == 'Invalid request data'

def test_update_status_visibility():
	with app.test_client() as client:
		response = client.post('/update_status_visibility/1/1', data=json.dumps({'visibility': 'private'}), content_type='application/json')
		data = json.loads(response.data)
		assert response.status_code == 200
		assert data['message'] == 'Status visibility updated successfully'
		for status in users[1]['statuses']:
			if status['id'] == 1:
				assert status['visibility'] == 'private'

		# Test with missing data
		response = client.post('/update_status_visibility/1/1', data=json.dumps({}), content_type='application/json')
		data = json.loads(response.data)
		assert response.status_code == 400
		assert data['message'] == 'Invalid request data'

def test_update_online_status():
	with app.test_client() as client:
		response = client.post('/update_online_status/1', data=json.dumps({'status': True}), content_type='application/json')
		data = json.loads(response.data)
		assert response.status_code == 200
		assert data['message'] == 'Online status updated successfully'
		assert users[1]['online'] == True

		# Test with missing data
		response = client.post('/update_online_status/1', data=json.dumps({}), content_type='application/json')
		data = json.loads(response.data)
		assert response.status_code == 400
		assert data['message'] == 'Invalid request data'

def test_app_route():
	with app.test_client() as client:
		response = client.get('/app')
		assert response.status_code == 200
		assert response.data == b'<html><body><h1>Welcome to the Application!</h1></body></html>'
