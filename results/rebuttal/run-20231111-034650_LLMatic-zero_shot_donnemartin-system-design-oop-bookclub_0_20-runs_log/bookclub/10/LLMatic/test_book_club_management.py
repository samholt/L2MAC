import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_book_club(client):
	response = client.post('/bookclub', json={'id': '1', 'name': 'Book Club 1', 'description': 'A book club for book lovers', 'privacy': 'public', 'members': []})
	assert response.get_json() == {'message': 'Book club created successfully'}
	assert response.status_code == 201


def test_get_book_club(client):
	response = client.get('/bookclub/1')
	assert response.get_json() == {'id': '1', 'name': 'Book Club 1', 'description': 'A book club for book lovers', 'privacy': 'public', 'members': []}


def test_update_book_club(client):
	response = client.put('/bookclub/1', json={'description': 'A book club for all book lovers'})
	assert response.get_json() == {'message': 'Book club updated successfully'}


def test_delete_book_club(client):
	response = client.delete('/bookclub/1')
	assert response.get_json() == {'message': 'Book club deleted successfully'}


def test_join_book_club(client):
	client.post('/bookclub', json={'id': '1', 'name': 'Book Club 1', 'description': 'A book club for book lovers', 'privacy': 'public', 'members': []})
	response = client.post('/bookclub/1/join', json={'user_id': '1'})
	assert response.get_json() == {'message': 'Joined book club successfully'}


def test_request_to_join_private_book_club(client):
	client.post('/bookclub', json={'id': '2', 'name': 'Book Club 2', 'description': 'A private book club', 'privacy': 'private', 'members': ['1']})
	response = client.post('/bookclub/2/join', json={'user_id': '2'})
	assert response.get_json() == {'message': 'Request to join private book club sent'}
