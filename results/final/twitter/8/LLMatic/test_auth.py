import pytest
import auth
from models import User, db
from werkzeug.security import generate_password_hash, check_password_hash

def setup_module():
	with auth.app.app_context():
		db.create_all()
		hashed_password = generate_password_hash('test', method='sha256')
		new_user = User(email='test@test.com', username='test', password=hashed_password)
		db.session.add(new_user)
		db.session.commit()

def test_register():
	with auth.app.app_context():
		response = auth.app.test_client().post('/register', json={
			'email': 'test2@test.com',
			'username': 'test2',
			'password': 'test'
		})
		assert response.status_code == 200

def test_login():
	with auth.app.app_context():
		response = auth.app.test_client().post('/login', json={
			'email': 'test@test.com',
			'password': 'test'
		})
		assert response.status_code == 200

def test_user_exists():
	with auth.app.app_context():
		user = User.query.filter_by(email='test@test.com').first()
		assert user is not None

def test_password_correct():
	with auth.app.app_context():
		user = User.query.filter_by(email='test@test.com').first()
		assert check_password_hash(user.password, 'test')
