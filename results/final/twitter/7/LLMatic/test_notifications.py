import pytest
from notifications import app
from database import users_db, notifications_db

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_notify(client):
	# Test notification creation
	response = client.post('/notify', json={'user_email': 'test@test.com', 'content': 'Test notification', 'type': 'like', 'timestamp': '2022-01-01T00:00:00Z'})
	assert response.status_code == 201
	assert notifications_db.get('test@test.com')

	# Test getting notifications
	response = client.get('/get_notifications', query_string={'user_email': 'test@test.com'})
	assert response.status_code == 200
	assert response.get_json()['notifications']

	# Test getting notifications for non-existent user
	response = client.get('/get_notifications', query_string={'user_email': 'nonexistent@test.com'})
	assert response.status_code == 404
