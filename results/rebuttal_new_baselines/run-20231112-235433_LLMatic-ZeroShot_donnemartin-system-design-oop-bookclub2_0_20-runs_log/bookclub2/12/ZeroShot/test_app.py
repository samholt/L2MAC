import pytest
import app
from app import User, Club, Meeting, Discussion

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={'id': '1', 'name': 'John', 'clubs': [], 'follows': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'name': 'John', 'clubs': [], 'follows': []}


def test_create_club(client):
	response = client.post('/club', json={'id': '1', 'name': 'Book Club', 'privacy': 'public', 'members': [], 'admins': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'name': 'Book Club', 'privacy': 'public', 'members': [], 'admins': []}


def test_create_meeting(client):
	response = client.post('/meeting', json={'id': '1', 'club_id': '1', 'date': '2022-12-31'})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'club_id': '1', 'date': '2022-12-31'}


def test_create_discussion(client):
	response = client.post('/discussion', json={'id': '1', 'club_id': '1', 'topic': 'Book Discussion', 'comments': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'club_id': '1', 'topic': 'Book Discussion', 'comments': []}
