import pytest
import app
from flask import json
import uuid


def test_signup():
	with app.app.test_client() as client:
		unique_email = str(uuid.uuid4()) + '@test.com'
		response = client.post('/signup', data=json.dumps({'email': unique_email, 'password': 'test_password'}), content_type='application/json')
		assert response.status_code == 201
		assert unique_email in app.DATABASE['users']


def test_login():
	with app.app.test_client() as client:
		unique_email = str(uuid.uuid4()) + '@test.com'
		response = client.post('/login', data=json.dumps({'email': unique_email, 'password': 'test_password'}), content_type='application/json')
		assert response.status_code == 400
		assert response.get_json()['message'] == 'Invalid email or password'


def test_logout():
	with app.app.test_client() as client:
		unique_email = str(uuid.uuid4()) + '@test.com'
		response = client.post('/logout', data=json.dumps({'email': unique_email}), content_type='application/json')
		assert response.status_code == 404
		assert response.get_json()['message'] == 'User does not exist'


def test_send_message():
	with app.app.test_client() as client:
		unique_sender_email = str(uuid.uuid4()) + '@test.com'
		unique_receiver_email = str(uuid.uuid4()) + '@test.com'
		response = client.post('/send_message', data=json.dumps({'sender': unique_sender_email, 'receiver': unique_receiver_email, 'message': 'Hello, world!', 'image_url': 'http://example.com/image.jpg'}), content_type='application/json')
		assert response.status_code == 400
		assert response.get_json()['message'] == 'Sender or receiver does not exist'


def test_receive_message():
	with app.app.test_client() as client:
		unique_message_id = str(uuid.uuid4())
		response = client.post('/receive_message', data=json.dumps({'message_id': unique_message_id}), content_type='application/json')
		assert response.status_code == 404
		assert response.get_json()['message'] == 'Message does not exist'


def test_read_receipt():
	with app.app.test_client() as client:
		unique_message_id = str(uuid.uuid4())
		response = client.post('/read_receipt', data=json.dumps({'message_id': unique_message_id}), content_type='application/json')
		assert response.status_code == 404
		assert response.get_json()['message'] == 'Message does not exist'

