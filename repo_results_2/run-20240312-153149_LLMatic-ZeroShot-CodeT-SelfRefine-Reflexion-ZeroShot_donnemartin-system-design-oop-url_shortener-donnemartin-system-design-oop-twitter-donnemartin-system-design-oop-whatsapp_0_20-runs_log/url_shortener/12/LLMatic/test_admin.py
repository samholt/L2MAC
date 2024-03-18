import pytest
import json
from views import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

# Test admin routes

def test_admin_urls(client):
	response = client.get('/admin/urls')
	assert response.status_code == 200


def test_admin_delete_url(client):
	response = client.delete('/admin/delete_url/1')
	assert response.status_code == 200 or response.status_code == 404


def test_admin_delete_user(client):
	response = client.delete('/admin/delete_user/1')
	assert response.status_code == 200 or response.status_code == 404


def test_admin_analytics(client):
	response = client.get('/admin/analytics')
	assert response.status_code == 200
