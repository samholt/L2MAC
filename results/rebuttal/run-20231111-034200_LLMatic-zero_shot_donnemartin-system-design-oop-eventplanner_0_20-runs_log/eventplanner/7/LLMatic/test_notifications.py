import pytest
import notifications


def test_create_notification():
	response = notifications.app.test_client().post('/notifications', json={'user_id': '1', 'message': 'Test message'})
	assert response.status_code == 201
	assert notifications.notifications_db['1'] == 'Test message'


def test_get_notification():
	response = notifications.app.test_client().get('/notifications/1')
	assert response.status_code == 200
	assert response.get_json() == {'user_id': '1', 'message': 'Test message'}


def test_get_notification_not_found():
	response = notifications.app.test_client().get('/notifications/2')
	assert response.status_code == 404
	assert response.get_json() == {'error': 'Notification not found'}
