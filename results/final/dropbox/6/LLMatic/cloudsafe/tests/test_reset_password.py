import pytest
import json
from werkzeug.security import check_password_hash
from app import app, users_db, serializer
from app.models import User

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.fixture
def init_database():
	users_db.clear()
	user = User(
		id=1,
		name='Test User',
		email='test@example.com',
		password='test_password',
		profile_picture='',
		storage_used=0
	)
	users_db[user.id] = user

	return user


def test_reset_password(client, init_database):
	user = init_database
	token = serializer.dumps(user.email, salt='password-reset-salt')
	response = client.post('/reset-password', data=json.dumps({'token': token, 'new_password': 'new_password'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Password reset successful'
	assert check_password_hash(user.password, 'new_password')

	response = client.post('/reset-password', data=json.dumps({'token': 'invalid_token', 'new_password': 'new_password'}), content_type='application/json')
	assert response.status_code == 400
	assert response.get_json()['message'] == 'Invalid or expired token'
