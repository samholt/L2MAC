import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		client.post('/signup', json={'email': 'test@test.com', 'password': 'test_password'})
		client.post('/signup', json={'email': 'test2@test.com', 'password': 'test_password2'})
		yield client


def test_send_image(client):
	response = client.post('/user/test@test.com/message/image', json={'recipient_email': 'test2@test.com', 'image': 'test_image'})
	assert response.status_code == 201
	assert json.loads(response.data)['message'] == 'Image sent'


def test_send_emoji(client):
	response = client.post('/user/test@test.com/message/emoji', json={'recipient_email': 'test2@test.com', 'emoji': 'test_emoji'})
	assert response.status_code == 201
	assert json.loads(response.data)['message'] == 'Emoji sent'


def test_send_gif(client):
	response = client.post('/user/test@test.com/message/gif', json={'recipient_email': 'test2@test.com', 'gif': 'test_gif'})
	assert response.status_code == 201
	assert json.loads(response.data)['message'] == 'GIF sent'


def test_send_sticker(client):
	response = client.post('/user/test@test.com/message/sticker', json={'recipient_email': 'test2@test.com', 'sticker': 'test_sticker'})
	assert response.status_code == 201
	assert json.loads(response.data)['message'] == 'Sticker sent'


def test_create_group(client):
	response = client.post('/user/test@test.com/group', json={'name': 'test_group', 'picture': 'test_picture'})
	assert response.status_code == 201
	assert json.loads(response.data)['message'] == 'Group created'


def test_assign_admin(client):
	client.post('/user/test@test.com/group', json={'name': 'test_group', 'picture': 'test_picture'})
	response = client.post('/user/test@test.com/group/1/assign_admin', json={'admins': ['test2@test.com']})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Admins assigned'


def test_remove_admin(client):
	client.post('/user/test@test.com/group', json={'name': 'test_group', 'picture': 'test_picture'})
	client.post('/user/test@test.com/group/1/assign_admin', json={'admins': ['test2@test.com']})
	response = client.post('/user/test@test.com/group/1/remove_admin', json={'admins': ['test2@test.com']})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Admins removed'


def test_set_permissions(client):
	client.post('/user/test@test.com/group', json={'name': 'test_group', 'picture': 'test_picture'})
	response = client.post('/user/test@test.com/group/1/set_permissions', json={'permissions': {'add_members': False, 'remove_members': False, 'assign_admins': False}})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Permissions set'

