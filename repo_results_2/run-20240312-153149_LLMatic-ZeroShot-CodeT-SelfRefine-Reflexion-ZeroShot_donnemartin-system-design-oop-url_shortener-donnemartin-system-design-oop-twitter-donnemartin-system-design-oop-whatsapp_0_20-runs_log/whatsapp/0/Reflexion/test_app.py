import pytest
from app import app
from models import User, db

@pytest.fixture

def client():
	app.config['TESTING'] = True
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
	with app.test_client() as client:
		yield client

@pytest.fixture

def init_database():
	db.create_all()
	yield
	db.drop_all()


def test_register(client, init_database):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Registered successfully'}
	user = User.query.filter_by(email='test@test.com').first()
	assert user is not None
