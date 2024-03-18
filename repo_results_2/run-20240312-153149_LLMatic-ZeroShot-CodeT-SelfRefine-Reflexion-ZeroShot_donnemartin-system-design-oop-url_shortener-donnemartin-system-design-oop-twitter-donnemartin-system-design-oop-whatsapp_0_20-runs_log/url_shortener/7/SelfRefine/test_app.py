import pytest
import app

# Test URL validation function
def test_validate_url():
	assert app.validate_url('https://www.google.com') == True
	assert app.validate_url('invalid_url') == False

# Test URL shortening function
def test_shorten_url():
	short_url = app.shorten_url('https://www.google.com')
	assert len(short_url) == 5
	assert app.DB[short_url] == 'https://www.google.com'
	assert app.ANALYTICS[short_url] == 0

# Test URL redirection function
def test_redirect_to_url(client):
	response = client.get('/invalid_url')
	assert response.status_code == 404
	short_url = app.shorten_url('https://www.google.com')
	response = client.get('/' + short_url)
	assert response.status_code == 302
	assert response.location == 'https://www.google.com'
	assert app.ANALYTICS[short_url] == 1

# Test URL shortening endpoint
def test_url_shortening(client):
	response = client.post('/shorten', json={'url': 'invalid_url'})
	assert response.status_code == 400
	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()

# Test analytics endpoint
def test_get_analytics(client):
	short_url = app.shorten_url('https://www.google.com')
	response = client.get('/analytics')
	assert response.status_code == 200
	assert short_url in response.get_json()

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client
