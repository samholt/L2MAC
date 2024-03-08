import pytest
import app
from app import User, BookClub

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_create_user(client):
	response = client.post('/user', json={
		'id': '1',
		'name': 'John Doe',
		'email': 'john.doe@example.com',
		'books_read': [],
		'wish_list': [],
		'clubs_joined': []
	})
	assert response.status_code == 201
	assert response.get_json() == User(
		id='1',
		name='John Doe',
		email='john.doe@example.com',
		books_read=[],
		wish_list=[],
		clubs_joined=[]
	)

def test_get_user(client):
	response = client.get('/user/1')
	assert response.status_code == 200
	assert response.get_json() == User(
		id='1',
		name='John Doe',
		email='john.doe@example.com',
		books_read=[],
		wish_list=[],
		clubs_joined=[]
	)

def test_create_book_club(client):
	response = client.post('/book_club', json={
		'id': '1',
		'name': 'Book Club 1',
		'description': 'This is a book club.',
		'is_private': False,
		'members': [],
		'books': [],
		'meetings': [],
		'discussions': []
	})
	assert response.status_code == 201
	assert response.get_json() == BookClub(
		id='1',
		name='Book Club 1',
		description='This is a book club.',
		is_private=False,
		members=[],
		books=[],
		meetings=[],
		discussions=[]
	)

def test_get_book_club(client):
	response = client.get('/book_club/1')
	assert response.status_code == 200
	assert response.get_json() == BookClub(
		id='1',
		name='Book Club 1',
		description='This is a book club.',
		is_private=False,
		members=[],
		books=[],
		meetings=[],
		discussions=[]
	)
