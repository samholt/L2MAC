import pytest
from flask import Flask, json
from app import app as flask_app


def test_shorten_url():
	response = flask_app.test_client().post('/shorten_url',
		data=json.dumps({'original_url': 'https://www.google.com'}),
		content_type='application/json',
	)
	data = json.loads(response.get_data(as_text=True))
	assert response.status_code == 201
	assert 'short_url' in data


def test_redirect_to_url():
	response = flask_app.test_client().get('/nonexistent_url')
	assert response.status_code == 404


def test_get_stats():
	response = flask_app.test_client().get('/stats/nonexistent_url')
	assert response.status_code == 404


def test_delete_expired_urls():
	response = flask_app.test_client().delete('/delete_expired_urls')
	assert response.status_code == 200

