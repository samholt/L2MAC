import pytest
import app

@pytest.fixture

def client():
	app.app.config['TESTING'] = True

	with app.app.test_client() as client:
		yield client


def test_home_page(client):
	response = client.get('/')
	assert response.status_code == 200
