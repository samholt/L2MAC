import pytest
from flask import json
from app import create_app
from models import db, User


@pytest.fixture
def client():
	app = create_app()
	app.config['TESTING'] = True
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
	with app.test_client() as client:
		with app.app_context():
			db.create_all()
			yield client
			db.drop_all()


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201


def test_login(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200


def test_edit_profile(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	login_response = client.post('/login', json={'username': 'test', 'password': 'test'})
	access_token = json.loads(login_response.data)['access_token']
	response = client.put('/edit_profile', headers={'Authorization': f'Bearer {access_token}'}, json={'profile_picture': 'test.jpg', 'bio': 'test bio', 'website_link': 'test.com', 'location': 'test location'})
	assert response.status_code == 200


def test_toggle_visibility(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	login_response = client.post('/login', json={'username': 'test', 'password': 'test'})
	access_token = json.loads(login_response.data)['access_token']
	response = client.put('/toggle_visibility', headers={'Authorization': f'Bearer {access_token}'})
	assert response.status_code == 200
