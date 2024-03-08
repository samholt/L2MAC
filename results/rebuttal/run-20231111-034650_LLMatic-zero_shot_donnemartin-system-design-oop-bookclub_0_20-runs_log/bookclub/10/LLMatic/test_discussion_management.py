import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_discussion(client):
	response = client.post('/discussion', json={'id': '1', 'book_club_id': '1', 'user_id': '1', 'message': 'Hello, world!', 'replies': [], 'attachments': []})
	assert response.get_json() == {'message': 'Discussion created successfully'}
	assert response.status_code == 201


def test_get_discussion(client):
	response = client.get('/discussion/1')
	assert response.get_json() == {'id': '1', 'book_club_id': '1', 'user_id': '1', 'message': 'Hello, world!', 'replies': [], 'attachments': []}
	assert response.status_code == 200


def test_update_discussion(client):
	response = client.put('/discussion/1', json={'message': 'Hello, book club!'})
	assert response.get_json() == {'message': 'Discussion updated successfully'}
	assert response.status_code == 200


def test_delete_discussion(client):
	response = client.delete('/discussion/1')
	assert response.get_json() == {'message': 'Discussion deleted successfully'}
	assert response.status_code == 200
