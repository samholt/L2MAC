import pytest
import app
from app import User, Club, Book, Meeting, Discussion, Resource

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def user():
	return User(id='1', name='Test User', email='test@example.com')

@pytest.fixture
def club():
	return Club(id='1', name='Test Club', description='This is a test club', is_private=False)

@pytest.fixture
def book():
	return Book(id='1', title='Test Book', author='Test Author', summary='This is a test book')

@pytest.fixture
def meeting():
	return Meeting(id='1', club_id='1', book_id='1', date='2022-01-01', reminder=True)

@pytest.fixture
def discussion():
	return Discussion(id='1', club_id='1', book_id='1', user_id='1', message='This is a test discussion')

@pytest.fixture
def resource():
	return Resource(id='1', title='Test Resource', link='https://example.com', contributor='1')


def test_create_user(client, user):
	response = client.post('/user', json=user.__dict__)
	assert response.status_code == 201
	assert response.get_json() == user.__dict__


def test_create_club(client, club):
	response = client.post('/club', json=club.__dict__)
	assert response.status_code == 201
	assert response.get_json() == club.__dict__


def test_create_book(client, book):
	response = client.post('/book', json=book.__dict__)
	assert response.status_code == 201
	assert response.get_json() == book.__dict__


def test_create_meeting(client, meeting):
	response = client.post('/meeting', json=meeting.__dict__)
	assert response.status_code == 201
	assert response.get_json() == meeting.__dict__


def test_create_discussion(client, discussion):
	response = client.post('/discussion', json=discussion.__dict__)
	assert response.status_code == 201
	assert response.get_json() == discussion.__dict__


def test_create_resource(client, resource):
	response = client.post('/resource', json=resource.__dict__)
	assert response.status_code == 201
	assert response.get_json() == resource.__dict__
