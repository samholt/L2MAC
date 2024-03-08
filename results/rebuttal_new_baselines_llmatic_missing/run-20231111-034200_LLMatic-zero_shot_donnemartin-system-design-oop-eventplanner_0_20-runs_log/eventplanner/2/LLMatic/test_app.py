import pytest
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello, World!', 200

@pytest.fixture

def client():
	with app.test_client() as client:
		with app.app_context():
			app.config['TESTING'] = True
			yield client


def test_home_page(client):
	response = client.get('/')
	assert response.status_code == 200
