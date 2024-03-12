import pytest
import app
import url_shortener as us

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_home(client):
	response = client.get('/')
	assert response.status_code == 200


def test_redirect_to_url(client):
	short_url = us.generate_short_url('https://www.google.com')
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	assert response.status_code == 200


def test_get_analytics(client):
	short_url = us.generate_short_url('https://www.google.com')
	response = client.get(f'/analytics/{short_url}')
	assert response.status_code == 200


def test_create_user(client):
	response = client.post('/user', json={'username': 'testuser'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Account created successfully.'


def test_get_all_urls(client):
	response = client.get('/admin/urls')
	assert response.status_code == 200
