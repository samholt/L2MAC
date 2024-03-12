import pytest
from app import app
from models import User, db


def test_home():
	with app.test_client() as c:
		resp = c.get('/')
		assert resp.status_code == 200
		assert resp.data == b'Hello, World!'


def test_register():
	with app.test_client() as c:
		# Get the register page
		resp = c.get('/register')
		assert resp.status_code == 200

		# Post to the register route with the form data
		resp = c.post('/register', data={'email': 'test@test.com', 'username': 'test', 'password': 'test', 'confirm_password': 'test'}, follow_redirects=True)
		assert resp.status_code == 200

		# Check that the user was created
		user = User.query.filter_by(email='test@test.com').first()
		assert user is not None
		assert user.check_password('test')


def test_login():
	with app.test_client() as c:
		resp = c.post('/login', data={'email': 'test@test.com', 'password': 'test'}, follow_redirects=True)
		assert resp.status_code == 200


def test_user_model():
	with app.app_context():
		user = User(email='test2@test.com', username='test2')
		user.set_password('test2')
		assert user.check_password('test2')
		assert not user.check_password('test')
		db.session.add(user)
		db.session.commit()
		user_from_db = User.query.filter_by(email='test2@test.com').first()
		assert user_from_db is not None
		assert user_from_db.check_password('test2')
		db.session.delete(user_from_db)
		db.session.commit()

