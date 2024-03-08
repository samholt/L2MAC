import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_create_user(client):
	response = client.post('/user', json={
		'id': '1',
		'name': 'Test User',
		'clubs': [],
		'books': []
	})
	assert response.status_code == 201
	assert json.loads(response.data) == {
		'id': '1',
		'name': 'Test User',
		'clubs': [],
		'books': []
	}

def test_create_club(client):
	response = client.post('/club', json={
		'id': '1',
		'name': 'Test Club',
		'members': [],
		'books': [],
		'meetings': []
	})
	assert response.status_code == 201
	assert json.loads(response.data) == {
		'id': '1',
		'name': 'Test Club',
		'members': [],
		'books': [],
		'meetings': []
	}

def test_create_book(client):
	response = client.post('/book', json={
		'id': '1',
		'title': 'Test Book',
		'author': 'Test Author'
	})
	assert response.status_code == 201
	assert json.loads(response.data) == {
		'id': '1',
		'title': 'Test Book',
		'author': 'Test Author'
	}

def test_create_meeting(client):
	response = client.post('/meeting', json={
		'id': '1',
		'club_id': '1',
		'book_id': '1',
		'date': '2022-01-01'
	})
	assert response.status_code == 201
	assert json.loads(response.data) == {
		'id': '1',
		'club_id': '1',
		'book_id': '1',
		'date': '2022-01-01'
	}
