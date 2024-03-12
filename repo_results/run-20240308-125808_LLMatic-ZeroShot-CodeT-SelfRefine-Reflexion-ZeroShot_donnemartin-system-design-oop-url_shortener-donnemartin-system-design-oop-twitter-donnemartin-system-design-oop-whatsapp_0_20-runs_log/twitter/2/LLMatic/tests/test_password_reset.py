import pytest
import json
from models import User
from views import users


def test_request_reset(client):
	user = User('test@test.com', 'test', 'test')
	users[user.email] = user
	response = client.post('/request-reset', data=json.dumps({'email': 'test@test.com'}), content_type='application/json')
	assert response.status_code == 200
	assert 'Password reset link sent' in response.get_data(as_text=True)


def test_reset_password(client):
	user = User('test@test.com', 'test', 'test')
	users[user.email] = user
	reset_token = user.get_reset_token()
	response = client.post('/reset-password', data=json.dumps({'token': reset_token, 'new_password': 'new_test'}), content_type='application/json')
	assert response.status_code == 200
	assert 'Password reset successful' in response.get_data(as_text=True)
	assert user.check_password('new_test')


def test_reset_password_invalid_token(client):
	response = client.post('/reset-password', data=json.dumps({'token': 'invalid', 'new_password': 'new_test'}), content_type='application/json')
	assert response.status_code == 400
	assert 'Invalid or expired token' in response.get_data(as_text=True)
