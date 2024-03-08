import pytest
from flask import Flask
from cloudsafe.app.sharing_controller import sharing

@pytest.fixture

def client():
	app = Flask(__name__)
	app.register_blueprint(sharing)
	client = app.test_client()
	return client

def test_generate_share_link(client):
	response = client.post('/generate_share_link', json={'id': '1', 'file_id': '1'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Share link generated successfully'}

def test_set_expiry_date(client):
	response = client.put('/set_expiry_date', json={'id': '1', 'days': 7})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Expiry date set successfully'}

def test_set_password(client):
	response = client.put('/set_password', json={'id': '1', 'password': 'password'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Password set successfully'}

def test_invite_user(client):
	response = client.post('/invite_user', json={'id': '1', 'folder_id': '1', 'user_id': '1', 'permissions': 'read'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User invited successfully'}

def test_set_permissions(client):
	response = client.put('/set_permissions', json={'id': '1', 'permissions': 'write'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Permissions set successfully'}
