import pytest
from app import app


def test_app():
	app.testing = True
	client = app.test_client()

	response = client.post('/book_club', json={'name': 'Sci-Fi', 'description': 'A club for Sci-Fi lovers', 'privacy': 'public'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Club created successfully'

	response = client.post('/book_club/join', json={'name': 'Sci-Fi', 'user': 'John'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'User added successfully'

	response = client.post('/book_club/manage', json={'name': 'Sci-Fi', 'user': 'John', 'action': 'remove'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'User removed successfully'

	response = client.post('/add_resource', json={'title': 'Test Title', 'content': 'Test Content'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Resource added successfully'

	response = client.get('/view_resources')
	assert response.status_code == 200
	assert response.get_json() == {'Test Title': 'Test Content'}
