import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_club(client):
	response = client.post('/create_club', json={'name': 'Test Club', 'description': 'This is a test club', 'is_private': False})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Club created successfully'}


def test_join_club(client):
	app.users['Test User'] = app.User('Test User', 'test@example.com', {})
	app.clubs['Test Club'] = app.Club('Test Club', 'This is a test club', False, {})
	response = client.post('/join_club', json={'user_name': 'Test User', 'club_name': 'Test Club'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Joined club successfully'}
