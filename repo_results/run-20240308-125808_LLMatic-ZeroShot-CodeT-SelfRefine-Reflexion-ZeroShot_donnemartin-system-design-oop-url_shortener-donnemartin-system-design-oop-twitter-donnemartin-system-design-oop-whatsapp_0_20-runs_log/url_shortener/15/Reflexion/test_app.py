import pytest
import app
import uuid
from models import User, URL
from database import Database


def test_shorten_url():
	with app.app.test_client() as c:
		response = c.post('/shorten_url', json={'original_url': 'https://www.google.com'})
		assert response.status_code == 200
		assert 'shortened_url' in response.get_json()


def test_redirect_to_original():
	with app.app.test_client() as c:
		shortened_url = str(uuid.uuid4())[:8]
		url = URL(id=shortened_url, original_url='https://www.google.com', shortened_url=shortened_url, user_id=None, clicks=[], expiration=None)
		app.db.add_url(url)
		response = c.get(f'/{shortened_url}')
		assert response.status_code == 302


def test_register():
	with app.app.test_client() as c:
		response = c.post('/register', json={'username': 'test', 'password': 'test'})
		assert response.status_code == 200
		assert 'user_id' in response.get_json()


def test_login():
	with app.app.test_client() as c:
		user = User(id=str(uuid.uuid4()), username='test', password='test', urls=[])
		app.db.add_user(user)
		response = c.post('/login', json={'username': 'test', 'password': 'test'})
		assert response.status_code == 200
		assert 'user_id' in response.get_json()


def test_admin():
	with app.app.test_client() as c:
		response = c.get('/admin')
		assert response.status_code == 200
		assert 'users' in response.get_json()
		assert 'urls' in response.get_json()

