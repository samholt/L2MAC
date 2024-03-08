import pytest
from app import app
from models import User, URL, Click


def test_url_expiration():
	with app.test_client() as client:
		# Create a URL with an expiration date in the past
		response = client.post('/shorten', data={'original_url': 'https://www.google.com', 'custom': 'google', 'expiration_date': '2000-01-01'})
		assert response.status_code == 200
		assert response.data == b'URL shortened successfully'

		# Try to access the expired URL
		response = client.get('/google')
		assert response.status_code == 200
		assert response.data == b'URL expired'

