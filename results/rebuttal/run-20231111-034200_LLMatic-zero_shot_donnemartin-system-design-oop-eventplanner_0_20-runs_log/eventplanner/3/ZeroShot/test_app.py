import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_event(client):
	response = client.post('/event', json={
		'id': 1,
		'type': 'Birthday',
		'date': '2022-12-31',
		'time': '18:00',
		'theme': 'Space',
		'color_scheme': 'Blue and White'
	})
	assert response.status_code == 201
	assert response.get_json() == {
		'id': 1,
		'type': 'Birthday',
		'date': '2022-12-31',
		'time': '18:00',
		'theme': 'Space',
		'color_scheme': 'Blue and White'
	}


def test_get_event(client):
	response = client.get('/event/1')
	assert response.status_code == 200
	assert response.get_json() == {
		'id': 1,
		'type': 'Birthday',
		'date': '2022-12-31',
		'time': '18:00',
		'theme': 'Space',
		'color_scheme': 'Blue and White'
	}
