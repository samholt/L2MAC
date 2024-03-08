import pytest
from flask import Flask
from cloudsafe.app.security_controller import security_blueprint

@pytest.fixture
def client():
	app = Flask(__name__)
	app.register_blueprint(security_blueprint)
	client = app.test_client()
	return client

def test_encrypt_file(client):
	response = client.post('/encrypt', data={'file': (open('test_file.txt', 'rb'), 'test_file.txt')})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'File encrypted successfully'

def test_decrypt_file(client):
	response = client.post('/decrypt', data={'file': (open('test_file.txt', 'rb'), 'test_file.txt')})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'File decrypted successfully'

def test_get_activity_log(client):
	response = client.get('/log', query_string={'user_id': 1})
	assert response.status_code == 200
	assert 'logs' in response.get_json()
