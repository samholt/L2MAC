import pytest
import app
from app import User

@pytest.fixture

def create_user():
	user = User(id='1', email='test@test.com', password='test')
	app.users[user.id] = user
	return user


def test_register(create_user):
	user = create_user
	response = app.register()
	assert response.status_code == 201
	assert response.get_json() == {'id': user.id}


def test_login(create_user):
	user = create_user
	response = app.login()
	assert response.status_code == 200
	assert response.get_json() == {'id': user.id}
