import pytest
from cloudsafe.app.models import User, Activity, File
from cloudsafe.app import db


def test_change_password(client, auth):
	auth.register()
	auth.login()
	response = client.post('/change-password', json={'old_password': 'test', 'new_password': 'new_test'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Password changed successfully'

	user = User.query.filter_by(username='test').first()
	assert user.check_password('new_test')


def test_activity(client, auth):
	auth.register()
	auth.login()
	user = User.query.filter_by(username='test').first()
	activity = Activity(action='uploaded', target='test.txt', user=user)
	db.session.add(activity)
	db.session.commit()

	response = client.get('/activity')
	assert response.status_code == 200
	assert response.get_json()[0]['action'] == 'uploaded'
	assert response.get_json()[0]['target'] == 'test.txt'

def test_share_link(client, auth):
	auth.register()
	auth.login()
	user = User.query.filter_by(username='test').first()
	file = File(name='test.txt', user=user)
	db.session.add(file)
	db.session.commit()

	response = client.post('/share', json={'file_id': file.id})
	assert response.status_code == 200
	assert 'link' in response.get_json()

