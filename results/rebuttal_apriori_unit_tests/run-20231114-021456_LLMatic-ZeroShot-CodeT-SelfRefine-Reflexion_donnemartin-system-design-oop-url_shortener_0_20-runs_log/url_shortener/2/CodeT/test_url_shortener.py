import pytest
from random import randint, choices
import string
from datetime import datetime, timedelta
from url_shortener import app, DATABASE, generate_short_url, validate_url, check_expiration

# Helper Functions
def random_url():
	return f'https://example{randint(1000, 9999)}.com'

def random_username():
	return 'user' + ''.join(choices(string.ascii_lowercase + string.digits, k=5))

def random_slug():
	return ''.join(choices(string.ascii_lowercase + string.digits, k=8))

# Test Functions
class TestURLShorteningService:

	def setup_method(self):
		DATABASE['users'].clear()
		DATABASE['urls'].clear()

	def test_input_url_shortening(self):
		url = random_url()
		with app.test_client() as client:
			response = client.post('/shorten', json={'url': url})
			data = response.get_json()
			assert response.status_code == 200
			assert 'short_url' in data
			assert len(data['short_url']) < len(url)

	def test_url_validation(self):
		valid_url = random_url()
		invalid_url = 'htp:/invalid' + ''.join(choices(string.ascii_lowercase + string.digits, k=10))
		assert validate_url(valid_url) is True
		assert validate_url(invalid_url) is False

	def test_unique_shortened_url(self):
		url = random_url()
		with app.test_client() as client:
			response1 = client.post('/shorten', json={'url': url})
			response2 = client.post('/shorten', json={'url': url})
			data1 = response1.get_json()
			data2 = response2.get_json()
			assert data1['short_url'] != data2['short_url']

	def test_custom_short_link(self):
		url = random_url()
		custom_slug = random_slug()
		with app.test_client() as client:
			response = client.post('/shorten', json={'url': url, 'custom_slug': custom_slug})
			data = response.get_json()
			assert data['short_url'] == custom_slug

	def test_redirection(self):
		original_url = random_url()
		with app.test_client() as client:
			response = client.post('/shorten', json={'url': original_url})
			data = response.get_json()
			short_url = data['short_url']
			redirect_response = client.get(f'/{short_url}')
			assert redirect_response.status_code == 302
			assert redirect_response.location == original_url

	def test_url_expiration(self):
		url = random_url()
		expiration_time = (datetime.now() + timedelta(minutes=randint(1, 60))).isoformat()
		with app.test_client() as client:
			response = client.post('/shorten', json={'url': url, 'expiration_time': expiration_time})
			data = response.get_json()
			short_url = data['short_url']
			assert check_expiration(short_url) is False
