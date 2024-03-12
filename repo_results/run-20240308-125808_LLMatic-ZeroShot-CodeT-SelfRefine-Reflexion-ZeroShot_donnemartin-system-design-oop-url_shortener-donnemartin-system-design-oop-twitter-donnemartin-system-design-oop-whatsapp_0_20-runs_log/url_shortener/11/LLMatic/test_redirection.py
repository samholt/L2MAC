import pytest
from flask import Flask
from url_shortener import DATABASE
from app import app as flask_app

@pytest.fixture
def app():
	return flask_app

@pytest.fixture
def client(app):
	return app.test_client()


def test_redirection(client):
	DATABASE['http://example.com'] = 'exmpl'
	response = client.get('/exmpl')
	assert response.status_code == 302
	assert response.location == 'http://example.com'

	response = client.get('/notfound')
	assert response.status_code == 404
