import pytest
from app import app, url_database


def test_redirect_to_url():
	with app.test_client() as c:
		url_database['test'] = {'url': 'http://example.com', 'expiration': None}
		response = c.get('/test')
		assert response.status_code == 302
		assert response.location == 'http://example.com'

		response = c.get('/nonexistent')
		assert response.status_code == 404

