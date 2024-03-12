import pytest
from flask import Flask, request
from app import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_home(client):
	response = client.get('/')
	assert response.status_code == 200


def test_sign_up(client):
	response = client.post('/sign_up', data={'email': 'test@test.com', 'password': 'test123'})
	assert response.data == b'User signed up successfully'


def test_password_recovery(client):
	response = client.post('/password_recovery', data={'email': 'test@test.com'})
	assert response.data == b'Password recovery link has been sent to your email'


def test_set_profile_picture(client):
	response = client.post('/set_profile_picture', data={'picture_file': 'test.jpg'})
	assert response.data == b'Profile picture set successfully'


def test_set_status_message(client):
	response = client.post('/set_status_message', data={'status_message': 'Hello, world!'})
	assert response.data == b'Status message set successfully'


def test_manage_privacy_settings(client):
	response = client.post('/manage_privacy_settings', data={'privacy_settings': 'Public'})
	assert response.data == b'Privacy settings updated successfully'


def test_block_contact(client):
	response = client.post('/block_contact', data={'user': 'test@test.com'})
	assert response.data == b'Contact blocked successfully'


def test_unblock_contact(client):
	response = client.post('/unblock_contact', data={'user': 'test@test.com'})
	assert response.data == b'Contact unblocked successfully'


def test_create_group(client):
	response = client.post('/create_group', data={'group_details': 'Test Group'})
	assert response.data == b'Group created successfully'


def test_edit_group(client):
	response = client.post('/edit_group', data={'group_details': 'Test Group'})
	assert response.data == b'Group edited successfully'


def test_manage_group(client):
	response = client.post('/manage_group', data={'group_details': 'Test Group'})
	assert response.data == b'Group managed successfully'


def test_send_message(client):
	response = client.post('/send_message', data={'receiver': 'test@test.com', 'text': 'Hello, world!'})
	assert response.data == b'Message sent'


def test_receive_message(client):
	response = client.post('/receive_message', data={'sender': 'test@test.com', 'text': 'Hello, world!'})
	assert response.data == b'Message received'


def test_manage_read_receipt(client):
	response = client.post('/manage_read_receipt', data={'read_receipt': 'Read'})
	assert response.data == b'Read receipt managed'


def test_encrypt_message(client):
	response = client.post('/encrypt_message', data={'text': 'Hello, world!', 'encryption_key': '123'})
	assert response.data == b'Message encrypted'


def test_decrypt_message(client):
	response = client.post('/decrypt_message', data={'encrypted_text': '!dlrow ,olleH', 'encryption_key': '123'})
	assert response.data == b'Message decrypted'


def test_share_image(client):
	response = client.post('/share_image', data={'image': 'test.jpg'})
	assert response.data == b'Image shared'


def test_post_image_status(client):
	response = client.post('/post_image_status', data={'image': 'test.jpg', 'visibility_time': '24'})
	assert response.data == b'Image status posted'


def test_manage_viewers(client):
	response = client.post('/manage_viewers', data={'viewers': 'Public'})
	assert response.data == b'Viewers managed'
