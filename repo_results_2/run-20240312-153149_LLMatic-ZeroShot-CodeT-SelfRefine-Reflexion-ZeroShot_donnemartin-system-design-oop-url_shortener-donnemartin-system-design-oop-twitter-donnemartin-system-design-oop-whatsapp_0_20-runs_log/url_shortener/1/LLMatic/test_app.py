import pytest
from flask import Flask
from app import app as flask_app, shortener
from datetime import datetime, timedelta

@pytest.fixture
def app():
	return flask_app

@pytest.fixture
def client(app):
	return app.test_client()


def test_redirect(client):
	original_url = 'https://www.google.com'
	short_url = shortener.generate_short_url(original_url)
	response = client.get('/' + short_url)
	assert response.status_code == 302
	assert response.location == original_url


def test_redirect_not_found(client):
	response = client.get('/nonexistent')
	assert response.status_code == 404


def test_redirect_expired(client):
	original_url = 'https://www.google.com'
	short_url = shortener.generate_short_url(original_url, expiration_date=datetime.now() - timedelta(minutes=1))
	response = client.get('/' + short_url)
	assert response.status_code == 404


def test_redirect_invalid(client):
	response = client.get('/invalid')
	assert response.status_code == 404


def test_nonexistent_user(client):
	response = client.get('/user/nonexistent')
	assert response.status_code == 404
