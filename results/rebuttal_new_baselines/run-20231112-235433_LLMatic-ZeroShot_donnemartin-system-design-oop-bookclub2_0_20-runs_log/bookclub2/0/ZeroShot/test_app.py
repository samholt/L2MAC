import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.mark.parametrize('user', [
	{'id': '1', 'name': 'John Doe', 'clubs': [], 'follows': []},
	{'id': '2', 'name': 'Jane Doe', 'clubs': [], 'follows': []}
])
def test_create_user(client, user):
	response = client.post('/create_user', data=json.dumps(user), content_type='application/json')
	assert response.status_code == 200
	assert json.loads(response.data) == user

@pytest.mark.parametrize('club', [
	{'id': '1', 'name': 'Book Club 1', 'members': [], 'privacy': 'public'},
	{'id': '2', 'name': 'Book Club 2', 'members': [], 'privacy': 'private'}
])
def test_create_club(client, club):
	response = client.post('/create_club', data=json.dumps(club), content_type='application/json')
	assert response.status_code == 200
	assert json.loads(response.data) == club

@pytest.mark.parametrize('meeting', [
	{'id': '1', 'club_id': '1', 'date': '2022-01-01'},
	{'id': '2', 'club_id': '2', 'date': '2022-02-01'}
])
def test_create_meeting(client, meeting):
	response = client.post('/create_meeting', data=json.dumps(meeting), content_type='application/json')
	assert response.status_code == 200
	assert json.loads(response.data) == meeting
