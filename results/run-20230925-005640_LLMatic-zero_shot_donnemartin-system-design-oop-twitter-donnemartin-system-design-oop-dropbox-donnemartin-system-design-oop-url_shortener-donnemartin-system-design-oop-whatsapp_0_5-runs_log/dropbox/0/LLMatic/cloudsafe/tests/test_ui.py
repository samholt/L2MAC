import pytest
from flask import url_for


def test_index(client):
	response = client.get(url_for('index'))
	assert response.status_code == 200
	assert b'CloudSafe' in response.data


def test_dark_mode(client):
	response = client.get(url_for('toggle_dark_mode'))
	assert response.status_code == 200
	assert b'Dark mode enabled' in response.data


def test_light_mode(client):
	response = client.get(url_for('toggle_light_mode'))
	assert response.status_code == 200
	assert b'Light mode enabled' in response.data


def test_file_preview(client):
	response = client.get(url_for('preview_file', file_id=1))
	assert response.status_code == 200
	assert b'File preview' in response.data
