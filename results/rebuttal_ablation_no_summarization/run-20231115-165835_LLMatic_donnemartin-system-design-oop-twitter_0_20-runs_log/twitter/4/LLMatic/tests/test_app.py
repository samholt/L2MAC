import pytest
from flask import Flask

@pytest.fixture

def create_app():
	app = Flask(__name__)
	@app.route('/')
	def home():
		return 'Hello, World!', 200
	return app


def test_home(create_app):
	client = create_app.test_client()
	response = client.get('/')
	assert response.status_code == 200
	assert response.data == b'Hello, World!'
