import pytest
from flask import url_for
from app.app import app, db

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_signup_page(client):
	response = client.get(url_for('routes.signup'))
	assert response.status_code == 200
	assert b'Signup' in response.data


def test_login_page(client):
	response = client.get(url_for('routes.login'))
	assert response.status_code == 200
	assert b'Login' in response.data


def test_chat_page(client):
	response = client.get(url_for('routes.index'))
	assert response.status_code == 200
	assert b'Chat' in response.data


def test_group_page(client):
	response = client.get(url_for('routes.group'))
	assert response.status_code == 200
	assert b'Group' in response.data


def test_status_page(client):
	response = client.get(url_for('routes.status'))
	assert response.status_code == 200
	assert b'Status' in response.data
