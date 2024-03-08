import pytest
from cloudsafe.app import create_app, db
from cloudsafe.app.models import User


@pytest.fixture
def client():
	app = create_app()
	app.config['TESTING'] = True

	with app.test_client() as client:
		with app.app_context():
			db.create_all()
			yield client

	with app.app_context():
		db.drop_all()


@pytest.fixture
def auth(client):
	def login(email='test@test.com', password='test'):
		return client.post('/login', json={'email': email, 'password': password})

	def logout():
		return client.get('/logout')

	def register(email='test@test.com', password='test', name='test'):
		return client.post('/register', json={'email': email, 'password': password, 'name': name})

	return {'login': login, 'logout': logout, 'register': register}
