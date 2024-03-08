import pytest
from flask import url_for


def test_register_template(client):
	response = client.get(url_for('routes.register'))
	assert response.status_code == 200
	assert b'Register' in response.data


def test_login_template(client):
	response = client.get(url_for('routes.login'))
	assert response.status_code == 200
	assert b'Login' in response.data


def test_profile_template(client):
	response = client.get(url_for('routes.profile'))
	assert response.status_code == 200
	assert b'Profile' in response.data


def test_upload_template(client):
	response = client.get(url_for('file_routes.upload'))
	assert response.status_code == 200
	assert b'Upload' in response.data


def test_download_template(client):
	response = client.get(url_for('file_routes.download'))
	assert response.status_code == 200
	assert b'Download' in response.data


def test_organize_template(client):
	response = client.get(url_for('file_routes.organize'))
	assert response.status_code == 200
	assert b'Organize' in response.data


def test_versioning_template(client):
	response = client.get(url_for('file_routes.versioning'))
	assert response.status_code == 200
	assert b'Versioning' in response.data


def test_share_template(client):
	response = client.get(url_for('share_routes.share'))
	assert response.status_code == 200
	assert b'Share' in response.data


def test_activity_log_template(client):
	response = client.get(url_for('routes.activity'))
	assert response.status_code == 200
	assert b'Activity Log' in response.data
