import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_get_recommendations(client):
	app.DATABASE['users']['1'] = {'username': 'test', 'email': 'test@test.com', 'password': 'test', 'interests': [], 'books': []}
	response = client.get('/recommendations/1')
	assert response.status_code == 200
	assert 'recommendations' in response.get_json()


def test_get_popular_books(client):
	response = client.get('/popular_books')
	assert response.status_code == 200
	assert 'popular_books' in response.get_json()
