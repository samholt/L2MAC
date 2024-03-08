import pytest
import app
import uuid

# existing tests...

def test_send_message():
	with app.app.test_client() as c:
		response = c.post('/send_message', json={'sender_id': 'user1', 'recipient_id': 'user2', 'content': 'Hello, user2!'})
		assert response.status_code == 200
		assert 'message_id' in response.get_json()

		message_id = response.get_json()['message_id']
		response = c.get('/receive_messages', query_string={'user_id': 'user2'})
		assert response.status_code == 200
		assert 'messages' in response.get_json()
		assert message_id in response.get_json()['messages']
