import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_club(client):
	response = client.post('/create_club', json={'name': 'Test Club', 'description': 'This is a test club', 'is_private': False, 'members': []})
	assert response.status_code == 201
	assert response.get_json() == {'name': 'Test Club', 'description': 'This is a test club', 'is_private': False, 'members': []}


def test_join_club(client):
	app.users['Test User'] = app.User(name='Test User', email='test@example.com', clubs=[])
	app.clubs['Test Club'] = app.Club(name='Test Club', description='This is a test club', is_private=False, members=[])
	response = client.post('/join_club', json={'user_name': 'Test User', 'club_name': 'Test Club'})
	assert response.status_code == 200
	assert response.get_json() == {'name': 'Test User', 'email': 'test@example.com', 'clubs': [{'name': 'Test Club', 'description': 'This is a test club', 'is_private': False, 'members': ['Test User']}]}
