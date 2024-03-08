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


def test_view_public_profile(client, init_database):
	user = User.query.filter_by(username='user1').first()
	user.is_private = False
	db.session.commit()
	response = client.get('/profile/user1', follow_redirects=True)
	assert response.status_code == 200


def test_view_private_profile(client, init_database):
	user = User.query.filter_by(username='user1').first()
	user.is_private = True
	db.session.commit()
	response = client.get('/profile/user1', follow_redirects=True)
	assert response.status_code == 302


def test_edit_profile(client, init_database):
	client.post('/login', data=dict(username='user1', password='password1'), follow_redirects=True)
	response = client.post('/edit_profile', data=dict(bio='new bio', website_link='new_website.com', location='new location', is_private=False), follow_redirects=True)
	assert response.status_code == 200
	user = User.query.filter_by(username='user1').first()
	assert user.bio == 'new bio'
	assert user.website_link == 'new_website.com'
	assert user.location == 'new location'
	assert user.is_private == False
