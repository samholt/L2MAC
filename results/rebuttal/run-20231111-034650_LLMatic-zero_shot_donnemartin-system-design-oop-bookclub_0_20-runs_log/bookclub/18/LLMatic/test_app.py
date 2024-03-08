import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.get_json() == {'message': 'User registered successfully'}
	assert response.status_code == 200


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.get_json() == {'message': 'Logged in successfully'}
	assert response.status_code == 200


def test_view_profile(client):
	response = client.get('/view_profile?username=test')
	assert response.get_json() == {'read_books': [], 'wish_list': [], 'following': []}
	assert response.status_code == 200


def test_edit_profile(client):
	response = client.post('/edit_profile', json={'username': 'test', 'new_data': {'bio': 'I love reading books'}})
	assert response.get_json() == {'message': 'Profile updated successfully'}
	assert response.status_code == 200


def test_add_book(client):
	response = client.post('/add_book', json={'username': 'test', 'book_title': 'To Kill a Mockingbird'})
	assert response.get_json() == {'message': 'Book added to read books successfully'}
	assert response.status_code == 200


def test_add_to_wish_list(client):
	response = client.post('/add_to_wish_list', json={'username': 'test', 'book_title': '1984'})
	assert response.get_json() == {'message': 'Book added to wish list successfully'}
	assert response.status_code == 200


def test_follow_user(client):
	response = client.post('/register', json={'username': 'test2', 'email': 'test2@test.com', 'password': 'test2'})
	assert response.get_json() == {'message': 'User registered successfully'}
	assert response.status_code == 200
	response = client.post('/follow_user', json={'username': 'test', 'user_to_follow': 'test2'})
	assert response.get_json() == {'message': 'User followed successfully'}
	assert response.status_code == 200


def test_generate_recommendations(client):
	response = client.post('/add_book', json={'username': 'test2', 'book_title': '1984'})
	assert response.get_json() == {'message': 'Book added to read books successfully'}
	assert response.status_code == 200
	response = client.post('/generate_recommendations', json={'username': 'test'})
	assert response.get_json() == {'message': 'Recommendations generated successfully'}
	assert response.status_code == 200


def test_admin_dashboard(client):
	response = client.get('/admin/dashboard')
	assert response.status_code == 200


def test_remove_user(client):
	response = client.post('/admin/remove_user', json={'username': 'test2'})
	assert response.get_json() == {'message': 'User removed successfully'}
	assert response.status_code == 200


def test_remove_book(client):
	response = client.post('/admin/remove_book', json={'book_title': '1984'})
	assert response.get_json() == {'message': 'Book removed successfully'}
	assert response.status_code == 200


def test_notifications(client):
	response = client.post('/notifications', json={'username': 'test', 'notification': 'New book club meeting scheduled'})
	assert response.get_json() == {'message': 'Notification added successfully'}
	assert response.status_code == 200


def test_view_notifications(client):
	response = client.get('/view_notifications?username=test')
	assert 'notifications' in response.get_json()
	assert response.status_code == 200

