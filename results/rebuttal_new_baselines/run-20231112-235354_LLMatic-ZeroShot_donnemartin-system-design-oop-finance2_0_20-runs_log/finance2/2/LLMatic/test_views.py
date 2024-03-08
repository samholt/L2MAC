import unittest
from flask import Flask
import app


def test_create_alert():
	with app.app.test_client() as client:
		response = client.post('/create_alert', json={'user_id': 'test', 'message': 'Budget limit nearing'})
		assert response.status_code == 201

	response = client.get('/get_user_alerts', query_string={'user_id': 'test'})
	assert response.status_code == 200
	assert 'Budget limit nearing' in response.get_json()['alerts'][0]['message']

