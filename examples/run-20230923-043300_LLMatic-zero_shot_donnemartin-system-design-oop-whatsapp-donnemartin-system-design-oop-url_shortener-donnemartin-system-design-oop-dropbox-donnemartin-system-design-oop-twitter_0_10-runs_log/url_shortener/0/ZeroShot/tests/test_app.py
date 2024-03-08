import pytest
from app import app, db
from app.models import User, Url, Click

@pytest.fixture
def client():
	app.config['TESTING'] = True
	app.config['WTF_CSRF_ENABLED'] = False
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
	with app.test_client() as client:
		yield client

	with app.app_context():
		db.drop_all()

@pytest.fixture
def init_database():
	with app.app_context():
		db.create_all()
		yield db
		db.drop_all()


def test_home_page(client):
	response = client.get('/')
	assert response.status_code == 200


def test_register_page(client):
	response = client.get('/register')
	assert response.status_code == 200


def test_login_page(client):
	response = client.get('/login')
	assert response.status_code == 200


def test_account_page(client, init_database):
	user = User(username='test', password='test')
	init_database.session.add(user)
	init_database.session.commit()
	with client.session_transaction() as session:
		session['user_id'] = 1
	response = client.get('/account')
	assert response.status_code == 200


def test_admin_page(client, init_database):
	user = User(username='admin', password='admin', is_admin=True)
	init_database.session.add(user)
	init_database.session.commit()
	with client.session_transaction() as session:
		session['user_id'] = 1
	response = client.get('/admin')
	assert response.status_code == 200


def test_analytics_page(client, init_database):
	user = User(username='test', password='test')
	url = Url(original_url='https://www.google.com', short_url='google', creator=user)
	init_database.session.add(user)
	init_database.session.add(url)
	init_database.session.commit()
	with client.session_transaction() as session:
		session['user_id'] = 1
	response = client.get('/analytics/google')
	assert response.status_code == 200


def test_redirect_to_url(client, init_database):
	url = Url(original_url='https://www.google.com', short_url='google')
	init_database.session.add(url)
	init_database.session.commit()
	response = client.get('/google')
	assert response.status_code == 302
