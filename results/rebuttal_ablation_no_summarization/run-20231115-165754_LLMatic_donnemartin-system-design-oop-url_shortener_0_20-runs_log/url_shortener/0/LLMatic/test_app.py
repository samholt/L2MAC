import pytest
import app
from flask import json


def test_custom_short_url():
	app.app.testing = True
	client = app.app.test_client()

	# Register a user
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200

	# Login the user
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200

	# Shorten a URL with a custom short link
	response = client.post('/shorten_url', json={'url': 'https://www.google.com', 'custom_short_url': 'google', 'expiration_date': '2022-12-31T23:59:59'})
	assert response.status_code == 200
	assert json.loads(response.data)['short_url'] == 'short.ly/google'

	# Try to shorten another URL with the same custom short link
	response = client.post('/shorten_url', json={'url': 'https://www.yahoo.com', 'custom_short_url': 'google', 'expiration_date': '2022-12-31T23:59:59'})
	assert response.status_code == 200
	assert json.loads(response.data)['short_url'] != 'short.ly/google'

	# Logout the user
	response = client.get('/logout')
	assert response.status_code == 200


if __name__ == '__main__':
	pytest.main()
