import pytest
from flask import Flask
from post import app as post_app
from database import users_db, posts_db

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
	posts_db.clear()
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
class TestPost:
	def test_create_post(self, client):
		response = client.post('/post', json={
			'post_id': '1',
			'content': 'This is a test post.',
			'image': ''
		})
		assert response.status_code == 201
		assert response.get_json() == {'message': 'Post created.'}

	def test_delete_post(self, client):
		response = client.delete('/post', json={'post_id': '1'})
		assert response.status_code == 200
		assert response.get_json() == {'message': 'Post deleted.'}

