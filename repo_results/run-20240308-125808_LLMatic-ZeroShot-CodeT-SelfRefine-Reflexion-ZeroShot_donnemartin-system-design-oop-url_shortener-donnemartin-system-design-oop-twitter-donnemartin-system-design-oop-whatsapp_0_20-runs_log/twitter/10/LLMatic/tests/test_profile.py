import pytest
from models import User, db
from app import app


def setup_function():
	with app.app_context():
		db.create_all()


def teardown_function():
	with app.app_context():
		db.session.remove()
		db.drop_all()


def test_get_public_profile():
	with app.app_context():
		with app.test_client() as client:
			user = User(username='testuser', email='testuser@example.com')
			user.set_password('testpassword')
			db.session.add(user)
			db.session.commit()
			response = client.get('/profile', json={'user_id': user.id})
			data = response.get_json()
			assert response.status_code == 200
			assert data['username'] == 'testuser'
			assert data['email'] == 'testuser@example.com'


def test_get_private_profile():
	with app.app_context():
		with app.test_client() as client:
			user = User(username='testuser', email='testuser@example.com', is_private=True)
			user.set_password('testpassword')
			db.session.add(user)
			db.session.commit()
			response = client.get('/profile', json={'user_id': user.id})
			data = response.get_json()
			assert response.status_code == 403
			assert data['message'] == 'This profile is private.'


def test_update_profile():
	with app.app_context():
		with app.test_client() as client:
			user = User(username='testuser', email='testuser@example.com')
			user.set_password('testpassword')
			db.session.add(user)
			db.session.commit()
			response = client.put('/profile', json={'user_id': user.id, 'bio': 'This is a test bio.'})
			data = response.get_json()
			assert response.status_code == 200
			assert data['message'] == 'Profile updated successfully'
			user = User.query.get(user.id)
			assert user.bio == 'This is a test bio.'
