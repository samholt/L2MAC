import pytest
from flask import url_for
from main import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		with app.app_context():
			yield client

def test_home(client):
	response = client.get(url_for('home'))
	assert response.status_code == 200

def test_login(client):
	response = client.get(url_for('login'))
	assert response.status_code == 200

def test_register(client):
	response = client.get(url_for('register'))
	assert response.status_code == 200

def test_contacts(client):
	response = client.get(url_for('contacts'))
	assert response.status_code == 200

def test_messages(client):
	response = client.get(url_for('messages'))
	assert response.status_code == 200

def test_groups(client):
	response = client.get(url_for('groups'))
	assert response.status_code == 200

def test_status(client):
	response = client.get(url_for('status_view'))
	assert response.status_code == 200
