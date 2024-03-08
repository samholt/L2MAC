import pytest
from app import app
from url_shortener import DATABASE
from user_accounts import USER_DB
from analytics import ANALYTICS_DB
from datetime import datetime, timedelta

@pytest.fixture(autouse=True)
def setup():
	DATABASE.clear()
	USER_DB.clear()
	ANALYTICS_DB.clear()


def test_home():
	with app.test_client() as client:
		response = client.get('/')
		assert response.status_code == 200
		assert response.json['message'] == 'Hello, World!'


def test_redirect_to_url():
	with app.test_client() as client:
		response = client.get('/test')
		assert response.status_code == 404

	DATABASE['test'] = {'url': 'http://google.com', 'expiry_date': datetime.now() + timedelta(days=1)}
	response = client.get('/test')
	assert response.status_code == 302


def test_create_new_account():
	with app.test_client() as client:
		response = client.post('/create_account', json={'username': 'test', 'password': 'password'})
		assert response.status_code == 200
		assert response.json['result'] == True


def test_add_url():
	with app.test_client() as client:
		response = client.post('/add_url', json={'username': 'test', 'short_url': 'test'})
		assert response.status_code == 200
		assert response.json['result'] == True


def test_remove_url():
	with app.test_client() as client:
		response = client.post('/remove_url', json={'username': 'test', 'short_url': 'test'})
		assert response.status_code == 200
		assert response.json['result'] == True


def test_get_urls():
	with app.test_client() as client:
		response = client.post('/get_user_urls', json={'username': 'test'})
		assert response.status_code == 200
		assert response.json['result'] == []


def test_authenticate():
	with app.test_client() as client:
		response = client.post('/authenticate_user', json={'username': 'test', 'password': 'password'})
		assert response.status_code == 200
		assert response.json['result'] == True


def test_view_urls():
	with app.test_client() as client:
		response = client.get('/view_all_urls')
		assert response.status_code == 200
		assert response.json['result'] == {}


def test_del_url():
	with app.test_client() as client:
		response = client.post('/delete_url', json={'short_url': 'test'})
		assert response.status_code == 200
		assert response.json['result'] == True


def test_del_user():
	with app.test_client() as client:
		response = client.post('/delete_user', json={'username': 'test'})
		assert response.status_code == 200
		assert response.json['result'] == True


def test_view_performance():
	with app.test_client() as client:
		response = client.get('/view_system_performance')
		assert response.status_code == 200
		assert response.json['result'] == {'number_of_urls': 0, 'number_of_users': 0, 'number_of_clicks': 0}

