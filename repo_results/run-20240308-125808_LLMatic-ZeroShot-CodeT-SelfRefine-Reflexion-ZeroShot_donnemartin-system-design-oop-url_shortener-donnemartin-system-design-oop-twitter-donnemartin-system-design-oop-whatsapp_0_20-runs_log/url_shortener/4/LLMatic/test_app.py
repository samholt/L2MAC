import pytest
from flask import Flask
from app import app as flask_app
import url_shortener as us

@pytest.fixture
def app():
	return flask_app


def test_home_page(client):
	response = client.get('/')
	assert response.status_code == 200
	assert response.data == b'Hello, World!'


def test_redirect(client):
	short_url = us.generate_short_url('https://www.google.com')
	response = client.get('/' + short_url)
	assert response.status_code == 302


def test_404(client):
	response = client.get('/non_existent_url')
	assert response.status_code == 404
	
	expired_url = us.generate_short_url('https://www.google.com', expiration_minutes=-1)
	response = client.get('/' + expired_url)
	assert response.status_code == 404

