import pytest
import app

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
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User and profile created successfully'}


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Login successful'}


def test_view_profile(client):
	response = client.get('/view_profile', json={'username': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'books': [], 'following': []}


def test_edit_profile(client):
	response = client.post('/edit_profile', json={'username': 'test', 'new_info': {'favorite_book': 'The Great Gatsby'}})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Profile edited successfully'}


def test_list_books(client):
	response = client.get('/list_books', json={'username': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'books': []}


def test_follow_user(client):
	response = client.post('/follow_user', json={'username': 'test', 'user_to_follow': 'test2'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User followed successfully'}


def test_create_book_club(client):
	response = client.post('/create_book_club', json={'name': 'Book Club 1', 'admin': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Book club created successfully'}


def test_join_book_club(client):
	response = client.post('/join_book_club', json={'name': 'Book Club 1', 'admin': 'test', 'member': 'test2'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Member added successfully'}


def test_schedule_meeting(client):
	response = client.post('/schedule_meeting', json={'meeting_id': '1', 'book_club': 'Book Club 1', 'date': '2022-01-01', 'time': '12:00'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Meeting scheduled successfully'}


def test_create_discussion(client):
	response = client.post('/create_discussion', json={'discussion_id': '1', 'book_club': 'Book Club 1', 'topic': 'Discussion 1'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Discussion created successfully'}


def test_post_comment(client):
	response = client.post('/post_comment', json={'discussion_id': '1', 'book_club': 'Book Club 1', 'topic': 'Discussion 1', 'comment': 'This is a comment'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Comment posted successfully'}


def test_upload_resource(client):
	response = client.post('/upload_resource', json={'discussion_id': '1', 'book_club': 'Book Club 1', 'topic': 'Discussion 1', 'resource': 'This is a resource'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Resource uploaded successfully'}


def test_suggest_book(client):
	response = client.post('/suggest_book', json={'book_id': '1', 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'username': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Book suggested successfully'}


def test_vote_for_book(client):
	response = client.post('/vote_for_book', json={'book_id': '1', 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Vote cast successfully'}


def test_generate_recommendation(client):
	response = client.get('/generate_recommendation', json={'username': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'recommendation': '1'}


def test_highlight_popular_book(client):
	response = client.get('/highlight_popular_book')
	assert response.status_code == 200
	assert response.get_json() == {'popular_book': '1'}


def test_admin_manage_book_club(client):
	response = client.post('/admin/manage_book_club', json={'username': 'test', 'book_club_name': 'Book Club 1', 'action': 'add_member', 'member': 'test2'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Action performed successfully'}


def test_admin_manage_user_account(client):
	response = client.post('/admin/manage_user_account', json={'username': 'test', 'user_to_manage': 'test2', 'action': 'delete_user'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Action performed successfully'}


def test_admin_remove_inappropriate_content(client):
	response = client.post('/admin/remove_inappropriate_content', json={'username': 'test', 'discussion_id': '1'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Inappropriate content removed'}


def test_admin_view_analytics(client):
	response = client.get('/admin/view_analytics', json={'username': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'num_users': 1, 'num_book_clubs': 1}


def test_setup_notification(client):
	response = client.post('/setup_notification', json={'username': 'test', 'message': 'This is a notification'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Notification set up successfully'}


def test_send_email_alert(client):
	response = client.post('/send_email_alert', json={'username': 'test', 'message': 'This is a notification'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Email alert sent'}

