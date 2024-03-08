import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={'id': '1', 'name': 'John', 'clubs': [], 'follows': []})
	assert response.status_code == 201
	assert json.loads(response.data) == {'id': '1', 'name': 'John', 'clubs': [], 'follows': []}


def test_create_club(client):
	response = client.post('/club', json={'id': '1', 'name': 'Book Club', 'members': [], 'privacy': 'public'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'id': '1', 'name': 'Book Club', 'members': [], 'privacy': 'public'}


def test_create_meeting(client):
	response = client.post('/meeting', json={'id': '1', 'club_id': '1', 'date': '2022-12-31'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'id': '1', 'club_id': '1', 'date': '2022-12-31'}
