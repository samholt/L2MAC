import app
import pytest


def test_database():
	# Test that the database can store and retrieve data
	app.DATABASE['users']['test_user'] = 'test_data'
	assert app.DATABASE['users']['test_user'] == 'test_data'
	
	# Test that the database can delete data
	del app.DATABASE['users']['test_user']
	assert 'test_user' not in app.DATABASE['users']


def test_register():
	with app.app.test_client() as client:
		# Test that a user can be registered
		response = client.post('/register', json={'username': 'test_user', 'password': 'test_password'})
		assert response.status_code == 200
		assert 'test_user' in app.DATABASE['users']

		# Test that a user cannot be registered twice
		response = client.post('/register', json={'username': 'test_user', 'password': 'test_password'})
		assert response.status_code == 400


def test_login():
	with app.app.test_client() as client:
		# Test that a user can login
		response = client.post('/login', json={'username': 'test_user', 'password': 'test_password'})
		assert response.status_code == 200

		# Test that a user cannot login with wrong password
		response = client.post('/login', json={'username': 'test_user', 'password': 'wrong_password'})
		assert response.status_code == 400

		# Test that a user cannot login if not registered
		response = client.post('/login', json={'username': 'non_existent_user', 'password': 'test_password'})
		assert response.status_code == 400


def test_create_club():
	with app.app.test_client() as client:
		# Test that a user can create a book club
		response = client.post('/create_club', json={'club_name': 'test_club', 'username': 'test_user'})
		assert response.status_code == 200
		assert 'test_club' in app.DATABASE['book_clubs']

		# Test that a book club cannot be created twice
		response = client.post('/create_club', json={'club_name': 'test_club', 'username': 'test_user'})
		assert response.status_code == 400


def test_join_club():
	with app.app.test_client() as client:
		# Test that a user can join a book club
		response = client.post('/join_club', json={'club_name': 'test_club', 'username': 'test_user2'})
		assert response.status_code == 200
		assert 'test_user2' in app.DATABASE['book_clubs']['test_club']['members']

		# Test that a user cannot join a book club that does not exist
		response = client.post('/join_club', json={'club_name': 'non_existent_club', 'username': 'test_user2'})
		assert response.status_code == 400

		# Test that a user cannot join a book club twice
		response = client.post('/join_club', json={'club_name': 'test_club', 'username': 'test_user2'})
		assert response.status_code == 400


def test_manage_club():
	with app.app.test_client() as client:
		# Test that a member can be removed from a book club
		response = client.post('/manage_club', json={'club_name': 'test_club', 'username': 'test_user2', 'action': 'remove'})
		assert response.status_code == 200
		assert 'test_user2' not in app.DATABASE['book_clubs']['test_club']['members']

		# Test that a member cannot be removed from a book club that does not exist
		response = client.post('/manage_club', json={'club_name': 'non_existent_club', 'username': 'test_user2', 'action': 'remove'})
		assert response.status_code == 400

		# Test that a non-member cannot be removed from a book club
		response = client.post('/manage_club', json={'club_name': 'test_club', 'username': 'non_existent_user', 'action': 'remove'})
		assert response.status_code == 400


def test_schedule_meeting():
	with app.app.test_client() as client:
		# Test that a meeting can be scheduled
		response = client.post('/schedule_meeting', json={'meeting_id': 'test_meeting', 'club_name': 'test_club', 'meeting_details': 'test_details'})
		assert response.status_code == 200
		assert 'test_meeting' in app.DATABASE['meetings']

		# Test that a meeting cannot be scheduled twice
		response = client.post('/schedule_meeting', json={'meeting_id': 'test_meeting', 'club_name': 'test_club', 'meeting_details': 'test_details'})
		assert response.status_code == 400


def test_send_reminder():
	with app.app.test_client() as client:
		# Test that a reminder can be sent
		response = client.post('/send_reminder', json={'meeting_id': 'test_meeting', 'reminder': 'test_reminder'})
		assert response.status_code == 200
		assert 'test_meeting' in app.DATABASE['notifications']

		# Test that a reminder cannot be sent for a non-existent meeting
		response = client.post('/send_reminder', json={'meeting_id': 'non_existent_meeting', 'reminder': 'test_reminder'})
		assert response.status_code == 400


def test_create_discussion():
	with app.app.test_client() as client:
		# Test that a discussion can be created
		response = client.post('/create_discussion', json={'discussion_id': 'test_discussion', 'club_name': 'test_club', 'topic': 'test_topic'})
		assert response.status_code == 200
		assert 'test_discussion' in app.DATABASE['discussions']

		# Test that a discussion cannot be created twice
		response = client.post('/create_discussion', json={'discussion_id': 'test_discussion', 'club_name': 'test_club', 'topic': 'test_topic'})
		assert response.status_code == 400


def test_post_comment():
	with app.app.test_client() as client:
		# Test that a comment can be posted
		response = client.post('/post_comment', json={'discussion_id': 'test_discussion', 'username': 'test_user', 'comment': 'test_comment'})
		assert response.status_code == 200
		assert {'username': 'test_user', 'comment': 'test_comment'} in app.DATABASE['discussions']['test_discussion']['comments']

		# Test that a comment cannot be posted in a non-existent discussion
		response = client.post('/post_comment', json={'discussion_id': 'non_existent_discussion', 'username': 'test_user', 'comment': 'test_comment'})
		assert response.status_code == 400


def test_suggest_book():
	with app.app.test_client() as client:
		# Test that a book can be suggested
		response = client.post('/suggest_book', json={'club_name': 'test_club', 'username': 'test_user', 'book_id': 'test_book'})
		assert response.status_code == 200
		assert 'test_book' in app.DATABASE['book_selections']

		# Test that a book cannot be suggested by a non-member
		response = client.post('/suggest_book', json={'club_name': 'test_club', 'username': 'non_existent_user', 'book_id': 'test_book2'})
		assert response.status_code == 400


def test_vote_book():
	with app.app.test_client() as client:
		# Test that a book can be voted
		response = client.post('/vote_book', json={'book_id': 'test_book', 'username': 'test_user'})
		assert response.status_code == 200
		assert app.DATABASE['book_selections']['test_book']['votes'] == 1

		# Test that a vote cannot be casted for a non-existent book
		response = client.post('/vote_book', json={'book_id': 'non_existent_book', 'username': 'test_user'})
		assert response.status_code == 400


def test_recommend_books():
	with app.app.test_client() as client:
		# Test that a book can be recommended
		app.DATABASE['user_profiles']['test_user'] = {'reading_history': [{'genre': 'fiction', 'book_id': 'book1'}, {'genre': 'fiction', 'book_id': 'book2'}, {'genre': 'non-fiction', 'book_id': 'book3'}]}
		app.DATABASE['book_selections']['book4'] = {'genre': 'fiction', 'club_name': 'test_club', 'suggester': 'test_user2', 'votes': 5}
		response = client.post('/recommend_books', json={'username': 'test_user'})
		assert response.status_code == 200
		assert {'genre': 'fiction', 'club_name': 'test_club', 'suggester': 'test_user2', 'votes': 5} in response.get_json()['recommendations']

		# Test that a book cannot be recommended for a non-existent user
		response = client.post('/recommend_books', json={'username': 'non_existent_user'})
		assert response.status_code == 400

if __name__ == '__main__':
	pytest.main()

