import pytest
import json
from security import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_encrypt_decrypt(client):
	response = client.post('/encrypt', data=json.dumps({'file': 'test_file'}), content_type='application/json')
	assert response.status_code == 200
	assert 'encrypted_file' in response.get_json()

	response = client.post('/decrypt', data=json.dumps({'file': response.get_json()['encrypted_file']}), content_type='application/json')
	assert response.status_code == 200
	assert 'decrypted_file' in response.get_json()


def test_activity_log(client):
	response = client.get('/activity_log')
	assert response.status_code == 200
	assert 'activity_log' in response.get_json()
	assert len(response.get_json()['activity_log']) > 0
