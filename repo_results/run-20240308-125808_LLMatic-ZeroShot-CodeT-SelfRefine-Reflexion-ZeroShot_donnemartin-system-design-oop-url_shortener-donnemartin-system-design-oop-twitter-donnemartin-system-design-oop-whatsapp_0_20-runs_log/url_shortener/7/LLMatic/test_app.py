import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_home_page(client):
	response = client.get('/')
	assert response.status_code == 200


def test_redirect_to_original_url(client):
	short_url = app.generate_short_url('https://www.google.com')
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_view_all_urls(client):
	response = client.get('/admin/urls')
	assert response.status_code == 200


def test_delete_url(client):
	short_url = app.generate_short_url('https://www.google.com')
	response = client.get(f'/admin/delete_url/{short_url}')
	assert response.status_code == 200


def test_delete_user(client):
	username = 'test_user'
	app.user_account.create_account(username, 'password')
	response = client.get(f'/admin/delete_user/{username}')
	assert response.status_code == 200


def test_view_analytics(client):
	response = client.get('/admin/analytics')
	assert response.status_code == 200
