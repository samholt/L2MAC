import pytest
import app
from app import Club, User

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
	app.clubs['Test Club'] = Club('Test Club', 'This is a test club', False, [])
	app.users['Test User'] = User('Test User', [])
	response = client.post('/join_club', json={'club_name': 'Test Club', 'user_name': 'Test User'})
	assert response.status_code == 200
	assert response.get_json() == {'name': 'Test Club', 'description': 'This is a test club', 'is_private': False, 'members': ['Test User']}
