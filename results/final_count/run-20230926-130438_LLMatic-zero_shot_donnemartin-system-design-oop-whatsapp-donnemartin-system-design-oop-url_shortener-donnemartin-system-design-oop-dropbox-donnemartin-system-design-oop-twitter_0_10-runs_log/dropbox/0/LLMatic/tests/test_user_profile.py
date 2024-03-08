import pytest
from routes.user_routes import user_routes
from services.user_service import UserService
from flask import Flask, json

app = Flask(__name__)
app.config['TESTING'] = True
app.register_blueprint(user_routes)

user_service = UserService()
app.config['user_service'] = user_service

@pytest.fixture
def client():
	with app.test_client() as client:
		app.config['user_service'].register_user('Test User', 'test@test.com', 'password')
		yield client


def test_get_profile(client):
	response = client.get('/users/profile/1')
	data = json.loads(response.data)
	assert response.status_code == 200
	assert data['id'] == 1
	assert data['name'] == 'Test User'
	assert data['email'] == 'test@test.com'


def test_get_profile_not_found(client):
	response = client.get('/users/profile/100')
	assert response.status_code == 404
