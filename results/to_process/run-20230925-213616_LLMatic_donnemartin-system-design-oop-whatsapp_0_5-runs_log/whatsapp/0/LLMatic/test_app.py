import pytest
import app
import json


def test_register():
	with app.app.test_client() as c:
		response = c.post('/register', json={'email': 'test@test.com', 'password': 'test'})
		assert response.status_code == 201
		assert json.loads(response.data)['email'] == 'test@test.com'


def test_recover():
	with app.app.test_client() as c:
		response = c.post('/recover', json={'email': 'test@test.com'})
		assert response.status_code == 200
		assert json.loads(response.data)['password'] == 'test'


def test_profile_picture():
	with app.app.test_client() as c:
		response = c.post('/profile_picture', json={'email': 'test@test.com', 'picture': 'test.jpg'})
		assert response.status_code == 200
		assert json.loads(response.data)['message'] == 'Profile picture set.'


def test_status_message():
	with app.app.test_client() as c:
		response = c.post('/status_message', json={'email': 'test@test.com', 'message': 'Hello, world!'})
		assert response.status_code == 200
		assert json.loads(response.data)['message'] == 'Status message set.'


def test_privacy_settings():
	with app.app.test_client() as c:
		response = c.post('/privacy_settings', json={'email': 'test@test.com', 'settings': {'private': True}})
		assert response.status_code == 200
		assert json.loads(response.data)['message'] == 'Privacy settings set.'


def test_block_unblock():
	with app.app.test_client() as c:
		response = c.post('/block_unblock', json={'user_email': 'test@test.com', 'contact_email': 'contact@test.com'})
		assert response.status_code == 200
		assert json.loads(response.data)['message'] == 'Contact blocked/unblocked.'


def test_create_group():
	with app.app.test_client() as c:
		response = c.post('/create_group', json={'group_name': 'Test Group', 'user_email': 'test@test.com'})
		assert response.status_code == 201
		assert json.loads(response.data)['message'] == 'Group created.'


def test_edit_group():
	with app.app.test_client() as c:
		response = c.post('/edit_group', json={'group_name': 'Test Group', 'user_email': 'test2@test.com', 'action': 'add'})
		assert response.status_code == 200
		assert json.loads(response.data)['message'] == 'Group edited.'


def test_send_message():
	with app.app.test_client() as c:
		response = c.post('/send_message', json={'sender': 'test@test.com', 'recipient': 'test2@test.com', 'content': 'Hello, world!'})
		assert response.status_code == 201
		assert json.loads(response.data)['message'] == 'Message sent.'


def test_read_message():
	with app.app.test_client() as c:
		response = c.post('/read_message', json={'sender': 'test@test.com', 'recipient': 'test2@test.com'})
		assert response.status_code == 200
		assert json.loads(response.data)['content'] == 'Hello, world!'


def test_update_read_receipt():
	with app.app.test_client() as c:
		response = c.post('/update_read_receipt', json={'sender': 'test@test.com', 'recipient': 'test2@test.com'})
		assert response.status_code == 200
		assert json.loads(response.data)['message'] == 'Read receipt updated.'


def test_encrypt_message():
	with app.app.test_client() as c:
		response = c.post('/encrypt_message', json={'sender': 'test@test.com', 'recipient': 'test2@test.com'})
		assert response.status_code == 200
		assert json.loads(response.data)['message'] == 'Message encrypted.'


def test_share_image():
	with app.app.test_client() as c:
		response = c.post('/share_image', json={'sender': 'test@test.com', 'recipient': 'test2@test.com', 'image_content': 'test.jpg'})
		assert response.status_code == 201
		assert json.loads(response.data)['message'] == 'Image shared.'


def test_create_group_chat():
	with app.app.test_client() as c:
		response = c.post('/create_group_chat', json={'name': 'Test Group Chat', 'participants': ['test@test.com', 'test2@test.com']})
		assert response.status_code == 201
		assert json.loads(response.data)['message'] == 'Group chat created.'


def test_add_participant():
	with app.app.test_client() as c:
		response = c.post('/add_participant', json={'group_chat': 'Test Group Chat', 'participant': 'test3@test.com'})
		assert response.status_code == 200
		assert json.loads(response.data)['message'] == 'Participant added.'


def test_remove_participant():
	with app.app.test_client() as c:
		response = c.post('/remove_participant', json={'group_chat': 'Test Group Chat', 'participant': 'test3@test.com'})
		assert response.status_code == 200
		assert json.loads(response.data)['message'] == 'Participant removed.'


def test_set_admin():
	with app.app.test_client() as c:
		response = c.post('/set_admin', json={'group_chat': 'Test Group Chat', 'admin': 'test2@test.com'})
		assert response.status_code == 200
		assert json.loads(response.data)['message'] == 'Admin set.'


def test_post_status():
	with app.app.test_client() as c:
		response = c.post('/post_status', json={'email': 'test@test.com', 'content': 'Hello, world!', 'visibility': 'public'})
		assert response.status_code == 201
		assert json.loads(response.data)['content'] == 'Hello, world!'

if __name__ == '__main__':
	pytest.main()
