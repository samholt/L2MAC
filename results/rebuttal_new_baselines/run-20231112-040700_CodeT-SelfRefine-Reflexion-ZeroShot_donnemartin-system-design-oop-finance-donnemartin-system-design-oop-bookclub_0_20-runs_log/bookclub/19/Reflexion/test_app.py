import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'id': 1, 'name': 'John'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}


def test_create_club(client):
	response = client.post('/create_club', json={'id': 1, 'name': 'Book Club'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Club created successfully'}


def test_join_club(client):
	client.post('/create_user', json={'id': 1, 'name': 'John'})
	client.post('/create_club', json={'id': 1, 'name': 'Book Club'})
	response = client.post('/join_club', json={'user_id': 1, 'club_id': 1})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User joined club successfully'}
