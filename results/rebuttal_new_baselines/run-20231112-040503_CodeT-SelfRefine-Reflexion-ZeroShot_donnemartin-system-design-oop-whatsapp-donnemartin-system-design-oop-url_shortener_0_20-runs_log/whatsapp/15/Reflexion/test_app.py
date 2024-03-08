import pytest
import app
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.mark.parametrize('user', [
	{'id': '1', 'email': 'test1@test.com', 'password': 'password1', 'profile_picture': '', 'status_message': '', 'last_seen': datetime.datetime.now(), 'blocked_users': [], 'groups': []},
	{'id': '2', 'email': 'test2@test.com', 'password': 'password2', 'profile_picture': '', 'status_message': '', 'last_seen': datetime.datetime.now(), 'blocked_users': [], 'groups': []}
])
def test_signup(client, user):
	response = client.post('/signup', json=user)
	assert response.status_code == 201
	assert response.get_json()['message'] == 'User created successfully'

@pytest.mark.parametrize('chat', [
	{'id': '1', 'users': ['1'], 'messages': []},
	{'id': '2', 'users': ['1', '2'], 'messages': []}
])
def test_create_chat(client, chat):
	response = client.post('/create_chat', json=chat)
	assert response.status_code == 201
	assert response.get_json()['message'] == 'Chat created successfully'

@pytest.mark.parametrize('message', [
	{'chat_id': '1', 'message': 'Hello, world!'},
	{'chat_id': '2', 'message': 'Hello, everyone!'}
])
def test_send_message(client, message):
	response = client.post('/send_message', json=message)
	assert response.status_code == 201
	assert response.get_json()['message'] == 'Message sent successfully'

@pytest.mark.parametrize('chat_id', ['1', '2'])
def test_view_messages(client, chat_id):
	response = client.get(f'/view_messages?chat_id={chat_id}')
	assert response.status_code == 200
	assert 'messages' in response.get_json()
