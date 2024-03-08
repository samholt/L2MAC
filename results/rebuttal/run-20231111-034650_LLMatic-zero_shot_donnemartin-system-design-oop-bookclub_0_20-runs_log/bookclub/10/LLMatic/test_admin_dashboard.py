import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_admin_dashboard(client):
	response = client.get('/admin/dashboard')
	assert response.status_code == 200
	data = response.get_json()
	assert 'users' in data
	assert 'book_clubs' in data
	assert 'discussions' in data
	assert 'books' in data
	assert 'user_engagement' in data
	assert 'popular_books' in data
