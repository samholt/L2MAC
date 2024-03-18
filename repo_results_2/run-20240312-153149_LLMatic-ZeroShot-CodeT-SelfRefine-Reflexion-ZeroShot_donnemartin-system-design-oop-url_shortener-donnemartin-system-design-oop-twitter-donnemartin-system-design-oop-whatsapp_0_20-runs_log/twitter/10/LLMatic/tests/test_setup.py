import pytest
from app import app as flask_app


@pytest.fixture
def app():
	app = flask_app
	app.config['TESTING'] = True
	return app


def test_setup():
	assert True
