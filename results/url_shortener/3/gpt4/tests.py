import pytest
from main import app
from models import db, URL
from controllers import URLController

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

def test_create_short_url(client, init_database):
	response = client.post('/create', json={'long_url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()

	short_url = response.get_json()['short_url']
	url = URL.query.filter_by(short_url=short_url).first()
	assert url
	assert url.long_url == 'https://www.google.com'

	response = client.get('/' + short_url)
	assert response.status_code == 302
	assert url.click_count == 1

	response = client.get('/stats/' + short_url)
	assert response.status_code == 200
	assert response.get_json()['click_count'] == 1

	URLController.delete_expired_urls()
	assert URL.query.count() == 0
