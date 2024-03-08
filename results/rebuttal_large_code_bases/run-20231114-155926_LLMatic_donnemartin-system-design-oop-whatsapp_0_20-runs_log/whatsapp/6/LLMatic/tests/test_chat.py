import pytest
from app import create_app, db
from app.models import User, Message

@pytest.fixture
def client():
	app = create_app('testing')
	app.config['TESTING'] = True

	with app.app_context():
		with app.test_client() as client:
			yield client


def test_send_message(client):
	response = client.post('/chat/send', json={'from': 'user1', 'to': 'user2', 'content': 'Hello'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Message sent'}


def test_receive_message(client):
	response = client.get('/chat/receive', query_string={'user_id': 'user2'})
	assert response.status_code == 200
	assert 'Hello' in response.get_json()['messages']


def test_view_history(client):
	response = client.get('/chat/history', query_string={'user_id': 'user1'})
	assert response.status_code == 200
	assert 'Hello' in response.get_json()['sent_messages']
	assert 'Hello' not in response.get_json()['received_messages']
