import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_signup(client):
	response = client.post('/signup', data={'email': 'test_user', 'password': 'test_password'})
	assert response.status_code == 200
	assert 'Sign In' in response.get_data(as_text=True)


def test_signin(client):
	app.DATABASE['users']['test_user'] = 'test_password'
	response = client.post('/signin', data={'email': 'test_user', 'password': 'test_password'})
	assert response.status_code == 200
	assert 'Profile' in response.get_data(as_text=True)


def test_profile(client):
	app.DATABASE['users']['test_user'] = 'test_password'
	response = client.get('/profile/test_user')
	assert response.status_code == 200
	assert 'Profile' in response.get_data(as_text=True)


def test_contacts(client):
	app.DATABASE['users']['test_user'] = 'test_password'
	response = client.get('/contacts/test_user')
	assert response.status_code == 200
	assert 'Contacts' in response.get_data(as_text=True)


def test_messages(client):
	app.DATABASE['users']['test_user'] = 'test_password'
	response = client.get('/messages/test_user')
	assert response.status_code == 200
	assert 'Messages' in response.get_data(as_text=True)


def test_groups(client):
	app.DATABASE['users']['test_user'] = 'test_password'
	response = client.get('/groups/test_user')
	assert response.status_code == 200
	assert 'Groups' in response.get_data(as_text=True)


def test_statuses(client):
	app.DATABASE['users']['test_user'] = 'test_password'
	response = client.get('/statuses/test_user')
	assert response.status_code == 200
	assert 'Statuses' in response.get_data(as_text=True)


def test_update_status(client):
	app.DATABASE['users']['test_user'] = 'test_password'
	response = client.post('/update_status/test_user', data={'status': 'online'})
	assert response.status_code == 200
	assert 'Status updated successfully' in response.get_data(as_text=True)
	assert app.DATABASE['user_status']['test_user'] == 'online'


def test_send_message(client):
	app.DATABASE['users']['test_user'] = 'test_password'
	app.DATABASE['users']['test_receiver'] = 'test_password'
	app.DATABASE['user_status']['test_receiver'] = 'offline'
	app.DATABASE['message_queue']['test_receiver'] = []
	response = client.post('/send_message', data={'email': 'test_user', 'receiver': 'test_receiver', 'message': 'Hello'})
	assert response.status_code == 200
	assert 'Message sent successfully' in response.get_data(as_text=True)
	assert len(app.DATABASE['message_queue']['test_receiver']) == 1
