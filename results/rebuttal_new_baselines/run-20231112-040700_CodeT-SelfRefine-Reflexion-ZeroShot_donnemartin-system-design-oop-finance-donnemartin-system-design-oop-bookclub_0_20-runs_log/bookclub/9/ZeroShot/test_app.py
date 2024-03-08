import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_club(client):
	response = client.post('/create_club', json={'name': 'Book Club', 'description': 'A club for book lovers', 'is_private': False, 'members': []})
	assert response.status_code == 201
	assert response.get_json()['name'] == 'Book Club'


def test_join_club(client):
	client.post('/create_club', json={'name': 'Book Club', 'description': 'A club for book lovers', 'is_private': False, 'members': []})
	response = client.post('/join_club', json={'user_name': 'John', 'club_name': 'Book Club'})
	assert response.status_code == 200
	assert 'Book Club' in response.get_json()['clubs']
