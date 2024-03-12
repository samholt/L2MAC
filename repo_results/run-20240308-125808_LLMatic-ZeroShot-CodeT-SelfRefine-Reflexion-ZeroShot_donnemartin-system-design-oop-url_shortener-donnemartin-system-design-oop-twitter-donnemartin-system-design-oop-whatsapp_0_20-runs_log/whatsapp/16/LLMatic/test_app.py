import json
import pytest
from app import app

# Existing tests

# New tests

def test_post_status():
	with app.test_client() as c:
		resp = c.post('/signup', json={'username': 'test', 'password': 'test'})
		user_id = json.loads(resp.data)['user_id']
		resp = c.post(f'/post_status?user_id={user_id}', json={'image_data': 'test_image', 'visibility': 'public'})
		assert resp.status_code == 200


def test_view_status():
	with app.test_client() as c:
		resp = c.post('/signup', json={'username': 'test', 'password': 'test'})
		user_id = json.loads(resp.data)['user_id']
		c.post(f'/post_status?user_id={user_id}', json={'image_data': 'test_image', 'visibility': 'public'})
		resp = c.get(f'/view_status?user_id={user_id}')
		assert resp.status_code == 200
		assert 'test_image' in resp.data.decode()


def test_home():
	with app.test_client() as c:
		resp = c.get('/')
		assert resp.status_code == 200
		assert 'Welcome to Chat Application' in resp.data.decode()


def test_update_status():
	with app.test_client() as c:
		resp = c.post('/signup', json={'username': 'test', 'password': 'test'})
		user_id = json.loads(resp.data)['user_id']
		resp = c.post(f'/update_status?user_id={user_id}', json={'status': True})
		assert resp.status_code == 200


def test_send_message():
	with app.test_client() as c:
		resp = c.post('/signup', json={'username': 'sender', 'password': 'test'})
		sender_id = json.loads(resp.data)['user_id']
		resp = c.post('/signup', json={'username': 'receiver', 'password': 'test'})
		receiver_id = json.loads(resp.data)['user_id']
		resp = c.post(f'/send_message?sender_id={sender_id}&receiver_id={receiver_id}', json={'message': 'Hello'})
		assert resp.status_code == 200


def test_send_message_invalid_sender():
	with app.test_client() as c:
		resp = c.post('/signup', json={'username': 'receiver', 'password': 'test'})
		receiver_id = json.loads(resp.data)['user_id']
		resp = c.post(f'/send_message?sender_id=invalid&receiver_id={receiver_id}', json={'message': 'Hello'})
		assert resp.status_code == 404

# Rest of the tests
