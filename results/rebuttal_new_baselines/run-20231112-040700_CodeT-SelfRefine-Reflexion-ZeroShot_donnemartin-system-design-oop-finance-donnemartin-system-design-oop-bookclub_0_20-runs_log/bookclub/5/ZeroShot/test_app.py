import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={
		'id': '1',
		'name': 'John Doe',
		'email': 'john@example.com',
		'clubs': {},
		'books_read': {},
		'books_to_read': {},
		'follows': {}
	})
	assert response.status_code == 201
	assert json.loads(response.data) == {
		'id': '1',
		'name': 'John Doe',
		'email': 'john@example.com',
		'clubs': {},
		'books_read': {},
		'books_to_read': {},
		'follows': {}
	}


def test_create_club(client):
	response = client.post('/club', json={
		'id': '1',
		'name': 'Book Club',
		'description': 'A club for book lovers',
		'is_private': False,
		'members': {},
		'books': {},
		'meetings': {},
		'discussions': {}
	})
	assert response.status_code == 201
	assert json.loads(response.data) == {
		'id': '1',
		'name': 'Book Club',
		'description': 'A club for book lovers',
		'is_private': False,
		'members': {},
		'books': {},
		'meetings': {},
		'discussions': {}
	}


def test_create_book(client):
	response = client.post('/book', json={
		'id': '1',
		'title': 'Book Title',
		'author': 'Author Name',
		'description': 'Book description',
		'reviews': {}
	})
	assert response.status_code == 201
	assert json.loads(response.data) == {
		'id': '1',
		'title': 'Book Title',
		'author': 'Author Name',
		'description': 'Book description',
		'reviews': {}
	}


def test_create_meeting(client):
	response = client.post('/meeting', json={
		'id': '1',
		'club_id': '1',
		'book_id': '1',
		'date': '2022-12-31',
		'time': '12:00'
	})
	assert response.status_code == 201
	assert json.loads(response.data) == {
		'id': '1',
		'club_id': '1',
		'book_id': '1',
		'date': '2022-12-31',
		'time': '12:00'
	}


def test_create_discussion(client):
	response = client.post('/discussion', json={
		'id': '1',
		'club_id': '1',
		'book_id': '1',
		'user_id': '1',
		'message': 'Discussion message',
		'replies': {}
	})
	assert response.status_code == 201
	assert json.loads(response.data) == {
		'id': '1',
		'club_id': '1',
		'book_id': '1',
		'user_id': '1',
		'message': 'Discussion message',
		'replies': {}
	}


def test_create_resource(client):
	response = client.post('/resource', json={
		'id': '1',
		'title': 'Resource Title',
		'link': 'http://example.com',
		'contributor': 'John Doe'
	})
	assert response.status_code == 201
	assert json.loads(response.data) == {
		'id': '1',
		'title': 'Resource Title',
		'link': 'http://example.com',
		'contributor': 'John Doe'
	}
