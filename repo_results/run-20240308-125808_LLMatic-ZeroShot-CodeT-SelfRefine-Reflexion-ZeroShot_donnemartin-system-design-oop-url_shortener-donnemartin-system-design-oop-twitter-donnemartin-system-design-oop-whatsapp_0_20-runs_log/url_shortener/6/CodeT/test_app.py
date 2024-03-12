import pytest
import app
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def reset_db():
	app.DB = {
		'users': {},
		'urls': {},
		'clicks': {}
	}

def test_shorten_url(client, reset_db):
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com'})
	assert response.status_code == 201
	assert 'short_url' in response.get_json()

	short_url = response.get_json()['short_url']
	assert short_url in app.DB['urls']
	assert app.DB['urls'][short_url].original_url == 'https://www.google.com'

	response = client.get(f'/{short_url}')
	assert response.status_code == 302
	assert response.location == 'https://www.google.com'

	app.DB['urls'][short_url].expiration_date = datetime.datetime.now() - datetime.timedelta(days=1)
	response = client.get(f'/{short_url}')
	assert response.status_code == 410
