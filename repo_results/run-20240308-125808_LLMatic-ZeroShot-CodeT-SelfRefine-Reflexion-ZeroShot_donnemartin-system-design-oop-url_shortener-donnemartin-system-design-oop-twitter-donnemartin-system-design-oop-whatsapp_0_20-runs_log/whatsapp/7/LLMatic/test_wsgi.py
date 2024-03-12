import pytest
from werkzeug.test import Client
from app import app

@pytest.fixture(scope='module')
def client():
	return Client(app, response_wrapper=app.response_class)


def test_wsgi_server(client):
	response = client.get('/user/test@test.com')
	assert response.status_code == 200
	assert response.get_json()['email'] == 'test@test.com'
