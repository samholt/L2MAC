import pytest
from app import app
from models import db, URL

@pytest.fixture
def client():
	app.config['TESTING'] = True
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
	with app.test_client() as client:
		db.create_all()
		yield client
		db.drop_all()


def test_create(client):
	response = client.post('/', json={'original_url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()


def test_redirect_to_original(client):
	url = URL(original_url='https://www.google.com', short_url='abcde')
	db.session.add(url)
	db.session.commit()
	response = client.get('/abcde')
	assert response.status_code == 302


def test_stats(client):
	url = URL(original_url='https://www.google.com', short_url='abcde')
	db.session.add(url)
	db.session.commit()
	response = client.get('/abcde/stats')
	assert response.status_code == 200
	assert 'clicks' in response.get_json()
