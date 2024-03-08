import pytest
from app import app, urls_db, URL
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.fixture(autouse=True)
def clear_db():
	urls_db.clear()

@pytest.mark.parametrize('original_url, custom_short_url, expiration_date', [
	('https://www.google.com', None, None),
	('https://www.google.com', 'custom', None),
	('https://www.google.com', None, (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')),
])
def test_shorten_url(client, original_url, custom_short_url, expiration_date):
	response = client.post('/shorten_url', json={'original_url': original_url, 'custom_short_url': custom_short_url, 'expiration_date': expiration_date})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()

	short_url = response.get_json()['short_url']
	assert urls_db[short_url].original_url == original_url
	assert urls_db[short_url].short_url == short_url
	assert urls_db[short_url].expiration_date == datetime.strptime(expiration_date, '%Y-%m-%d %H:%M:%S') if expiration_date else None

	response = client.get(f'/{short_url}')
	assert response.status_code == 302
	assert response.location == original_url

	if expiration_date:
		urls_db[short_url].expiration_date = datetime.now() - timedelta(minutes=1)
		response = client.get(f'/{short_url}')
		assert response.status_code == 410

	response = client.post('/shorten_url', json={'original_url': original_url, 'custom_short_url': short_url})
	assert response.status_code == 400
	assert 'error' in response.get_json()
	assert response.get_json()['error'] == 'Custom short URL already exists'
