import pytest
import app
from app import User, Club, Book, Meeting, Discussion, Resource

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	user = User(id='1', name='John Doe', email='john@example.com')
	response = client.post('/user', json=user.__dict__)
	assert response.status_code == 201
	assert response.get_json() == user.__dict__


def test_create_club(client):
	club = Club(id='1', name='Book Club', description='A club for book lovers', is_private=False)
	response = client.post('/club', json=club.__dict__)
	assert response.status_code == 201
	assert response.get_json() == club.__dict__


def test_create_book(client):
	book = Book(id='1', title='Book Title', author='Author Name', description='Book Description')
	response = client.post('/book', json=book.__dict__)
	assert response.status_code == 201
	assert response.get_json() == book.__dict__


def test_create_meeting(client):
	meeting = Meeting(id='1', club_id='1', book_id='1', date='2022-01-01', time='12:00')
	response = client.post('/meeting', json=meeting.__dict__)
	assert response.status_code == 201
	assert response.get_json() == meeting.__dict__


def test_create_discussion(client):
	discussion = Discussion(id='1', club_id='1', book_id='1', user_id='1', message='Discussion Message')
	response = client.post('/discussion', json=discussion.__dict__)
	assert response.status_code == 201
	assert response.get_json() == discussion.__dict__


def test_create_resource(client):
	resource = Resource(id='1', title='Resource Title', description='Resource Description', link='http://example.com')
	response = client.post('/resource', json=resource.__dict__)
	assert response.status_code == 201
	assert response.get_json() == resource.__dict__
