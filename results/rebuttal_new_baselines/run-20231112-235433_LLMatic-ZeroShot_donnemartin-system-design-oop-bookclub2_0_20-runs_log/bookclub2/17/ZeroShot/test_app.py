import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_create_user(client):
	response = client.post('/create_user', json={'id': '1', 'name': 'John', 'clubs': [], 'follows': []})
	assert response.status_code == 200
	assert json.loads(response.data) == {'id': '1', 'name': 'John', 'clubs': [], 'follows': []}

def test_create_club(client):
	response = client.post('/create_club', json={'id': '1', 'name': 'Book Club', 'members': [], 'privacy': 'public'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'id': '1', 'name': 'Book Club', 'members': [], 'privacy': 'public'}

def test_join_club(client):
	client.post('/create_user', json={'id': '1', 'name': 'John', 'clubs': [], 'follows': []})
	client.post('/create_club', json={'id': '1', 'name': 'Book Club', 'members': [], 'privacy': 'public'})
	response = client.post('/join_club', json={'user_id': '1', 'club_id': '1'})
	assert response.status_code == 200
	assert response.data == b'Joined club'

def test_schedule_meeting(client):
	response = client.post('/schedule_meeting', json={'id': '1', 'club_id': '1', 'date': '2022-12-31'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'id': '1', 'club_id': '1', 'date': '2022-12-31'}
