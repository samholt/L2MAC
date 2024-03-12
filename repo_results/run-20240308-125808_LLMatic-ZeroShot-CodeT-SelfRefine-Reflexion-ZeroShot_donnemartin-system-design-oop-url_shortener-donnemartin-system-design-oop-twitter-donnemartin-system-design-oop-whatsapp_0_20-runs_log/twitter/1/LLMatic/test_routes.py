import pytest
import routes as app


def test_register():
	response = app.app.test_client().post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
	assert response.status_code == 201


def test_authenticate():
	response = app.app.test_client().post('/auth', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200


def test_password_reset_request():
	response = app.app.test_client().post('/password_reset', json={'email': 'test@test.com'})
	assert response.status_code == 200


def test_password_reset():
	response = app.app.test_client().post('/password_reset/token', json={'new_password': 'new_test'})
	assert response.status_code == 200


def test_update_profile():
	response = app.app.test_client().post('/update_profile', json={'email': 'test@test.com', 'token': 'JWT_TOKEN', 'profile_picture': 'new_pic.jpg', 'bio': 'new_bio', 'website_link': 'new_website.com', 'location': 'new_location'})
	assert response.status_code == 200


def test_create_post():
	response = app.app.test_client().post('/create_post', json={'email': 'test@test.com', 'token': 'JWT_TOKEN', 'text': 'new_post', 'images': ['new_image.jpg']})
	assert response.status_code == 201


def test_delete_post():
	response = app.app.test_client().delete('/delete_post/post_id', json={'email': 'test@test.com', 'token': 'JWT_TOKEN'})
	assert response.status_code == 200


def test_like_post():
	response = app.app.test_client().post('/like_post/post_id', json={'email': 'test@test.com', 'token': 'JWT_TOKEN'})
	assert response.status_code == 200


def test_retweet_post():
	response = app.app.test_client().post('/retweet_post/post_id', json={'email': 'test@test.com', 'token': 'JWT_TOKEN'})
	assert response.status_code == 200


def test_reply_post():
	response = app.app.test_client().post('/reply_post/post_id', json={'email': 'test@test.com', 'token': 'JWT_TOKEN', 'text': 'reply_text'})
	assert response.status_code == 200


def test_follow():
	response = app.app.test_client().post('/follow', json={'email': 'test@test.com', 'target_email': 'target@test.com', 'token': 'JWT_TOKEN'})
	assert response.status_code == 200


def test_unfollow():
	response = app.app.test_client().post('/unfollow', json={'email': 'test@test.com', 'target_email': 'target@test.com', 'token': 'JWT_TOKEN'})
	assert response.status_code == 200


def test_search():
	response = app.app.test_client().get('/search', query_string={'q': 'query'})
	assert response.status_code == 200


def test_send_message():
	response = app.app.test_client().post('/send_message', json={'sender_email': 'test@test.com', 'receiver_email': 'target@test.com', 'token': 'JWT_TOKEN', 'text': 'message_text'})
	assert response.status_code == 201

