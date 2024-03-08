import pytest
import app
from app import Event

@pytest.fixture(scope='module')
def test_client():
	flask_app = app.app
	flask_app.config['TESTING'] = True
	flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

	with flask_app.test_client() as testing_client:
		with flask_app.app_context():
			app.db.create_all()
			yield testing_client
		app.db.session.remove()
		app.db.drop_all()

@pytest.fixture(scope='module')
def new_event():
	return Event(id=1, type='Birthday', date='2022-12-12', time='18:00', theme='Space', color_scheme='Blue')


def test_create_event(test_client, new_event):
	response = test_client.post('/event', json=new_event.to_dict())
	assert response.status_code == 201
	assert response.get_json() == new_event.to_dict()


def test_update_event(test_client, new_event):
	app.db.session.add(new_event)
	app.db.session.commit()
	new_event.theme = 'Pirate'
	response = test_client.put(f'/event/{new_event.id}', json=new_event.to_dict())
	assert response.status_code == 200
	assert response.get_json() == new_event.to_dict()


def test_get_event(test_client, new_event):
	app.db.session.add(new_event)
	app.db.session.commit()
	response = test_client.get(f'/event/{new_event.id}')
	assert response.status_code == 200
	assert response.get_json() == new_event.to_dict()
