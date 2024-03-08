import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_club(client):
	response = client.post('/create_club', json={'name': 'Test Club', 'description': 'This is a test club', 'is_private': False, 'members': {}})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Club created successfully'}


def test_join_club(client):
	app.users['Test User'] = app.User(name='Test User', email='test@example.com', clubs={})
	response = client.post('/join_club', json={'club_name': 'Test Club', 'user_name': 'Test User'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Joined club successfully'}


def test_join_private_club(client):
	app.clubs['Test Club'].is_private = True
	response = client.post('/join_club', json={'club_name': 'Test Club', 'user_name': 'Test User'})
	assert response.status_code == 403
	assert response.get_json() == {'message': 'This club is private'}


def test_join_non_existent_club(client):
	response = client.post('/join_club', json={'club_name': 'Non Existent Club', 'user_name': 'Test User'})
	assert response.status_code == 404
	assert response.get_json() == {'message': 'Club or User not found'}
