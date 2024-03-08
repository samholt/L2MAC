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
		'books_read': {},
		'clubs_joined': {}
	})
	assert response.status_code == 201
	assert json.loads(response.data) == {
		'id': '1',
		'name': 'John Doe',
		'email': 'john@example.com',
		'books_read': {},
		'clubs_joined': {}
	}


def test_create_club(client):
	response = client.post('/club', json={
		'id': '1',
		'name': 'Book Club',
		'description': 'A club for book lovers',
		'is_private': False,
		'members': {}
	})
	assert response.status_code == 201
	assert json.loads(response.data) == {
		'id': '1',
		'name': 'Book Club',
		'description': 'A club for book lovers',
		'is_private': False,
		'members': {}
	}


def test_create_book(client):
	response = client.post('/book', json={
		'id': '1',
		'title': 'Book Title',
		'author': 'Author Name',
		'description': 'Book Description'
	})
	assert response.status_code == 201
	assert json.loads(response.data) == {
		'id': '1',
		'title': 'Book Title',
		'author': 'Author Name',
		'description': 'Book Description'
	}


def test_create_meeting(client):
	response = client.post('/meeting', json={
		'id': '1',
		'club_id': '1',
		'book_id': '1',
		'date': '2022-12-31'
	})
	assert response.status_code == 201
	assert json.loads(response.data) == {
		'id': '1',
		'club_id': '1',
		'book_id': '1',
		'date': '2022-12-31'
	}


def test_create_discussion(client):
	response = client.post('/discussion', json={
		'id': '1',
		'club_id': '1',
		'book_id': '1',
		'user_id': '1',
		'message': 'This is a discussion message'
	})
	assert response.status_code == 201
	assert json.loads(response.data) == {
		'id': '1',
		'club_id': '1',
		'book_id': '1',
		'user_id': '1',
		'message': 'This is a discussion message'
	}


def test_create_resource(client):
	response = client.post('/resource', json={
		'id': '1',
		'title': 'Resource Title',
		'link': 'https://example.com'
	})
	assert response.status_code == 201
	assert json.loads(response.data) == {
		'id': '1',
		'title': 'Resource Title',
		'link': 'https://example.com'
	}
