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
		'clubs': [],
		'books_read': [],
		'wish_list': []
	})
	assert response.status_code == 201
	assert json.loads(response.data) == {
		'id': '1',
		'name': 'John Doe',
		'email': 'john@example.com',
		'clubs': [],
		'books_read': [],
		'wish_list': []
	}


def test_create_club(client):
	response = client.post('/club', json={
		'id': '1',
		'name': 'Book Club',
		'description': 'A club for book lovers',
		'is_private': False,
		'members': [],
		'books': [],
		'discussions': []
	})
	assert response.status_code == 201
	assert json.loads(response.data) == {
		'id': '1',
		'name': 'Book Club',
		'description': 'A club for book lovers',
		'is_private': False,
		'members': [],
		'books': [],
		'discussions': []
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


def test_create_discussion(client):
	response = client.post('/discussion', json={
		'id': '1',
		'club_id': '1',
		'book_id': '1',
		'comments': []
	})
	assert response.status_code == 201
	assert json.loads(response.data) == {
		'id': '1',
		'club_id': '1',
		'book_id': '1',
		'comments': []
	}
