import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_home(client):
	response = client.get('/')
	assert response.status_code == 200
	assert response.data == b'Welcome to the Book Club App!'


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Logged in successfully'}


def test_create_club(client):
	response = client.post('/create_club', json={'club_name': 'test_club', 'description': 'This is a test club', 'is_public': True, 'admin': 'test'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Book club created successfully'}


def test_join_club(client):
	response = client.post('/join_club', json={'club_name': 'test_club', 'username': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Joined the book club successfully'}


def test_schedule_meeting(client):
	response = client.post('/schedule_meeting', json={'meeting_id': 'test_meeting', 'date_time': '2022-01-01T00:00:00', 'book_club': 'test_club', 'attendees': ['test']})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Meeting scheduled successfully'}


def test_create_discussion(client):
	response = client.post('/create_discussion', json={'discussion_id': 'test_discussion', 'title': 'Test Discussion', 'book_club': 'test_club'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Discussion created successfully'}


def test_post_comment(client):
	response = client.post('/post_comment', json={'discussion_id': 'test_discussion', 'user': 'test', 'comment': 'This is a test comment'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Comment posted successfully'}


def test_post_reply(client):
	response = client.post('/post_reply', json={'discussion_id': 'test_discussion', 'comment_index': 0, 'user': 'test', 'reply': 'This is a test reply'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Reply posted successfully'}


def test_suggest_book(client):
	response = client.post('/suggest_book', json={'book_id': 'test_book', 'title': 'Test Book', 'author': 'Test Author'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Book suggested successfully'}


def test_vote_book(client):
	response = client.post('/vote_book', json={'book_id': 'test_book'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Vote counted successfully'}


def test_recommend_book(client):
	response = client.post('/recommend_book', json={'username': 'test', 'book_id': 'test_book', 'reason': 'This is a test reason'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Book recommended successfully'}


def test_admin_dashboard(client):
	response = client.get('/admin_dashboard')
	assert response.status_code == 200
	assert 'users' in json.loads(response.data)
	assert 'book_clubs' in json.loads(response.data)
	assert 'meetings' in json.loads(response.data)
	assert 'discussions' in json.loads(response.data)
	assert 'book_selections' in json.loads(response.data)
	assert 'user_profiles' in json.loads(response.data)
	assert 'recommendations' in json.loads(response.data)
	assert 'admin_dashboard' in json.loads(response.data)
	assert 'notifications' in json.loads(response.data)
	assert 'resource_library' in json.loads(response.data)


def test_create_notification(client):
	response = client.post('/create_notification', json={'notification_id': 'test_notification', 'type': 'Test Type', 'user': 'test', 'content': 'This is a test notification'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Notification created successfully'}
