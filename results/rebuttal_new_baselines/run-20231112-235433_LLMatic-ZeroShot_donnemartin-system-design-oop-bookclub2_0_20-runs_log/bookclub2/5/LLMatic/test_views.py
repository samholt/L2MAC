import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True

	# Setup
	app.users['1'] = {'id': '1', 'username': 'test', 'email': 'test@test.com', 'password': 'test'}
	app.bookclubs['1'] = {'id': '1', 'name': 'test', 'description': 'test', 'privacy_settings': 'public'}
	app.meetings['1'] = {'id': '1', 'bookclub_id': '1', 'date': '2022-01-01', 'time': '12:00', 'location': 'test'}

	with app.app.test_client() as client:
		yield client


def test_user_profile(client):
	response = client.get('/user/1')
	assert response.status_code == 200


def test_bookclub_page(client):
	response = client.get('/bookclub/1')
	assert response.status_code == 200


def test_meeting_page(client):
	response = client.get('/meeting/1')
	assert response.status_code == 200

