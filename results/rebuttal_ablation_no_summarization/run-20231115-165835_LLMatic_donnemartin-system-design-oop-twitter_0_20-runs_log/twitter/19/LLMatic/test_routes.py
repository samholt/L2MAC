from flask import json
from main import app


def test_register():
	response = app.test_client().post('/register', data=json.dumps({'email': 'test@test.com', 'username': 'test', 'password': 'password'}), content_type='application/json')
	data = json.loads(response.get_data(as_text=True))
	assert data['success']
	assert response.status_code == 200


def test_login():
	response = app.test_client().post('/login', data=json.dumps({'email': 'test@test.com', 'password': 'password'}), content_type='application/json')
	data = json.loads(response.get_data(as_text=True))
	assert data['success']
	assert response.status_code == 200


def test_edit_profile():
	response = app.test_client().post('/edit-profile', data=json.dumps({'email': 'test@test.com', 'profile_picture': 'new_picture.jpg', 'bio': 'new_bio', 'website_link': 'new_website.com', 'location': 'new_location'}), content_type='application/json')
	data = json.loads(response.get_data(as_text=True))
	assert data['success']
	assert response.status_code == 200


def test_toggle_privacy():
	response = app.test_client().post('/toggle-privacy', data=json.dumps({'email': 'test@test.com'}), content_type='application/json')
	data = json.loads(response.get_data(as_text=True))
	assert data['success']
	assert response.status_code == 200


def test_create_post():
	response = app.test_client().post('/create-post', data=json.dumps({'email': 'test@test.com', 'text_content': 'Hello, world!', 'images': ['pic1.jpg', 'pic2.jpg']}), content_type='application/json')
	data = json.loads(response.get_data(as_text=True))
	assert data['success']
	assert response.status_code == 200


def test_delete_post():
	response = app.test_client().post('/delete-post', data=json.dumps({'post_id': 0}), content_type='application/json')
	data = json.loads(response.get_data(as_text=True))
	assert data['success']
	assert response.status_code == 200


def test_search_posts():
	response = app.test_client().get('/search-posts?query=Hello')
	data = json.loads(response.get_data(as_text=True))
	assert 'Hello, world!' in [post['text_content'] for post in data['posts']]
	response = app.test_client().get('/search-posts?query=Goodbye')
	data = json.loads(response.get_data(as_text=True))
	assert 'Hello, world!' not in [post['text_content'] for post in data['posts']]
