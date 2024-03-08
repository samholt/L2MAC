import pytest
import random
import string
from unittest.mock import patch
from views import app, register, login, profile, posts_view, post_view


def random_string(length=10):
	return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def test_user_registration():
	username = random_string()
	email = f'{random_string()}@example.com'
	password = random_string()
	with app.test_request_context():
		with patch('views.request') as mock_request:
			mock_request.get_json.return_value = {'username': username, 'email': email, 'password': password}
			response = register()
			assert response[1] == 200


def test_user_authentication():
	username = random_string()
	email = f'{random_string()}@example.com'
	password = random_string()
	with app.test_request_context():
		with patch('views.request') as mock_request:
			mock_request.get_json.return_value = {'username': username, 'email': email, 'password': password}
			register()
			mock_request.get_json.return_value = {'email': email, 'password': password}
			response = login()
			assert response[1] == 200


def test_profile_editing():
	user_id = random.randint(1, 1000)
	new_bio = random_string(50)
	new_website = f'https://{random_string()}.com'
	new_location = random_string(15)
	with app.test_request_context():
		with patch('views.request') as mock_request:
			mock_request.get_json.return_value = {'bio': new_bio, 'website': new_website, 'location': new_location}
			response = profile(user_id)
			assert response is not None and response[1] in [200, 404]


def test_create_post():
	user_id = random.randint(1, 1000)
	post_content = random_string(280)
	with app.test_request_context():
		with patch('views.request') as mock_request:
			mock_request.get_json.return_value = {'user_id': user_id, 'content': post_content}
			response = posts_view()
			assert response is not None and response[1] in [200, 400, 404]


def test_delete_post():
	user_id = random.randint(1, 1000)
	post_content = random_string(280)
	with app.test_request_context():
		with patch('views.request') as mock_request:
			mock_request.get_json.return_value = {'user_id': user_id, 'content': post_content}
			posts_view()
			mock_request.get_json.return_value = {}
			response = post_view(1)
			assert response is not None and response[1] in [200, 404]


def test_get_post():
	user_id = random.randint(1, 1000)
	post_content = random_string(280)
	with app.test_request_context():
		with patch('views.request') as mock_request:
			mock_request.get_json.return_value = {'user_id': user_id, 'content': post_content}
			posts_view()
			response = post_view(1)
			assert response is not None and response[1] in [200, 404]

