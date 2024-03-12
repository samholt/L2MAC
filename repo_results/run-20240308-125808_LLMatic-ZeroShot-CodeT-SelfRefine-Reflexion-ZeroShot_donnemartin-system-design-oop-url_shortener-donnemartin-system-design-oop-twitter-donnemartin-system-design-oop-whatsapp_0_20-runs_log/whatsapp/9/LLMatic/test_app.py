import pytest
import app


def test_register():
	response = app.app.test_client().post('/register', data={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 302
	assert 'test@test.com' in app.users


def test_login():
	response = app.app.test_client().post('/login', data={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 302


def test_logout():
	with app.app.test_client() as c:
		c.post('/login', data={'email': 'test@test.com', 'password': 'test123'})
		response = c.get('/logout')
		assert response.status_code == 302


def test_home():
	with app.app.test_client() as c:
		c.post('/login', data={'email': 'test@test.com', 'password': 'test123'})
		response = c.get('/')
		assert response.status_code == 200


def test_connectivity():
	app.users['test@test.com'] = app.User('test@test.com', 'test123')
	app.users['test@test.com'].is_online = False
	app.users['test@test.com'].message_queue.append('Hello')
	response = app.app.test_client().post('/connectivity', json={'email': 'test@test.com', 'is_online': True})
	assert response.status_code == 204
	assert app.users['test@test.com'].is_online
	assert not app.users['test@test.com'].message_queue
	assert 'Hello' in app.messages
