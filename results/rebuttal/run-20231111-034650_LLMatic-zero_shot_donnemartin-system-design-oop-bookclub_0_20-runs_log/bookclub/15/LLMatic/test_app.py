import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_home(client):
	response = client.get('/')
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Welcome to the Book Club App!'}


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Logged in successfully'}


def test_view_profile(client):
	response = client.get('/profile/test')
	assert response.status_code == 200
	assert 'username' in json.loads(response.data)


def test_edit_profile(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	response = client.post('/edit_profile', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Profile updated successfully'}


def test_list_books(client):
	response = client.get('/books')
	assert response.status_code == 200


def test_follow(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	response = client.post('/follow', json={'username': 'test2'})
	assert response.status_code == 400


def test_get_recommendations(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	response = client.get('/recommendations')
	assert response.status_code == 200
	assert 'recommendations' in json.loads(response.data)


def test_get_popular_books(client):
	response = client.get('/popular_books')
	assert response.status_code == 200
	assert 'popular_books' in json.loads(response.data)


def test_admin_dashboard(client):
	response = client.get('/admin/dashboard')
	assert response.status_code == 403
	response = client.post('/login', json={'username': 'admin', 'password': 'admin'})
	response = client.get('/admin/dashboard')
	assert response.status_code == 200
	assert 'users' in json.loads(response.data)


def test_set_notifications(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	response = client.post('/notifications', json={'notifications': {'email': True, 'sms': False}})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Notifications set successfully'}


def test_get_notifications(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	response = client.get('/notifications')
	assert response.status_code == 200
	assert 'email' in json.loads(response.data)
	assert 'sms' in json.loads(response.data)


def test_share_resources(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	response = client.post('/resources', json={'resources': {'book1': 'link1', 'book2': 'link2'}})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Resources shared successfully'}


def test_view_resources(client):
	response = client.get('/resources')
	assert response.status_code == 200
	assert 'test' in json.loads(response.data)

