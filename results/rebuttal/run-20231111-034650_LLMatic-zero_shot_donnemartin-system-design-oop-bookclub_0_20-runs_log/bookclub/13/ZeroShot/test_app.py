import pytest
import app
from app import User, Club, Book, Meeting, Discussion, Resource

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def sample_data():
	return {
		'id': '1',
		'name': 'Test User',
		'email': 'test@example.com',
		'clubs': [],
		'books_read': [],
		'wish_list': [],
		'follows': []
	}

def test_create_user(client, sample_data):
	response = client.post('/user', json=sample_data)
	assert response.status_code == 201
	assert response.get_json() == sample_data

	user_in_db = app.DATABASE['users']['1']
	assert isinstance(user_in_db, User)
	assert user_in_db.id == '1'
	assert user_in_db.name == 'Test User'
	assert user_in_db.email == 'test@example.com'
	assert user_in_db.clubs == []
	assert user_in_db.books_read == []
	assert user_in_db.wish_list == []
	assert user_in_db.follows == []

# Similar tests can be written for Club, Book, Meeting, Discussion, Resource
