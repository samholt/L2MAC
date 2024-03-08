import pytest
from flask import Flask
from interactions import app as interactions_app
from database import users_db, interactions_db

app = Flask(__name__)
app.config['TESTING'] = True

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.fixture
def init_database():
	users_db.clear()
	interactions_db.clear()
	users_db['test@test.com'] = {
		'email': 'test@test.com',
		'username': 'test',
		'password': 'test',
		'profile_picture': '',
		'bio': '',
		'website_link': '',
		'location': '',
		'private': False
	}
	yield

@pytest.mark.usefixtures('client', 'init_database')
class TestInteractions:
	def test_create_interaction(self, client):
		response = client.post('/interact', json={
			'interaction_id': '1',
			'post_id': '1',
			'type': 'like'
		})
		assert response.status_code == 201
		assert response.get_json() == {'message': 'Interaction created.'}

