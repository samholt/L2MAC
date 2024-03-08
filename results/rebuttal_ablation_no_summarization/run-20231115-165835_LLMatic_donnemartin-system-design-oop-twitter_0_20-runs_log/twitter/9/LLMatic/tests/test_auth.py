import pytest
from app import app, db
from models import User
from flask_login import login_user

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.fixture
def init_database():
	with app.app_context():
		db.create_all()
		user1 = User(username='user1', email='user1@example.com')
		user1.set_password('password1')
		db.session.add(user1)
		db.session.commit()
		yield db
		db.drop_all()


def test_register(client, init_database):
	response = client.post('/register', data=dict(email='test2@test.com', username='test2', password='test2', confirm_password='test2'), follow_redirects=True)
	assert response.status_code == 200
	user = User.query.filter_by(email='test2@test.com').first()
	assert user is not None


def test_login(client, init_database):
	response = client.post('/login', data=dict(username='user1', password='password1'), follow_redirects=True)
	assert response.status_code == 200
	assert b'Login successful.' in response.data
