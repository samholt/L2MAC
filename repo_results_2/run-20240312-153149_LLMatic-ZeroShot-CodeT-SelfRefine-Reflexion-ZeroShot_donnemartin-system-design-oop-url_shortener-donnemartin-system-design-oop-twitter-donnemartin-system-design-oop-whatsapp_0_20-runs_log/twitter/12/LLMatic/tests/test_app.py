import pytest
import app
import jwt
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_notification(client):
	response = client.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	token = jwt.encode({'user': 'test@test.com', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.app.config['SECRET_KEY'])
	response = client.post('/create_notification', json={'token': token, 'content': 'This is a test notification'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Notification created successfully'}
	assert len(app.notifications_db) == 1
	assert app.notifications_db[0].user == 'test@test.com'
	assert app.notifications_db[0].content == 'This is a test notification'


def test_trending(client):
	response = client.post('/register', json={'email': 'test1@test.com', 'username': 'test1', 'password': 'test1'})
	assert response.status_code == 200
	token1 = jwt.encode({'user': 'test1@test.com', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.app.config['SECRET_KEY'])
	response = client.post('/create_post', json={'token': token1, 'content': 'This is a test post'})
	assert response.status_code == 200
	response = client.post('/register', json={'email': 'test2@test.com', 'username': 'test2', 'password': 'test2'})
	assert response.status_code == 200
	token2 = jwt.encode({'user': 'test2@test.com', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.app.config['SECRET_KEY'])
	response = client.post('/create_post', json={'token': token2, 'content': 'This is another test post'})
	assert response.status_code == 200
	response = client.get('/trending')
	assert response.status_code == 200
	assert response.get_json() == {'trending': [['This', 2], ['is', 2], ['test', 2], ['post', 2], ['a', 1], ['another', 1]]}

