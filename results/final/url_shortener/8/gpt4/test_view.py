from view import app
import pytest


def test_view():
	with app.test_client() as client:
		response = client.post('/create', data={'original_url': 'https://www.google.com'})
		assert response.status_code == 200
		short_url = response.get_json()['short_url']
		response = client.get(f'/{short_url}')
		assert response.status_code == 302
		response = client.delete('/delete_expired')
		assert response.status_code == 200
		assert response.get_json()['status'] == 'success'

