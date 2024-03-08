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
	resp = client.get('/')
	assert resp.status_code == 200
	assert resp.data == b'Hello, World!'
