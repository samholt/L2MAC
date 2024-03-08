import pytest
import app
from user import User
from service import Service

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_upload(client):
	response = client.post('/upload', data={'user_id': '1', 'file': (BytesIO(b'my file contents'), 'my_file.txt')})
	assert response.status_code == 200


def test_view(client):
	User('1').upload_file(BytesIO(b'my file contents'))
	response = client.get('/view?user_id=1&file_id=1')
	assert response.status_code == 200
	assert response.get_json()['file'] == 'my file contents'


def test_search(client):
	User('1').upload_file(BytesIO(b'my file contents'))
	response = client.get('/search?user_id=1&query=contents')
	assert response.status_code == 200
	assert 1 in response.get_json()['files']


def test_share(client):
	User('1').upload_file(BytesIO(b'my file contents'))
	response = client.post('/share', data={'user_id': '1', 'file_id': '1', 'recipient_id': '2'})
	assert response.status_code == 200
	assert '2' in Service.shared_files['1']


def test_download(client):
	User('1').upload_file(BytesIO(b'my file contents'))
	response = client.get('/download?user_id=1&file_id=1')
	assert response.status_code == 200
	assert response.get_json()['file'] == 'my file contents'
