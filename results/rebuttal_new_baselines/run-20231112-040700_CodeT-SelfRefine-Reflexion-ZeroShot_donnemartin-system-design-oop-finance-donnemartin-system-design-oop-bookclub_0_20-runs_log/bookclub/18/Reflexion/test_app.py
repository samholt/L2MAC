import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

# Test user creation
@pytest.mark.parametrize('user', [{'id': '1', 'name': 'John Doe', 'email': 'john@example.com'}])
def test_create_user(client, user):
	response = client.post('/user/create', data=json.dumps(user), content_type='application/json')
	assert response.status_code == 201
	assert json.loads(response.data) == {'id': '1'}

# Test club creation
@pytest.mark.parametrize('club', [{'id': '1', 'name': 'Book Club', 'description': 'A club for book lovers', 'is_private': False}])
def test_create_club(client, club):
	response = client.post('/club/create', data=json.dumps(club), content_type='application/json')
	assert response.status_code == 201
	assert json.loads(response.data) == {'id': '1'}

# Test book creation
@pytest.mark.parametrize('book', [{'id': '1', 'title': 'Book Title', 'author': 'Author Name', 'description': 'Book Description'}])
def test_create_book(client, book):
	response = client.post('/book/create', data=json.dumps(book), content_type='application/json')
	assert response.status_code == 201
	assert json.loads(response.data) == {'id': '1'}

# Test meeting creation
@pytest.mark.parametrize('meeting', [{'id': '1', 'club_id': '1', 'book_id': '1', 'scheduled_time': '2022-12-31T23:59:59Z'}])
def test_create_meeting(client, meeting):
	response = client.post('/meeting/create', data=json.dumps(meeting), content_type='application/json')
	assert response.status_code == 201
	assert json.loads(response.data) == {'id': '1'}

# Test discussion creation
@pytest.mark.parametrize('discussion', [{'id': '1', 'club_id': '1', 'book_id': '1', 'user_id': '1', 'message': 'This is a discussion message.'}])
def test_create_discussion(client, discussion):
	response = client.post('/discussion/create', data=json.dumps(discussion), content_type='application/json')
	assert response.status_code == 201
	assert json.loads(response.data) == {'id': '1'}

# Test resource creation
@pytest.mark.parametrize('resource', [{'id': '1', 'title': 'Resource Title', 'link': 'http://example.com'}])
def test_create_resource(client, resource):
	response = client.post('/resource/create', data=json.dumps(resource), content_type='application/json')
	assert response.status_code == 201
	assert json.loads(response.data) == {'id': '1'}
