import pytest
import views
import utils
from flask import Flask, jsonify

@pytest.fixture
def client():
	app = Flask(__name__)
	app.register_blueprint(views.views)
	with app.test_client() as client:
		yield client


def test_redirect_url(client):
	original_url = 'http://example.com'
	response = client.post('/shorten', json={'url': original_url})
	short_url = response.get_json()['short_url']
	response = client.get(f'/redirect/{short_url}')
	assert response.status_code == 302
	assert response.location == original_url


def test_analytics(client):
	original_url = 'http://example.com'
	response = client.post('/shorten', json={'url': original_url})
	short_url = response.get_json()['short_url']
	response = client.get(f'/redirect/{short_url}')
	assert response.status_code == 302
	assert response.location == original_url
	response = client.get(f'/analytics/{short_url}')
	assert response.status_code == 200
	assert 'clicks' in response.get_json()
	clicks = response.get_json()['clicks']
	assert len(clicks) > 0
	for click in clicks:
		assert 'click_time' in click
		assert 'location' in click
