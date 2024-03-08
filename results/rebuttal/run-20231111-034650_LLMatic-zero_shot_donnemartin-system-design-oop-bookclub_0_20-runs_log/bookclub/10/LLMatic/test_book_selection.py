import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_suggest_book(client):
	response = client.post('/book', json={'id': '1', 'title': 'Test Book', 'author': 'Test Author', 'description': 'Test Description', 'reviews': []})
	assert response.get_json() == {'message': 'Book suggested successfully'}
	assert response.status_code == 201


def test_get_book(client):
	response = client.get('/book/1')
	assert response.get_json() == {'id': '1', 'title': 'Test Book', 'author': 'Test Author', 'description': 'Test Description', 'reviews': []}
	assert response.status_code == 200


def test_vote_book(client):
	response = client.post('/book/1/vote', json={'user_id': '1'})
	assert response.get_json() == {'message': 'Voted for book successfully'}
	assert response.status_code == 200


def test_select_book(client):
	client.post('/bookclub', json={'id': '1', 'name': 'Test Club', 'description': 'Test Description', 'privacy': 'public', 'members': []})
	response = client.post('/book/1/select', json={'club_id': '1'})
	assert response.get_json() == {'message': 'Book selected for book club successfully'}
	assert response.status_code == 200
