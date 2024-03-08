import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'id': 1, 'name': 'John', 'clubs': [], 'reading_list': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1, 'name': 'John', 'clubs': [], 'reading_list': []}


def test_create_club(client):
	response = client.post('/create_club', json={'id': 1, 'name': 'Book Club', 'members': [], 'books': [], 'meetings': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1, 'name': 'Book Club', 'members': [], 'books': [], 'meetings': []}


def test_join_club(client):
	client.post('/create_user', json={'id': 1, 'name': 'John', 'clubs': [], 'reading_list': []})
	client.post('/create_club', json={'id': 1, 'name': 'Book Club', 'members': [], 'books': [], 'meetings': []})
	response = client.post('/join_club', json={'user_id': 1, 'club_id': 1})
	assert response.status_code == 200
	assert response.get_json()['clubs'][0]['name'] == 'Book Club'
