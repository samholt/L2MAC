import pytest
from flask import url_for
from app import app, db
from app.models import User, File, SharedFile


@pytest.fixture
def client():
	app.config['TESTING'] = True
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
	with app.test_client() as client:
		yield client


def test_home(client):
	response = client.get('/')
	assert response.status_code == 302


def test_login(client):
	response = client.get('/login')
	assert response.status_code == 200


def test_logout(client):
	response = client.get('/logout')
	assert response.status_code == 302


def test_upload(client):
	response = client.post('/upload', data={'file': (BytesIO(b'my file contents'), 'my_file.txt')}, content_type='multipart/form-data')
	assert response.status_code == 302


def test_download(client):
	response = client.get('/download/1')
	assert response.status_code == 403


def test_share(client):
	response = client.post('/share/1', data={'username': 'test_user'})
	assert response.status_code == 404
