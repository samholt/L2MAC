import pytest
from app import app, db
from app.models import User, Url, Click

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_home_page(client):
	response = client.get('/')
	assert response.status_code == 200


def test_register_page(client):
	response = client.get('/register')
	assert response.status_code == 200


def test_login_page(client):
	response = client.get('/login')
	assert response.status_code == 200


def test_dashboard_page(client):
	response = client.get('/dashboard')
	assert response.status_code == 302
