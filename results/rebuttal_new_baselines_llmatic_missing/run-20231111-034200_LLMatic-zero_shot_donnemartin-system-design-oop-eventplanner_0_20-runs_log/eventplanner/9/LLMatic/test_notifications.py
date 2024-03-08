import pytest
import notifications
from flask import json


def test_create_notification():
	with notifications.app.test_client() as c:
		resp = c.post('/notifications', json={'user_id': '1', 'event_id': '1', 'message': 'Event reminder'})
		assert resp.status_code == 201
		data = json.loads(resp.data)
		assert data['status'] == 'Notification created'


def test_get_notifications():
	with notifications.app.test_client() as c:
		resp = c.get('/notifications/1')
		data = json.loads(resp.data)
		assert 'event_id' in data
		assert 'message' in data
		assert 'time' in data
