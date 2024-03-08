import pytest
from app import app, db
from models import User, File, Permission

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.fixture
def init_database():
	db.create_all()
	yield
	db.drop_all()


def test_create_user(client, init_database):
	response = client.post('/user', json={'name': 'test', 'email': 'test@test.com'})
	assert response.status_code == 200
	assert response.get_json()['name'] == 'test'
	assert response.get_json()['email'] == 'test@test.com'


def test_upload_file(client, init_database):
	response = client.post('/file', json={'name': 'test.txt', 'content': 'Hello, World!', 'owner_id': 1})
	assert response.status_code == 200
	assert response.get_json()['name'] == 'test.txt'
	assert response.get_json()['owner_id'] == 1


def test_download_file(client, init_database):
	response = client.get('/file/1')
	assert response.status_code == 200
	assert response.get_json()['name'] == 'test.txt'
	assert response.get_json()['owner_id'] == 1


def test_delete_file(client, init_database):
	response = client.delete('/file/1')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'File deleted'


def test_share_file(client, init_database):
	response = client.post('/file/1/share', json={'user_id': 2, 'can_edit': True, 'can_view': True})
	assert response.status_code == 200
	assert response.get_json()['file_id'] == 1
	assert response.get_json()['user_id'] == 2
	assert response.get_json()['can_edit'] == True
	assert response.get_json()['can_view'] == True


def test_search_files(client, init_database):
	response = client.get('/file/search?query=test')
	assert response.status_code == 200
	assert len(response.get_json()) > 0
	assert response.get_json()[0]['name'] == 'test.txt'

