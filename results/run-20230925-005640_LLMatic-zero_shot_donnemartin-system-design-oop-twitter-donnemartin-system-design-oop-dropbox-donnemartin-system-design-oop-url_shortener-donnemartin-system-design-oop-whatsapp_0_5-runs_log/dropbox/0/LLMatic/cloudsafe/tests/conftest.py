import pytest
from cloudsafe.app import create_app


@pytest.fixture
def client():
	app = create_app()
	app.config['TESTING'] = True

	with app.test_client() as client:
		yield client
