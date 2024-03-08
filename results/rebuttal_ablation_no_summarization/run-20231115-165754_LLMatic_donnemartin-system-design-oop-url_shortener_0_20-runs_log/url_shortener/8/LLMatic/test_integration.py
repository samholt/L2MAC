import pytest
from unittest.mock import patch, MagicMock
from app import app, url_db, user_db
from datetime import datetime, timedelta


def test_workflow():
	with app.test_client() as c:
		# Test user registration
		response = c.post('/register', json={'username': 'test', 'password': 'test'})
		assert response.status_code == 200
		assert 'test' in user_db

		# Test user login
		response = c.post('/login', json={'username': 'test', 'password': 'test'})
		assert response.status_code == 200

		# Test URL shortening
		response = c.post('/shorten_url', json={'username': 'test', 'url': 'https://www.google.com', 'expiration_date': (datetime.now() + timedelta(days=1)).isoformat()})
		assert response.status_code == 200
		shortened_url = response.get_json()['shortened_url']
		assert url_db[shortened_url]['url'] == 'https://www.google.com'
		assert shortened_url in user_db['test']['urls']

		# Test URL redirection
		response = c.get('/' + shortened_url)
		assert response.status_code == 302
		assert response.location == 'https://www.google.com'
		assert len(url_db[shortened_url]['clicks']) == 1
		assert 'timestamp' in url_db[shortened_url]['clicks'][0]

		# Test analytics
		response = c.get('/analytics/test')
		assert response.status_code == 200
		assert response.get_json() == {shortened_url: url_db[shortened_url]['clicks']}

		# Test URL deletion
		response = c.post('/delete_url', json={'username': 'test', 'short_url': shortened_url})
		assert response.status_code == 200
		assert shortened_url not in url_db
		assert shortened_url not in user_db['test']['urls']

if __name__ == '__main__':
	pytest.main()

