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
	assert response.get_json() == {'message': 'Club created successfully'}


def test_join_club(client):
	client.post('/create_user', json={'name': 'Test User', 'email': 'test@example.com', 'clubs': [], 'invitations': []})
	client.post('/create_club', json={'name': 'Test Club', 'description': 'This is a test club', 'is_private': False, 'members': []})
	client.post('/send_invitation', json={'user_name': 'Test User', 'club_name': 'Test Club'})
	response = client.post('/join_club', json={'user_name': 'Test User', 'club_name': 'Test Club'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Joined club successfully'}


def test_create_user(client):
	response = client.post('/create_user', json={'name': 'Test User', 'email': 'test@example.com', 'clubs': [], 'invitations': []})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}


def test_send_invitation(client):
	client.post('/create_user', json={'name': 'Test User', 'email': 'test@example.com', 'clubs': [], 'invitations': []})
	client.post('/create_club', json={'name': 'Test Club', 'description': 'This is a test club', 'is_private': False, 'members': []})
	response = client.post('/send_invitation', json={'user_name': 'Test User', 'club_name': 'Test Club'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Invitation sent successfully'}
