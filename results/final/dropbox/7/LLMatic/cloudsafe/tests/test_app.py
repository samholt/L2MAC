import pytest
from cloudsafe import app

@pytest.fixture

def client():
	app.app.config['TESTING'] = True

	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.get('/register')
	assert response.status_code == 200


def test_login(client):
	response = client.get('/login')
	assert response.status_code == 200


def test_profile(client):
	response = client.get('/profile')
	assert response.status_code == 200


def test_upload(client):
	response = client.get('/upload')
	assert response.status_code == 200


def test_download(client):
	response = client.get('/download')
	assert response.status_code == 200


def test_organize(client):
	response = client.get('/organize')
	assert response.status_code == 200


def test_version(client):
	response = client.get('/version')
	assert response.status_code == 200


def test_share(client):
	response = client.get('/share')
	assert response.status_code == 200


def test_invite(client):
	response = client.get('/invite')
	assert response.status_code == 200


def test_log(client):
	response = client.get('/log')
	assert response.status_code == 200
