import pytest
import app
import url_shortener
import analytics
import user_accounts
import admin_dashboard

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_redirect_to_url(client):
	short_url = url_shortener.generate_short_url('https://www.google.com')
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_shorten_url(client):
	response = client.post('/shorten_url', json={'url': 'https://www.google.com'})
	assert response.status_code == 200


def test_get_analytics(client):
	short_url = url_shortener.generate_short_url('https://www.google.com')
	response = client.get(f'/analytics/{short_url}')
	assert response.status_code == 200


def test_create_account(client):
	response = client.post('/create_account', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200


def test_monitor_system(client):
	response = client.get('/admin/monitor_system')
	assert response.status_code == 200
