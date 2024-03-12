import pytest
import app
import datetime
from flask import json


def test_post_status():
	app.statuses = {}
	user_id = 'test_user'
	image = 'test_image'
	visibility = 'public'
	expiry_time = (datetime.datetime.now() + datetime.timedelta(hours=1)).isoformat()
	response = app.app.test_client().post('/post_status', data=json.dumps({'user_id': user_id, 'image': image, 'visibility': visibility, 'expiry_time': expiry_time}), content_type='application/json')
	assert response.status_code == 200
	assert 'message' in response.get_json()
	assert response.get_json()['message'] == 'Status posted.'
	assert user_id in app.statuses
	assert app.statuses[user_id][0]['image'] == image
	assert app.statuses[user_id][0]['visibility'] == visibility
	assert datetime.datetime.strptime(app.statuses[user_id][0]['expiry_time'], '%Y-%m-%dT%H:%M:%S.%f').isoformat() == expiry_time


def test_get_statuses():
	app.statuses = {}
	user_id = 'test_user'
	image = 'test_image'
	visibility = 'public'
	expiry_time = (datetime.datetime.now() + datetime.timedelta(hours=1)).isoformat()
	app.app.test_client().post('/post_status', data=json.dumps({'user_id': user_id, 'image': image, 'visibility': visibility, 'expiry_time': expiry_time}), content_type='application/json')
	response = app.app.test_client().get('/get_statuses', query_string={'user_id': user_id})
	assert response.status_code == 200
	assert len(response.get_json()) == 1
	assert response.get_json()[0]['image'] == image
	assert response.get_json()[0]['visibility'] == visibility
	assert datetime.datetime.strptime(response.get_json()[0]['expiry_time'], '%Y-%m-%dT%H:%M:%S.%f').isoformat() == expiry_time

