import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_post_status(client):
	response = client.post('/user', json={'email': 'test@example.com', 'password': 'test_password', 'online': True, 'queue': [], 'inbox': []})
	assert response.status_code == 201
	response = client.post('/user/test@example.com/status', json={'image': 'image_data', 'duration': 60, 'visibility': 'public'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Status posted successfully'}
	assert 'status' in app.users_db['test@example.com']
	assert app.users_db['test@example.com']['status'] == {'image': 'image_data', 'duration': 60, 'visibility': 'public'}


def test_offline_mode(client):
	response = client.post('/user', json={'email': 'test2@example.com', 'password': 'test_password', 'online': False, 'queue': [], 'inbox': []})
	assert response.status_code == 201
	response = client.post('/user/test2@example.com/status', json={'image': 'image_data', 'duration': 60, 'visibility': 'public'})
	assert response.status_code == 200
	assert 'status' not in app.users_db['test2@example.com']
	assert app.users_db['test2@example.com']['online'] == False
	assert len(app.users_db['test2@example.com']['queue']) == 1
