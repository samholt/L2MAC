import pytest
from app import app

@pytest.fixture
def client():
	with app.test_client() as client:
		yield client

@pytest.fixture
def user_data():
	return {'username': 'testuser', 'password': 'testpass', 'email': 'testuser@example.com'}

@pytest.fixture
def book_club_data():
	return {'name': 'testclub', 'privacy_setting': 'public'}

@pytest.fixture
def meeting_data():
	return {'date': '2022-12-31', 'time': '12:00', 'book_club': 'testclub'}

@pytest.fixture
def forum_data():
	return {'book_club': 'testclub'}

@pytest.fixture
def thread_data():
	return {'title': 'testthread', 'author': 'testuser'}

@pytest.fixture
def comment_data():
	return {'content': 'testcomment', 'author': 'testuser', 'thread': 'testthread'}

@pytest.fixture
def admin_data():
	return {'username': 'adminuser', 'action': 'moderate_content', 'content': {'id': 1, 'text': 'testcontent'}}


def test_register(client, user_data):
	response = client.post('/register', json=user_data)
	assert response.status_code == 201


def test_login(client, user_data):
	response = client.post('/login', json=user_data)
	assert response.status_code == 200


def test_create_book_club(client, book_club_data):
	response = client.post('/book_club', json=book_club_data)
	assert response.status_code == 201


def test_schedule_meeting(client, meeting_data):
	response = client.post('/meeting', json=meeting_data)
	assert response.status_code == 201


def test_create_forum(client, forum_data):
	response = client.post('/forum', json=forum_data)
	assert response.status_code == 201


def test_create_thread(client, thread_data):
	response = client.post('/thread', json=thread_data)
	assert response.status_code == 201


def test_post_comment(client, comment_data):
	response = client.post('/comment', json=comment_data)
	assert response.status_code == 201


def test_view_profile(client, user_data):
	client.post('/register', json=user_data)
	response = client.get('/profile', query_string={'username': user_data['username']})
	assert response.status_code == 200


def test_admin_action(client, admin_data):
	client.post('/register', json={'username': 'adminuser', 'password': 'adminpass', 'email': 'adminuser@example.com'})
	response = client.post('/admin', json=admin_data)
	assert response.status_code == 404

