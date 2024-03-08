import pytest
from flask import url_for
from app import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	app.config['SERVER_NAME'] = 'localhost'
	with app.test_client() as client:
		yield client


def test_home(client):
	with app.app_context():
		response = client.get(url_for('home'))
		assert response.status_code == 200


def test_profile(client):
	with app.app_context():
		response = client.get(url_for('profile'))
		assert response.status_code == 200


def test_contacts(client):
	with app.app_context():
		response = client.get(url_for('contacts'))
		assert response.status_code == 200


def test_messaging(client):
	with app.app_context():
		response = client.get(url_for('messaging'))
		assert response.status_code == 200


def test_group_chat(client):
	with app.app_context():
		response = client.get(url_for('group_chat'))
		assert response.status_code == 200


def test_status(client):
	with app.app_context():
		response = client.get(url_for('status'))
		assert response.status_code == 200
