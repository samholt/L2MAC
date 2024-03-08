import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={'id': '1', 'name': 'Test User', 'clubs': [], 'reading_list': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'name': 'Test User', 'clubs': [], 'reading_list': []}


def test_create_club(client):
	response = client.post('/club', json={'id': '1', 'name': 'Test Club', 'members': [], 'books': [], 'meetings': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'name': 'Test Club', 'members': [], 'books': [], 'meetings': []}


def test_create_meeting(client):
	response = client.post('/meeting', json={'id': '1', 'club_id': '1', 'date': '2022-01-01'})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'club_id': '1', 'date': '2022-01-01'}
