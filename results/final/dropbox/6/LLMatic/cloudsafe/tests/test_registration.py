import pytest
import json
from app import app, users_db


def test_register():
	with app.test_client() as client:
		response = client.post(
			'/register',
			data=json.dumps({'name': 'Test User', 'email': 'test@example.com', 'password': 'test123'}),
			content_type='application/json',
		)
		data = json.loads(response.data)
		assert response.status_code == 201
		assert data['message'] == 'User registered successfully'
		assert 'user_id' in data
		assert users_db[data['user_id']].email == 'test@example.com'
