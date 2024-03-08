import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_home_page(client):
	response = client.get('/')
	assert response.status_code == 200
	assert b'Welcome to the Book Club App!' in response.data


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert b'User registered successfully' in response.data


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert b'Logged in successfully' in response.data


def test_create_club(client):
	response = client.post('/create_club', json={'club_name': 'test_club', 'username': 'test'})
	assert response.status_code == 200
	assert b'Book club created successfully' in response.data


def test_join_club(client):
	response = client.post('/join_club', json={'club_name': 'test_club', 'username': 'test2'})
	assert response.status_code == 200
	assert b'Joined book club successfully' in response.data


def test_schedule_meeting(client):
	response = client.post('/schedule_meeting', json={'meeting_id': 'test_meeting', 'club_name': 'test_club', 'meeting_time': '2022-01-01T00:00:00'})
	assert response.status_code == 200
	assert b'Meeting scheduled successfully' in response.data


def test_create_discussion(client):
	response = client.post('/create_discussion', json={'discussion_id': 'test_discussion', 'club_name': 'test_club', 'topic': 'test_topic'})
	assert response.status_code == 200
	assert b'Discussion created successfully' in response.data


def test_post_comment(client):
	response = client.post('/post_comment', json={'discussion_id': 'test_discussion', 'comment': 'test_comment'})
	assert response.status_code == 200
	assert b'Comment posted successfully' in response.data


def test_suggest_book(client):
	response = client.post('/suggest_book', json={'book_id': 'test_book', 'club_name': 'test_club', 'username': 'test'})
	assert response.status_code == 200
	assert b'Book suggested successfully' in response.data


def test_vote_book(client):
	response = client.post('/vote_book', json={'book_id': 'test_book'})
	assert response.status_code == 200
	assert b'Vote counted successfully' in response.data


def test_create_profile(client):
	response = client.post('/create_profile', json={'username': 'test', 'profile_info': {'name': 'Test User', 'email': 'test@example.com'}})
	assert response.status_code == 200
	assert b'Profile created successfully' in response.data


def test_edit_profile(client):
	response = client.post('/edit_profile', json={'username': 'test', 'profile_info': {'name': 'Test User', 'email': 'test2@example.com'}})
	assert response.status_code == 200
	assert b'Profile updated successfully' in response.data


def test_view_profile(client):
	response = client.get('/view_profile?username=test')
	assert response.status_code == 200
	assert b'test2@example.com' in response.data


def test_follow_user(client):
	client.post('/register', json={'username': 'test2', 'password': 'test2'})
	response = client.post('/follow_user', json={'username': 'test', 'user_to_follow': 'test2'})
	assert response.status_code == 200
	assert b'User followed successfully' in response.data


def test_generate_recommendations(client):
	response = client.post('/generate_recommendations', json={'username': 'test'})
	assert response.status_code == 200
	assert b'Recommendations generated successfully' in response.data


def test_set_notification(client):
	response = client.post('/set_notification', json={'username': 'test', 'notification': 'test_notification'})
	assert response.status_code == 200
	assert b'Notification set successfully' in response.data


def test_view_notifications(client):
	response = client.get('/view_notifications?username=test')
	assert response.status_code == 200
	assert b'test_notification' in response.data
