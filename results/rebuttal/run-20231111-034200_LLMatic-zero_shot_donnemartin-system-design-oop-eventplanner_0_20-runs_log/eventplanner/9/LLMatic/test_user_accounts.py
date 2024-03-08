import json
from datetime import datetime, timedelta
from user_accounts import app


def test_create_profile():
	with app.test_client() as client:
		response = client.post('/create_profile', json={'name': 'Test User', 'email': 'test@example.com'})
		assert response.status_code == 201
		assert 'id' in response.get_json()


def test_customize_profile():
	with app.test_client() as client:
		response = client.post('/create_profile', json={'name': 'Test User', 'email': 'test@example.com'})
		id = response.get_json()['id']
		response = client.put(f'/customize_profile/{id}', json={'name': 'Updated User'})
		assert response.status_code == 204


def test_get_profile():
	with app.test_client() as client:
		response = client.post('/create_profile', json={'name': 'Test User', 'email': 'test@example.com'})
		id = response.get_json()['id']
		response = client.get(f'/get_profile/{id}')
		assert response.status_code == 200
		assert response.get_json()['name'] == 'Test User'


def test_get_events():
	with app.test_client() as client:
		response = client.post('/create_profile', json={'name': 'Test User', 'email': 'test@example.com'})
		user_id = response.get_json()['id']
		client.post('/create_event', json={'name': 'Past Event', 'date': (datetime.now() - timedelta(days=1)).replace(microsecond=0).isoformat(), 'user_id': user_id})
		client.post('/create_event', json={'name': 'Upcoming Event', 'date': (datetime.now() + timedelta(days=1)).replace(microsecond=0).isoformat(), 'user_id': user_id})
		response = client.get(f'/get_events/{user_id}')
		assert response.status_code == 200
		assert 'Past Event' in [event['name'] for event in response.get_json()['past_events']]
		assert 'Upcoming Event' in [event['name'] for event in response.get_json()['upcoming_events']]

